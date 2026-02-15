# Astro Framework Governance Profile
## Enterprise Conformance Model (v1.0)

---

## Authority Notice

**CLASSIFICATION:** Framework Implementation Profile (Cross-Cutting)

**AUTHORITY LAYER:** 08_DEVELOPER_GOVERNANCE_LAYER → FRAMEWORK_PROFILES → FRONTEND

**CONTROL AUTHORITY RELATIONSHIP:**
- This profile **implements** governance controls defined in [02_API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md)
- This profile **references** Next.js profile patterns for SSR/API routes
- This profile **clarifies** island architecture, server components, and static/dynamic rendering
- This profile **does not** redefine any control from root governance documents

**COMPLIANCE STATEMENT:** This profile enforces security across Astro applications (3.0+). Non-conformance impacts server-side state leakage, hydration secrets, and API route authentication.

Astro operates as **Hybrid Static/Dynamic + API Gateway** with islands of interactivity.

---

## 1. Purpose & Scope

This document defines governance conformance requirements for Astro applications operating under EATGF.

**Scope:** Content-heavy sites with interactive components, documentation portals, marketing sites with auth, hybrid static/dynamic applications

**Non-Scope:** Pure static sites (no auth), pure SPAs (use React/Vue profiles)

---

## 2. Architectural Position

**EATGF Layer Placement:**
```
08_DEVELOPER_GOVERNANCE_LAYER
├── FRAMEWORK_PROFILES
│   └── FRONTEND
│       ├── Next.js (full-stack SSR)
│       └── Astro (static-first hybrid) ← THIS PROFILE
```

**Astro operates as:**
- Static site generator with dynamic capabilities
- Island architecture (opt-in JavaScript)
- Server components executed at build/request time
- API routes for backend logic
- Hybrid rendering (pre-render + on-demand)

**Critical Principle:** Astro renders HTML server-side by default. Client JavaScript is islands. Secrets must not leak into static HTML.

---

## 3. Governance Principles

### Principle 1: Build-Time vs Runtime Security (MANDATORY)

```astro
<!-- ❌ PROHIBITED: Secret in template (rendered to static HTML) -->
<script>
  const dbPassword = import.meta.env.SECRET_DB_PASSWORD;
</script>

<!-- ✅ COMPLIANT: Access secret only in server file -->
---
// src/pages/api/data.astro
const dbPassword = import.meta.env.SECRET_DB_PASSWORD;
const data = await fetchFromDB(dbPassword);
---

<!-- HTML: No secret exposed -->
<div>{data.name}</div>
```

### Principle 2: Island Security Boundary (MANDATORY)

```astro
---
// src/pages/dashboard.astro
const user = await getUser(Astro.request); // Server-side auth
---

<html>
  <body>
    <header>{user.name}</header>
    
    <!-- ✅ COMPLIANT: Island receives only public data -->
    <UserWidget client:load user={user.email} />
  </body>
</html>

<!-- src/components/UserWidget.tsx -->
interface Props {
  user: string; // Only public email
}

export default function UserWidget({ user }: Props) {
  // ✅ Island cannot access server secrets
  return <div>Hello {user}</div>;
}
```

### Principle 3: API Route Authentication (MANDATORY)

```typescript
// ✅ COMPLIANT: API route with auth check
import type { APIRoute } from 'astro';

export const GET: APIRoute = async (context) => {
  // ✅ Verify authentication
  const user = await verifyAuth(context.request.headers.get('cookie'));

  if (!user) {
    return new Response(null, { status: 401 });
  }

  // ✅ Server-side database access
  const invoices = await getInvoices(user.id, user.tenantId);

  return new Response(JSON.stringify(invoices), {
    headers: { 'Content-Type': 'application/json' }
  });
};
```

### Principle 4: Middleware Authentication (MANDATORY)

```typescript
// ✅ COMPLIANT: Middleware enforces auth
import { defineMiddleware } from 'astro:middleware';

export const onRequest = defineMiddleware(async (context, next) => {
  // ✅ Check auth before route handler
  const user = await verifyAuth(context.request.headers.get('cookie'));

  if (!user && context.request.url.includes('/admin')) {
    return new Response(null, { status: 401 });
  }

  // Add user to context
  context.locals.user = user;

  return next();
});
```

### Principle 5: Environment Variable Isolation (MANDATORY)

```diff
# ✅ .env.local (NEVER commit)
SECRET_DB_PASSWORD=super-secret
PUBLIC_API_URL=https://api.example.com

# ✅ Code: Use PUBLIC_ prefix for client
const apiUrl = import.meta.env.PUBLIC_API_URL;

# ✅ Server file: Access any variable
const dbPassword = import.meta.env.SECRET_DB_PASSWORD;
```

### Principle 6: Static Generation Security (MANDATORY)

```astro
---
// ✅ COMPLIANT: Pre-render with auth context
export async function getStaticPaths() {
  // ✅ Server-side: Fetch all user data
  const users = await getAllUsers();

  return users.map(user => ({
    params: { slug: user.slug },
    props: { userName: user.name } // Non-sensitive
  }));
}

const { userName } = Astro.props;
---

<h1>{userName}</h1>
```

### Principle 7: Form Handling Security (MANDATORY)

```astro
---
// src/pages/invoices.astro
import { validateInput } from '@/lib/validation';

// ✅ Form submission: Server-side validation
if (Astro.request.method === 'POST') {
  const formData = await Astro.request.formData();
  
  try {
    const validated = validateInput(formData);
    const invoice = await createInvoice(validated);
    return Astro.redirect(`/invoices/${invoice.id}`);
  } catch (error) {
    // Validation failed, re-render form with errors
  }
}
---

<form method="POST">
  <input name="amount" required />
  <button type="submit">Create</button>
</form>
```

### Principle 8: Hydration Data Leakage (MANDATORY)

```astro
---
// ✅ COMPLIANT: Don't hydrate with sensitive data
const user = await getUser(context);
const sensitiveData = await getSensitiveData(user.id);
---

<html>
  <body>
    <!-- ✅ Safe: No secrets passed to island -->
    <Dashboard client:load userName={user.name} />
    
    <!-- ❌ UNSAFE: Sensitive data leaked to client -->
    <!-- <Dashboard client:load secret={sensitiveData.key} /> -->
  </body>
</html>
```

---

## 4. Control 1: Authentication

**Objective:** Middleware-enforced auth with context locals.

### Compliant Implementation

```typescript
// middleware.ts
export const onRequest = defineMiddleware(async (context, next) => {
  const token = context.request.headers.get('cookie')?.match(/auth_token=([^;]+)/)?.[1];

  try {
    const user = await verifyToken(token);
    context.locals.user = user;
  } catch {
    context.locals.user = null;
  }

  return next();
});

// pages/dashboard.astro
---
const user = Astro.locals.user;

if (!user) {
  return Astro.redirect('/login');
}
---

<h1>Welcome {user.email}</h1>
```

---

## 5. Control 2: Authorization

**Objective:** Server-side authorization checks.

### Compliant Implementation

```typescript
// api/invoices.ts
export const POST: APIRoute = async (context) => {
  const user = context.locals.user;

  if (!user?.roles?.includes('admin')) {
    return new Response(null, { status: 403 });
  }

  const invoice = await createInvoice(await context.request.json());
  return new Response(JSON.stringify(invoice), { status: 201 });
};
```

---

## 6. Control 3-8: Standard Controls

(API versioning, input validation, rate limiting, testing, logging, zero trust networking)

All implemented with Astro-specific patterns:
- API routes handle HTTP methods
- Middleware for cross-cutting concerns
- Form POST for server-side submission
- Environment variables for config

---

## 7. Control Mapping

| EATGF Control | ISO 27001:2022 | NIST SSDF 1.1 | OWASP ASVS 5.0 |
|---|---|---|---|
| Authentication | A.8.2, A.8.3 | PW.2.1 | V2 |
| Authorization | A.8.5, A.8.9 | PW.2.2 | V4 |
| Versioning | A.8.28 | PW.4.2 | V14 |
| Input Validation | A.8.22 | PW.8.1 | V5 |
| Rate Limiting | A.8.22 | PW.8.2 | V11 |
| Testing | A.8.28 | PW.9.1 | V14 |
| Logging | A.8.15 | RV.1.1 | V15 |
| Zero Trust | A.8.1 | PW.1.1 | V1 |

---

## 8. Developer Checklist

- [ ] Server secrets never passed to client components
- [ ] Islands receive only non-sensitive props
- [ ] Middleware enforces authentication
- [ ] API routes validate input and authorize
- [ ] Environment variables properly prefixed (PUBLIC_)
- [ ] Form submissions POST to server endpoints
- [ ] Pre-rendered pages do not contain sensitive data
- [ ] HTTP-only cookies used for tokens
- [ ] CSP headers configured
- [ ] npm audit passes
- [ ] Build disables source maps
- [ ] No secrets in static HTML output

---

## 9. Version Information

| Field | Value |
|---|---|
| **Document Version** | 1.0 |
| **Astro Version** | 3.0+ |
| **Node.js** | 18+ |

---

**Authorization:** Enterprise Architecture Board
**Last Reviewed:** February 15, 2026
**Next Review:** August 15, 2026
