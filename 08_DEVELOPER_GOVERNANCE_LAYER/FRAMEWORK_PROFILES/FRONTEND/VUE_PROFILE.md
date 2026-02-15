# Vue.js Framework Governance Profile

## Enterprise Conformance Model (v1.0)

---

## Authority Notice

**CLASSIFICATION:** Framework Implementation Profile (Cross-Cutting)

**AUTHORITY LAYER:** 08_DEVELOPER_GOVERNANCE_LAYER → FRAMEWORK_PROFILES → FRONTEND

**CONTROL AUTHORITY RELATIONSHIP:**

- This profile **implements** governance controls defined in [02_API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md)
- This profile **references** secure SDLC requirements from [01_SECURE_SDLC_GOVERNANCE_STANDARD.md](../../01_SECURE_SDLC/SECURE_SDLC_GOVERNANCE_STANDARD.md)
- This profile **clarifies** progressive framework patterns with Composition API and Pinia state management
- This profile **does not** redefine any control from root governance documents

**COMPLIANCE STATEMENT:** This profile enforces security across Vue.js 3+ applications. Non-conformance impacts credential handling, reactivity security boundaries, and state management integrity.

---

## 1. Purpose & Scope

This document defines governance conformance requirements for Vue.js applications (v3+) operating under EATGF.

**Scope:** Single-page applications, progressive enhancement apps, dashboard applications, component libraries with security boundary

**Non-Scope:** Vue 2.x (legacy), Vue for content sites without auth

---

## 2. Architectural Position

**EATGF Layer Placement:**

```
08_DEVELOPER_GOVERNANCE_LAYER
├── FRAMEWORK_PROFILES
│   └── FRONTEND
│       ├── React (client-side, hooks)
│       ├── Next.js (SSR, hybrid)
│       ├── React Native (mobile)
│       └── Vue.js (progressive, Composition API) ← THIS PROFILE
```

**Vue.js operates as:**

- Progressive JavaScript framework
- Reactive data binding engine
- Component-scoped state management
- Composition API for logic reuse
- Template-driven DOM updates

**Critical Principle:** Reactivity system creates implicit data flows. Security decisions must not be implicitly reactive (must be explicit).

---

## 3. Governance Principles

### Principle 1: Centralized API Client Configuration (MANDATORY)

```typescript
// ❌ PROHIBITED: Direct fetch in components
<script setup>
import { ref } from 'vue';

const data = ref([]);

onMounted(async () => {
  const response = await fetch('https://api.example.com/invoices');
  data.value = await response.json();
});
</script>

// ✅ COMPLIANT: Centralized client
import { useApi } from '@/composables/useApi';

<script setup>
const { data: invoices, error, loading } = useApi('/invoices');
</script>
```

### Principle 2: Pinia for Secure State Management (MANDATORY)

```typescript
// ❌ PROHIBITED: Reactive tokens in component state
<script setup>
const token = ref(localStorage.getItem('token'));
</script>

// ✅ COMPLIANT: Pinia store with restricted state
import { defineStore } from 'pinia';

export const useAuthStore = defineStore('auth', () => {
  // ✅ Token in Pinia, not persisted
  const user = ref<User | null>(null);

  const setUser = (newUser: User) => {
    user.value = newUser;
  };

  return { user: readonly(user), setUser };
});
```

### Principle 3: Template XSS Prevention (MANDATORY)

```vue
<!-- ❌ PROHIBITED: Unescaped HTML -->
<template>
  <div v-html="userComment"></div>
</template>

<!-- ✅ COMPLIANT: Text interpolation (auto-escaped) -->
<template>
  <div>{{ userComment }}</div>
</template>

<!-- ✅ COMPLIANT: Sanitized if HTML needed -->
<template>
  <div>{{ sanitized }}</div>
</template>

<script setup>
import DOMPurify from "dompurify";
const sanitized = computed(() => DOMPurify.sanitize(userComment.value));
</script>
```

### Principle 4: Composition API Security (MANDATORY)

```typescript
// ✅ COMPLIANT: Extract logic into composables with security context
import { ref } from "vue";
import { useAuthStore } from "@/stores/auth";

export function useInvoices() {
  const authStore = useAuthStore();
  const invoices = ref([]);
  const error = ref(null);

  const fetchInvoices = async () => {
    try {
      // ✅ Use authenticated context from store
      const response = await api.get("/invoices", {
        headers: {
          Authorization: `Bearer ${authStore.token}`,
        },
      });
      invoices.value = response.data;
    } catch (e) {
      error.value = e.message;
    }
  };

  return { invoices: readonly(invoices), error, fetchInvoices };
}
```

### Principle 5: Route Guard Authentication (MANDATORY)

```typescript
// ✅ COMPLIANT: Router guards enforce auth
import { createRouter, createWebHistory } from "vue-router";
import { useAuthStore } from "@/stores/auth";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "/dashboard",
      component: Dashboard,
      meta: { requiresAuth: true },
    },
  ],
});

router.beforeEach((to, from, next) => {
  const authStore = useAuthStore();

  if (to.meta.requiresAuth && !authStore.user) {
    next("/login");
  } else {
    next();
  }
});
```

### Principle 6: Environment Variable Isolation (MANDATORY)

```typescript
// ✅ COMPLIANT: Prefixed env vars
const apiUrl = import.meta.env.VITE_API_URL;
const publicKey = import.meta.env.VITE_PUBLIC_KEY;

// ❌ PROHIBITED: Secrets
// process.env.DATABASE_PASSWORD (never in frontend)
// import.meta.env.PRIVATE_JWT_SECRET (exposed to bundle)
```

### Principle 7: Watch and Computed Security (MANDATORY)

```typescript
// ❌ RISKY: Reactive side effects without boundaries
watch(() => authStore.user, async (newUser) => {
  if (newUser?.role === 'admin') {
    // Too implicit, hard to audit
  }
});

// ✅ COMPLIANT: Explicit, auditable guards
const isAdmin = computed(() => {
  return authStore.user?.roles?.includes('admin') ?? false;
});

// Audit trail: explicit check in template
<template>
  <button v-if="isAdmin" @click="deleteInvoice">Delete</button>
</template>
```

### Principle 8: Build Security (MANDATORY)

```bash
# ✅ Vite build configuration
export default defineConfig({
  build: {
    sourcemap: false, // Disable source maps in production
    minify: 'terser',
    rollupOptions: {
      output: {
        manualChunks: {
          // Separate vendor chunk for better caching
          'vendor': ['vue', 'vue-router', 'pinia']
        }
      }
    }
  }
});
```

---

## 4. Control 1: Authentication

**Objective:** Establish user identity with HTTP-only cookies.

### Compliant Implementation

```typescript
export const useAuth = defineStore("auth", () => {
  const user = ref(null);
  const isLoading = ref(true);

  const fetchUser = async () => {
    try {
      const response = await api.get("/auth/user");
      user.value = response.data;
    } catch {
      user.value = null;
    } finally {
      isLoading.value = false;
    }
  };

  const login = async (email: string, password: string) => {
    await api.post("/auth/login", { email, password });
    // ✅ Server sets HTTP-only cookie
    await fetchUser();
  };

  const logout = async () => {
    await api.post("/auth/logout");
    user.value = null;
  };

  onMounted(() => fetchUser());

  return { user: readonly(user), isLoading, login, logout };
});
```

---

## 5. Control 2: Authorization

**Objective:** Server-side authorization enforcement.

### Compliant Implementation

```typescript
export const useAuthorization = (action: string) => {
  const authStore = useAuthStore();
  const canAccess = ref(false);

  watch(() => authStore.user, async () => {
    try {
      const response = await api.get('/auth/authorize', {
        params: { action }
      });
      canAccess.value = response.data.authorized;
    } catch {
      canAccess.value = false;
    }
  });

  return { canAccess: readonly(canAccess) };
};

export function useCanDeleteInvoice(invoiceId: string) {
  return useAuthorization(`delete_invoice_${invoiceId}`);
}

// Usage in component
<script setup>
const { canAccess: canDelete } = useCanDeleteInvoice(invoiceId);
</script>

<template>
  <button v-if="canDelete" @click="deleteInvoice">Delete</button>
</template>
```

---

## 6. Control 3: Versioning

**Objective:** API version management.

### Compliant Implementation

```typescript
const API_VERSION = "v2";

export const api = axios.create({
  baseURL: `${import.meta.env.VITE_API_URL}/${API_VERSION}`,
  withCredentials: true,
});

api.interceptors.response.use((response) => {
  const version = response.headers["x-api-version"];
  if (version && version !== API_VERSION) {
    console.warn(`Version mismatch: expected ${API_VERSION}, got ${version}`);
  }
  return response;
});
```

---

## 7. Control 4: Input Validation

**Objective:** Validate all user input before submission.

### Compliant Implementation

```typescript
import { z } from "zod";

const InvoiceSchema = z.object({
  amount: z.number().positive(),
  currency: z.enum(["USD", "EUR"]),
  items: z
    .array(
      z.object({
        description: z.string().min(1),
        quantity: z.number().min(1).int(),
      }),
    )
    .min(1),
});

export const useInvoiceForm = () => {
  const form = reactive(InvoiceSchema.parse({}));
  const errors = reactive({});

  const submit = async () => {
    try {
      const validated = InvoiceSchema.parse(form);
      await api.post("/invoices", validated);
    } catch (error) {
      if (error instanceof z.ZodError) {
        Object.assign(errors, error.flatten().fieldErrors);
      }
    }
  };

  return { form, errors, submit };
};
```

---

## 8. Control 5: Rate Limiting

**Objective:** Handle rate limit responses gracefully.

### Compliant Implementation

```typescript
api.interceptors.response.use(
  (response) => response,
  async (error) => {
    if (error.response?.status === 429) {
      const retryAfter = parseInt(
        error.response.headers["retry-after"] || "60",
      );

      await new Promise((resolve) => setTimeout(resolve, retryAfter * 1000));

      return api.request(error.config);
    }

    return Promise.reject(error);
  },
);
```

---

## 9. Control 6: Testing & Documentation

**Objective:** Test coverage > 80%, security-focused tests.

### Compliant Implementation

```typescript
import { describe, it, expect, vi } from "vitest";
import { mount } from "@vue/test-utils";
import { useAuth } from "@/stores/auth";

describe("Authentication", () => {
  it("fetches user on component mount", async () => {
    const wrapper = mount(Dashboard);

    await wrapper.vm.$nextTick();

    expect(wrapper.find(".user-name").exists()).toBe(true);
  });

  it("redirects to login on 401", async () => {
    vi.mock("@/api", () => ({
      api: {
        get: vi.fn().mockRejectedValue({
          response: { status: 401 },
        }),
      },
    }));

    const authStore = useAuth();
    expect(authStore.user).toBeNull();
  });
});
```

---

## 10. Control 7: Logging & Observability

**Objective:** Structured logging with correlation IDs.

### Compliant Implementation

```typescript
import { ref, watch } from "vue";

export const useLogger = (component: string) => {
  const correlationId = ref(crypto.randomUUID());

  return {
    info: (message: string, data?: any) => {
      console.log(`[${component}] ${message}`, {
        correlationId: correlationId.value,
        ...data,
      });
    },
    error: (message: string, error?: Error) => {
      console.error(`[${component}] ${message}`, {
        correlationId: correlationId.value,
        error: error?.message,
      });
    },
  };
};
```

---

## 11. Control 8: Zero Trust Networking

**Objective:** HTTPS enforcement and secure cookies.

### Compliant Implementation

```typescript
// ✅ Vite config enforcement
export default defineConfig({
  server: {
    https: true, // Development server uses HTTPS
  },
});

// ✅ API client enforces HTTPS
const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
  withCredentials: true, // Send HTTP-only cookies
});
```

---

## 12. Multi-Tenancy Controls

**Objective:** Tenant isolation via authenticated context.

### Compliant Implementation

```typescript
export const useTenant = () => {
  const authStore = useAuthStore();

  const tenantId = computed(() => {
    return authStore.user?.tenantId ?? null;
  });

  return { tenantId };
};
```

---

## 13. Dependency & Supply Chain Governance

**Objective:** npm audit integration.

### Compliant Implementation

```bash
# package.json scripts
"audit": "npm audit --audit-level=high",
"build": "vue-tsc && vite build"
```

---

## 14. Control Mapping

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

## 15. Developer Checklist

- [ ] HTTP-only cookies used for tokens
- [ ] Pinia store for state management (not localStorage)
- [ ] Router guards enforce authentication
- [ ] Template uses text interpolation (auto-escaped), not v-html
- [ ] Composition API for logic reuse with explicit security context
- [ ] API client centralized with correlation IDs
- [ ] Environment variables prefixed (VITE\_)
- [ ] Watch/computed guards audit-complete and explicit
- [ ] npm audit passes
- [ ] Build disables source maps
- [ ] 80%+ test coverage
- [ ] No dangerouslySetInnerHTML equivalent (v-html) without sanitization
- [ ] Middleware/guards validate authorization

---

## Official References

- Vue.js Documentation: <https://vuejs.org/guide/>
- Vue.js Security Best Practices: <https://vuejs.org/guide/best-practices/security.html>
- OWASP Web Security: <https://owasp.org/www-project-web-security-testing-guide/>
- Vue Composition API: <https://vuejs.org/api/composition-api-setup.html>
- NIST SP 800-218: <https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-218.pdf>

---

## 16. Version Information

| Field                | Value                   |
| -------------------- | ----------------------- |
| **Document Version** | 1.0                     |
| **Change Type**      | Major (Initial Release) |
| **Issue Date**       | February 15, 2026       |
| **Vue Version**      | 3.3+                    |
| **Pinia Version**    | 2.1+                    |
| **Node.js**          | 18+                     |

---

**Authorization:** Enterprise Architecture Board (EATGF Governance)
**Last Reviewed:** February 15, 2026
**Next Review:** August 15, 2026
