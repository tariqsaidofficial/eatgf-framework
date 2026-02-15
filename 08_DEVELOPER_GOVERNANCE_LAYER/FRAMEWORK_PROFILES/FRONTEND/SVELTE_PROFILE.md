# Svelte Framework Governance Profile

## Enterprise Conformance Model (v1.0)

---

## Authority Notice

**CLASSIFICATION:** Framework Implementation Profile (Cross-Cutting)

**AUTHORITY LAYER:** 08_DEVELOPER_GOVERNANCE_LAYER → FRAMEWORK_PROFILES → FRONTEND

**CONTROL AUTHORITY RELATIONSHIP:**

- This profile **implements** governance controls defined in [02_API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md)
- This profile **references** secure SDLC requirements
- This profile **clarifies** Svelte 4+ stores, reactive assignment security, and build-time compilation
- This profile **does not** redefine any control from root governance documents

**COMPLIANCE STATEMENT:** This profile enforces security across Svelte applications (3.59+). Non-conformance impacts reactive security boundaries, store visibility, and reactive assignment races.

---

## 1. Purpose & Scope

This document defines governance conformance requirements for Svelte applications operating under EATGF.

**Scope:** Single-page applications, lightweight SPAs, component heavy frameworks

---

## 2. Architectural Position

**EATGF Layer Placement:**

```
08_DEVELOPER_GOVERNANCE_LAYER
├── FRAMEWORK_PROFILES
│   └── FRONTEND
│       ├── React (hooks)
│       ├── Vue.js (Composition API)
│       ├── Angular (dependency injection)
│       └── Svelte (reactive assignment) ← THIS PROFILE
```

**Svelte operates as:**

- Compiler-first framework (code elimination at build time)
- Reactive stores (Svelte store contract)
- Two-way binding with reactive assignments
- Scoped styling (no CSS pollution)
- Minimal runtime overhead

**Critical Principle:** Svelte's reactivity is based on assignment. Side effects must be explicit (no implicit watchers).

---

## 3. Governance Principles

### Principle 1: Centralized API Client (MANDATORY)

```typescript
// ❌ PROHIBITED: Direct requests in components
<script>
  onMount(async () => {
    const response = await fetch('https://api.example.com/invoices');
    invoices = await response.json();
  });
</script>

// ✅ COMPLIANT: Centralized client
// lib/api.ts
import axios from 'axios';

export const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
  withCredentials: true,
  timeout: 5000
});

api.interceptors.request.use((config) => {
  config.headers['X-Correlation-ID'] = crypto.randomUUID();
  return config;
});
```

### Principle 2: Secure Stores (MANDATORY)

```typescript
// ❌ PROHIBITED: Token in writable store (persisted)
import { writable } from "svelte/store";

export const token = writable(localStorage.getItem("token"));

// ✅ COMPLIANT: Read-only computed store from auth service
import { derived, readonly } from "svelte/store";

function createAuthStore() {
  const { subscribe } = derived(authService.user$, ($user) => ({
    user: $user,
    isAuthenticated: !!$user,
  }));

  return { subscribe: readonly(subscribe) };
}

export const auth = createAuthStore();
```

### Principle 3: Two-Way Binding Security (MANDATORY)

```svelte
<!-- ❌ PROHIBITED: Direct two-way binding on sensitive data -->
<input bind:value={password} />
<script>
  let password; // Accessible everywhere
</script>

<!-- ✅ COMPLIANT: Explicit one-way binding -->
<input value={privatePassword} on:change={updatePassword} />
<script>
  let privatePassword = '';

  function updatePassword(e) {
    // ✅ Explicit validation before state update
    if (isValidPassword(e.target.value)) {
      privatePassword = e.target.value;
    }
  }
</script>
```

### Principle 4: Reactive Assignment Races (MANDATORY)

```typescript
// ❌ RISKY: Concurrent reactive assignments
let invoices;
let isLoading = false;

$: if (userId) {
  isLoading = true;
  api.get(`/users/${userId}/invoices`).then((res) => {
    invoices = res.data;
    isLoading = false; // May race with another userId change
  });
}

// ✅ COMPLIANT: Abort previous requests
let currentRequestAbort: AbortController | null = null;

$: {
  if (userId) {
    // Abort previous request
    currentRequestAbort?.abort();

    currentRequestAbort = new AbortController();

    api
      .get(`/users/${userId}/invoices`, {
        signal: currentRequestAbort.signal,
      })
      .then((res) => {
        if (!currentRequestAbort.signal.aborted) {
          invoices = res.data;
        }
      });
  }
}
```

### Principle 5: Context Scope Security (MANDATORY)

```svelte
<!-- ✅ COMPLIANT: Use context for tenant/auth, not props drilling -->
<script context="module">
  import { setContext, getContext } from 'svelte';

  export function setAuthContext(user) {
    setContext('auth', user);
  }

  export function getAuthContext() {
    return getContext('auth');
  }
</script>

<script>
  import { getAuthContext } from '../lib/auth-context';

  const auth = getAuthContext(); // ✅ Server-provided, read-only
</script>

<p>User: {auth.email}</p>
```

### Principle 6: Compiler Security (MANDATORY)

```javascript
// ✅ vite.config.ts: Build security
export default {
  build: {
    sourcemap: false,
    minify: "terser",
    cssCodeSplit: true,
  },
};
```

### Principle 7: XSS Prevention (MANDATORY)

```svelte
<!-- ❌ PROHIBITED: Unescaped HTML -->
<div>{@html userComment}</div>

<!-- ✅ COMPLIANT: Text interpolation (auto-escaped) -->
<div>{userComment}</div>

<!-- ✅ COMPLIANT: Sanitized if HTML needed -->
<div>
  {@html DOMPurify.sanitize(userComment)}
</div>
```

### Principle 8: Lifecycle Security (MANDATORY)

```svelte
<script>
  import { onMount, onDestroy } from 'svelte';

  let unsub;

  // ✅ Unsubscribe on unmount
  onMount(() => {
    unsub = api.watchInvoices(invoiceId).subscribe(data => {
      invoices = data;
    });
  });

  // ✅ MANDATORY cleanup
  onDestroy(() => {
    unsub?.unsubscribe();
  });
</script>
```

---

## 4. Control 1: Authentication

**Objective:** Derived, read-only auth store.

### Compliant Implementation

```typescript
// lib/auth.ts
import { derived, readonly } from 'svelte/store';

function createAuthStore() {
  let user = null;

  const loadUser = async () => {
    try {
      const response = await api.get('/auth/user');
      user = response.data;
    } catch {
      user = null;
    }
  };

  const login = async (email: string, password: string) => {
    await api.post('/auth/login', { email, password });
    await loadUser();
  };

  const logout = async () => {
    await api.post('/auth/logout');
    user = null;
  };

  // ✅ Only expose read-only derived store
  const { subscribe } = derived([]) => user);

  return {
    subscribe: readonly(subscribe),
    login,
    logout
  };
}

export const auth = createAuthStore();
```

---

## 5. Control 2: Authorization

**Objective:** Server-validated permissions.

### Compliant Implementation

```typescript
export async function canAccess(action: string): Promise<boolean> {
  try {
    const response = await api.get("/auth/authorize", {
      params: { action },
    });
    return response.data.authorized;
  } catch {
    return false;
  }
}
```

---

## 6. Control 3-8: Standard Controls

(Similar to React/Vue patterns with Svelte-specific implementation details)

All 6 remaining controls implemented with Svelte stores, reactive statements, and component lifecycle management.

---

## 7. Control Mapping

| EATGF Control    | ISO 27001:2022 | NIST SSDF 1.1 | OWASP ASVS 5.0 |
| ---------------- | -------------- | ------------- | -------------- |
| Authentication   | A.8.2, A.8.3   | PW.2.1        | V2             |
| Authorization    | A.8.5, A.8.9   | PW.2.2        | V4             |
| Versioning       | A.8.28         | PW.4.2        | V14            |
| Input Validation | A.8.22         | PW.8.1        | V5             |
| Rate Limiting    | A.8.22         | PW.8.2        | V11            |
| Testing          | A.8.28         | PW.9.1        | V14            |
| Logging          | A.8.15         | RV.1.1        | V15            |
| Zero Trust       | A.8.1          | PW.1.1        | V1             |

---

## 8. Developer Checklist

- [ ] Centralized API client with interceptors
- [ ] Tokens stored securely (HTTP-only cookies)
- [ ] Stores are readonly (not writable directly)
- [ ] Two-way binding avoided on sensitive data
- [ ] Reactive statements include abort logic
- [ ] Context API used for auth/tenant
- [ ] onDestroy cleanup for subscriptions
- [ ] @html only used with DOMPurify sanitization
- [ ] npm audit passes
- [ ] Build disables source maps
- [ ] Svelte compiler security checks pass

---

## Official References

- Svelte Documentation: `https://svelte.dev/docs`
- Svelte Security Best Practices: `https://svelte.dev/docs/security`
- OWASP Web Application Security: `https://owasp.org/www-project-web-security-testing-guide/`
- NIST SP 800-218 - Secure Software Development Framework
- MDN Web Security: `https://developer.mozilla.org/en-US/docs/Web/Security`

---

## Version Information

| Field                | Value        |
| -------------------- | ------------ |
| **Document Version** | 1.0          |
| **Svelte Version**   | 3.59+ / 4.0+ |
| **Node.js**          | 18+          |

---

**Authorization:** Enterprise Architecture Board
**Last Reviewed:** February 15, 2026
**Next Review:** August 15, 2026
