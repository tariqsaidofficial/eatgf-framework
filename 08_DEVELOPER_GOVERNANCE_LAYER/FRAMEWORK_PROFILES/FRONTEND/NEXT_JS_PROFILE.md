# Next.js Framework Governance Profile

## Enterprise Conformance Model (v1.0)

---

## Authority Notice

**CLASSIFICATION:** Framework Implementation Profile (Cross-Cutting)

**AUTHORITY LAYER:** 08_DEVELOPER_GOVERNANCE_LAYER → FRAMEWORK_PROFILES → FRONTEND

**CONTROL AUTHORITY RELATIONSHIP:**

- This profile **implements** governance controls defined in [02_API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md)
- This profile **references** secure SDLC requirements from [01_SECURE_SDLC_GOVERNANCE_STANDARD.md](../../01_SECURE_SDLC/SECURE_SDLC_GOVERNANCE_STANDARD.md)
- This profile **clarifies** DevSecOps patterns from [03_DEVSECOPS_GOVERNANCE_STANDARD.md](../../03_DEVSECOPS_GOVERNANCE_STANDARD.md)
- This profile **does not** redefine any control from root governance documents
- This profile **supersedes** React profile for SSR applications

**COMPLIANCE STATEMENT:** This profile enforces unified security across server-rendered and client-side React. Non-conformance compromises:

- Server-side session management
- XSS/CSRF attack surface
- Hydration security boundary
- API route authentication
- Environment variable isolation

Next.js operates as both **Backend API Layer** (API routes) and **Frontend Presentation Layer** (SSR). Dual governance required.

---

## 1. Purpose & Scope

This document defines governance conformance requirements for Next.js applications operating under EATGF.

**Scope:** Server-side rendered SPA, hybrid SSR/CSR applications, API-driven full-stack apps, edge-deployed applications

**Non-Scope:** Pure client-side React (React Profile), static site generation without auth (separate guidance)

---

## 2. Architectural Position

**EATGF Layer Placement:**

```
08_DEVELOPER_GOVERNANCE_LAYER
├── FRAMEWORK_PROFILES
│   ├── BACKEND (Django, FastAPI, Node.js, Spring Boot)
│   ├── FRONTEND
│   │   ├── React (client-side only)
│   │   ├── Next.js (hybrid SSR/CSR) ← THIS PROFILE
│   │   └── React Native (mobile)
│   └── INFRASTRUCTURE
```

**Next.js operates as:**

- **Server-side:** API routes, server components, middleware (backend-like auth)
- **Client-side:** React components in browser (frontend-like XSS risks)
- **Hybrid:** Page rendering at build-time, request-time, runtime
- **Edge:** Cloudflare Workers, Vercel Edge Functions (request interception)

**Next.js must conform to:**

- **02_API_GOVERNANCE:** API route security (server-side)
- **01_SECURE_SDLC:** Full-stack development lifecycle
- **05_DOMAIN_FRAMEWORKS:** Framework-specific build pipeline
- **Backend API controls** (API routes like REST backend)
- **Frontend controls** (Client components like React frontend)

**Critical Principle:** Next.js has dual attack surface. Server-side auth must not leak to client. Client-side rendering must not trust server data implicitly.

---

## 3. Governance Principles

### Principle 1: Server/Client Trust Boundary (MANDATORY)

Next.js must maintain strict separation between server context and client context.

```typescript
// ❌ PROHIBITED: Leaking server secret to client
export const getServerSideProps = async (context) => {
  const secret = process.env.DATABASE_PASSWORD; // Server secret
  return {
    props: {
      dbSecret: secret // ← EXPOSED to client bundle
    }
  };
};

function Page({ dbSecret }) {
  return <div>{dbSecret}</div>;
}

// ✅ COMPLIANT: Process secrets server-side only
export const getServerSideProps = async (context) => {
  const dbSecret = process.env.DATABASE_PASSWORD;
  const data = await fetchFromDB(dbSecret); // Use secret server-side

  return {
    props: {
      publicData: data // Send only sanitized public data
    }
  };
};
```

**Enforcement:**

- `process.env.SECRET_*` never passed to `props`
- `process.env.NEXT_PUBLIC_*` exclusively for client-accessible config
- Server components use secrets directly
- Use `useServer` directive to mark secret-aware functions

---

### Principle 2: Hydration Security (MANDATORY)

Server-rendered HTML must match client-hydrated HTML exactly. Mismatches create XSS vulnerabilities.

```typescript
// ❌ PROHIBITED: Non-deterministic rendering
function Page() {
  const [timestamp] = useState(() => Date.now()); // Random
  return <div>{timestamp}</div>;
  // Server renders: <div>1708000000</div>
  // Client hydrates: <div>1708000001</div> ← MISMATCH
}

// ✅ COMPLIANT: Deterministic rendering
function Page({ timestamp }: { timestamp: number }) {
  return <div>{timestamp}</div>;
  // Both server and client render same value
}

export const getServerSideProps = async () => {
  return {
    props: {
      timestamp: Math.floor(Date.now() / 1000)
    }
  };
};
```

**Enforcement:**

- No `useEffect` for critical rendering (decoration only)
- SSR output validation required
- Mismatch detection enabled (`suppressHydrationWarning` audited)

---

### Principle 3: API Route Authentication (MANDATORY)

API routes in `/pages/api/` behave like backend endpoints. Same authentication controls apply.

```typescript
// ✅ COMPLIANT: Authenticate API route via middleware
import type { NextApiRequest, NextApiResponse } from "next";
import { verifyAuth } from "@/lib/auth";

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse,
) {
  // ✅ MANDATORY: Verify authentication on every request
  const user = await verifyAuth(req.cookies.token);

  if (!user) {
    return res.status(401).json({ error: "Unauthorized" });
  }

  if (req.method === "GET") {
    const invoices = await fetchUserInvoices(user.id, user.tenantId);
    return res.json(invoices);
  }

  if (req.method === "POST") {
    const validated = InvoiceSchema.parse(req.body);
    const invoice = await createInvoice(validated, user.tenantId);
    return res.status(201).json(invoice);
  }

  res.status(405).end();
}
```

**Enforcement:**

- Middleware pattern enforces auth on all routes
- No public API routes without explicit `POST /api/public/*` marker
- Rate limiting applied at route level
- Input validation on every endpoint

---

### Principle 4: Server Component Security (MANDATORY)

React Server Components (RSC) execute on server. Direct database access possible but risky.

```typescript
// ✅ COMPLIANT: Use 'use server' for sensitive operations
'use server'; // Top of file

import { db } from '@/lib/db';

export async function deleteInvoice(invoiceId: string, userId: string) {
  // ✅ Only called from server, never from client
  // ✅ User ID from authenticated session, not client

  const invoice = await db.invoices.findUnique({ where: { id: invoiceId } });

  if (invoice.userId !== userId) {
    throw new Error('Unauthorized');
  }

  return await db.invoices.delete({ where: { id: invoiceId } });
}

// Client component imports and calls it
'use client';

import { deleteInvoice } from './actions';

export function InvoiceCard({ invoice, userId }) {
  return (
    <button onClick={() => deleteInvoice(invoice.id, userId)}>
      Delete
    </button>
  );
}
```

**Enforcement:**

- 'use server' functions never exposed in client bundle
- Credentials/secrets accessible in server components only
- Client → server function calls properly typed via React 19+

---

### Principle 5: Environment Variable Isolation (MANDATORY)

Next.js exposes `NEXT_PUBLIC_*` to browser. All others server-side only.

```typescript
// ✅ COMPLIANT: Proper env var usage
// .env.local (never committed)
DATABASE_URL=postgres://...
JWT_SECRET=super-secret-key
NEXT_PUBLIC_API_URL=https://api.example.com

// src/lib/config.ts
export const config = {
  // ✓ Client-accessible config
  apiUrl: process.env.NEXT_PUBLIC_API_URL,

  // ✗ Secret - NOT exposed to client
  // process.env.JWT_SECRET is server-side only
};

// pages/api/auth.ts (server-side)
export default async function handler(req, res) {
  const secret = process.env.JWT_SECRET; // ✓ Accessible
  const token = jwt.sign({ ... }, secret);
  res.setHeader('Set-Cookie', `token=${token}; HttpOnly; Secure`);
}
```

**Enforcement:**

- Prefixes must be explicit: `NEXT_PUBLIC_*` (client), `[A-Z_]*` (server)
- Build fails if server var used in client code
- `.env.local` in `.gitignore` mandatory

---

### Principle 6: Middleware Authentication (MANDATORY)

Next.js middleware intercepts all requests. Perfect for auth checks.

```typescript
// middleware.ts (at project root)
import { NextRequest, NextResponse } from "next/server";
import { verifyAuth } from "@/lib/auth";

export async function middleware(request: NextRequest) {
  const { pathname } = request.nextUrl;

  // ✅ Public routes (no auth required)
  if (pathname === "/login" || pathname === "/signup") {
    return NextResponse.next();
  }

  // ✅ Protected routes (require auth)
  if (pathname.startsWith("/dashboard")) {
    const token = request.cookies.get("auth_token")?.value;

    if (!token) {
      return NextResponse.redirect(new URL("/login", request.url));
    }

    try {
      const user = await verifyAuth(token);

      // ✅ Add user to request headers (forwarded to page)
      const requestHeaders = new Headers(request.headers);
      requestHeaders.set("x-user-id", user.id);
      requestHeaders.set("x-tenant-id", user.tenantId);

      return NextResponse.next({
        request: {
          headers: requestHeaders,
        },
      });
    } catch (error) {
      return NextResponse.redirect(new URL("/login", request.url));
    }
  }

  return NextResponse.next();
}

export const config = {
  matcher: ["/((?!_next/static|favicon.ico).*)"], // Apply to all routes
};
```

**Enforcement:**

- Middleware runs on every request (before pages/API)
- Session validation required
- Redirect to login on auth failure

---

### Principle 7: XSS Prevention in SSR (MANDATORY)

Server-rendered HTML is vulnerable to injection if not properly escaped.

```typescript
// ❌ PROHIBITED: Unescaped user input in SSR
export const getServerSideProps = async () => {
  const userComment = await fetchComment();
  return {
    props: {
      comment: userComment // If contains HTML, XSS on render
    }
  };
};

export default function Post({ comment }) {
  return <div dangerouslySetInnerHTML={{ __html: comment }} />;
}

// ✅ COMPLIANT: Escape and sanitize
import DOMPurify from 'isomorphic-dompurify';

export const getServerSideProps = async () => {
  const userComment = await fetchComment();

  // ✅ Sanitize on server before rendering
  const sanitized = DOMPurify.sanitize(userComment, {
    ALLOWED_TAGS: ['b', 'i', 'em'],
    ALLOWED_ATTR: []
  });

  return {
    props: { comment: sanitized }
  };
};

export default function Post({ comment }) {
  return (
    <div>
      {comment} {/* Rendered as text, XSS-safe */}
    </div>
  );
}
```

---

### Principle 8: Build-Time Security Verification (MANDATORY)

Next.js build process must verify security constraints.

```bash
# ✅ next.config.ts
/** @type {import('next').NextConfig} */
const nextConfig = {
  // ✅ Disable source maps in production
  productionBrowserSourceMaps: false,

  // ✅ Enable strict mode for development warnings
  reactStrictMode: true,

  // ✅ Enforce CSP headers
  headers: async () => {
    return [{
      source: '/(.*)',
      headers: [
        {
          key: 'Content-Security-Policy',
          value: "default-src 'self'; script-src 'self' 'unsafe-inline'; img-src * data:; font-src 'self'"
        }
      ]
    }];
  },

  // ✅ Security headers
  async redirects() {
    return [];
  },

  // ✅ Disable x-powered-by header
  poweredByHeader: false
};

module.exports = nextConfig;
```

---

## 4. Control 1: Authentication

**Objective:** Validate user identity at server level with SSR hydration security.

### Requirement

- Session validation on every server render
- Middleware intercepts unauthenticated requests
- Token refresh server-side only
- No JWT parsing on client for auth decisions

### Compliant Implementation

```typescript
// lib/auth.ts
import { jwtVerify } from 'jose';
import { cookies } from 'next/headers';

const secret = new TextEncoder().encode(process.env.JWT_SECRET!);

export async function verifyAuth() {
  const cookieStore = await cookies();
  const token = cookieStore.get('auth_token')?.value;

  if (!token) {
    return null;
  }

  try {
    const verified = await jwtVerify(token, secret);
    return verified.payload as any;
  } catch (err) {
    return null;
  }
}

// pages/dashboard.tsx
export const getServerSideProps = async (context) => {
  // ✅ Authenticate server-side before rendering
  const user = await verifyAuth();

  if (!user) {
    return {
      redirect: {
        destination: '/login',
        permanent: false
      }
    };
  }

  return {
    props: { user: { id: user.sub, tenantId: user.tenant_id } }
  };
};

export default function Dashboard({ user }) {
  return <div>Welcome {user.id}</div>;
}
```

### MFA Integration

```typescript
// pages/api/auth/login.ts
export default async function handler(req, res) {
  if (req.method !== "POST") {
    return res.status(405).end();
  }

  const { email, password } = req.body;

  // ✅ Validate credentials
  const user = await validateCredentials(email, password);

  if (!user) {
    return res.status(401).json({ error: "Invalid credentials" });
  }

  // ✅ Check MFA requirement
  if (user.mfaEnabled) {
    // Generate temporary token (short-lived, single-use)
    const mfaToken = jwt.sign(
      { sub: user.id, type: "mfa" },
      process.env.JWT_SECRET,
      { expiresIn: "5m" },
    );

    return res.status(200).json({
      mfaRequired: true,
      mfaToken,
    });
  }

  // ✅ Issue auth token (HTTP-only cookie)
  const authToken = jwt.sign(
    { sub: user.id, tenant_id: user.tenantId },
    process.env.JWT_SECRET,
    { expiresIn: "1h" },
  );

  res.setHeader(
    "Set-Cookie",
    `auth_token=${authToken}; HttpOnly; Secure; SameSite=Strict; Path=/`,
  );

  return res.json({ success: true });
}
```

---

## 5. Control 2: Authorization

**Objective:** Server-side authorization checks with row-level security.

### Requirement

- Tenant context obtained from authenticated session
- Row-level security filters in database queries
- No authorization delegation to client

### Compliant Implementation

```typescript
// lib/db.ts (Prisma example)
import { PrismaClient } from "@prisma/client";

const prisma = new PrismaClient();

// ✅ Scoped query: tenant isolation built-in
export async function getInvoices(userId: string, tenantId: string) {
  return prisma.invoices.findMany({
    where: {
      userId,
      tenantId, // ← SERVER enforces tenant boundary
    },
  });
}

// pages/api/invoices.ts
export default async function handler(req, res) {
  const user = await verifyAuth(); // From session

  if (!user) return res.status(401).end();

  // ✅ Use server-validated tenant ID
  const invoices = await getInvoices(user.sub, user.tenant_id);

  res.json(invoices);
}

// pages/dashboard/invoices.tsx
export const getServerSideProps = async (context) => {
  const user = await verifyAuth(); // Server-side auth
  const invoices = await getInvoices(
    user.sub,
    user.tenant_id, // Never from URL/client
  );

  return { props: { invoices } };
};
```

---

## 6. Control 3: Versioning

**Objective:** API route versioning for backward compatibility.

### Requirement

- Versioned API endpoints (`/api/v1/`, `/api/v2/`)
- Client detects version mismatch
- Graceful deprecation handling

### Compliant Implementation

```typescript
// pages/api/v1/invoices.ts (deprecated)
export default async function handler(req, res) {
  const user = await verifyAuth();

  // ✅ Version header in response
  res.setHeader("X-API-Version", "v1");
  res.setHeader("Deprecation", "true");
  res.setHeader("Sunset", "Fri, 01 Dec 2026 23:59:59 GMT");

  // Handle v1 logic
  const invoices = await getInvoices(user.sub, user.tenant_id);
  res.json(invoices);
}

// pages/api/v2/invoices.ts (current)
export default async function handler(req, res) {
  const user = await verifyAuth();

  res.setHeader("X-API-Version", "v2");

  // New v2 response format
  const invoices = await getInvoices(user.sub, user.tenant_id);
  res.json({
    data: invoices,
    meta: { total: invoices.length },
  });
}

// lib/api-routes.ts (client-side)
const API_VERSION = "v2";

export const api = {
  async getInvoices(token) {
    const response = await fetch(`/api/${API_VERSION}/invoices`, {
      headers: { Authorization: `Bearer ${token}` },
    });

    if (response.headers.get("Deprecation") === "true") {
      console.warn("API version deprecated");
    }

    return response.json();
  },
};
```

---

## 7. Control 4: Input Validation

**Objective:** Validate at both server (API routes) and client layers.

### Requirement

- Server-side validation mandatory on all API routes
- Client-side validation for UX
- Schema coercion and sanitization

### Compliant Implementation

```typescript
// lib/schemas.ts
import { z } from 'zod';

export const CreateInvoiceSchema = z.object({
  customerId: z.string().min(1),
  amount: z.number().positive().max(999999.99),
  currency: z.enum(['USD', 'EUR', 'GBP']),
  items: z.array(z.object({
    description: z.string().min(1).max(500),
    quantity: z.number().min(1).int(),
    unitPrice: z.number().positive()
  })).min(1)
});

// pages/api/invoices.ts (server)
export default async function handler(req, res) {
  if (req.method !== 'POST') return res.status(405).end();

  const user = await verifyAuth();

  try {
    // ✅ Parse and validate request body
    const validated = CreateInvoiceSchema.parse(req.body);

    // ✅ Add server-controlled fields
    const invoice = await createInvoice({
      ...validated,
      userId: user.sub,
      tenantId: user.tenant_id
    });

    res.status(201).json(invoice);
  } catch (error) {
    if (error instanceof z.ZodError) {
      return res.status(422).json({ errors: error.errors });
    }
    throw error;
  }
}

// components/InvoiceForm.tsx (client)
export function InvoiceForm() {
  const form = useForm({
    resolver: zodResolver(CreateInvoiceSchema)
  });

  const onSubmit = async (data) => {
    try {
      const response = await fetch('/api/invoices', {
        method: 'POST',
        body: JSON.stringify(data)
      });

      if (!response.ok) {
        const errors = await response.json();
        form.setError('root', { message: errors.message });
      }
    } catch (error) {
      console.error(error);
    }
  };

  return <form onSubmit={form.handleSubmit(onSubmit)}>...</form>;
}
```

---

## 8. Control 5: Rate Limiting

**Objective:** Protect API routes from abuse.

### Requirement

- Rate limit middleware on API routes
- Client-side debouncing for UX
- Proper 429 response handling

### Compliant Implementation

```typescript
// middleware.ts
import { rateLimit } from "@/lib/rate-limit";

const limiter = rateLimit({
  interval: "1m",
  uniqueTokenPerInterval: 500,
});

export async function middleware(request: NextRequest) {
  if (request.nextUrl.pathname.startsWith("/api/")) {
    try {
      await limiter.check(request, 100); // 100 requests per minute
    } catch (error) {
      return new NextResponse("Too many requests", {
        status: 429,
        headers: { "Retry-After": "60" },
      });
    }
  }

  return NextResponse.next();
}

// lib/rate-limit.ts
export function rateLimit(config) {
  return {
    async check(request, limit) {
      const ip = request.ip || "unknown";
      const key = `${ip}:${request.nextUrl.pathname}`;

      const count = await redis.incr(key);

      if (count === 1) {
        await redis.expire(key, 60);
      }

      if (count > limit) {
        throw new Error("Rate limit exceeded");
      }
    },
  };
}

// Client-side debouncing
import { debounce } from "lodash-es";

export const debouncedFetch = debounce(async (query) => {
  const response = await fetch(`/api/search?q=${query}`);
  return response.json();
}, 300);
```

---

## 9. Control 6: Testing & Documentation

**Objective:** Ensure API routes and SSR pages have adequate test coverage.

### Requirement

- Unit tests > 80% coverage
- Integration tests for API routes
- E2E tests for auth flows

### Compliant Implementation

```typescript
// __tests__/pages/api/invoices.test.ts
import { createMocks } from 'node-mocks-http';
import handler from '@/pages/api/invoices';
import * as auth from '@/lib/auth';

vi.mock('@/lib/auth');

describe('/api/invoices', () => {
  it('returns 401 for unauthenticated request', async () => {
    vi.mocked(auth.verifyAuth).mockResolvedValue(null);

    const { req, res } = createMocks({ method: 'GET' });
    await handler(req, res);

    expect(res._getStatusCode()).toBe(401);
  });

  it('creates invoice with valid input', async () => {
    vi.mocked(auth.verifyAuth).mockResolvedValue({
      sub: 'user-123',
      tenant_id: 'tenant-abc'
    });

    const { req, res } = createMocks({
      method: 'POST',
      body: {
        customerId: 'cust-456',
        amount: 1000,
        currency: 'USD',
        items: [{ description: 'Item', quantity: 1, unitPrice: 100 }]
      }
    });

    await handler(req, res);

    expect(res._getStatusCode()).toBe(201);
    expect(res._getJSONData().id).toBeDefined();
  });

  it('rejects invalid input', async () => {
    const { req, res } = createMocks({
      method: 'POST',
      body: { amount: -100 } // Invalid
    });

    await handler(req, res);

    expect(res._getStatusCode()).toBe(422);
  });
});

// __tests__/pages/dashboard.test.tsx
import { render } from '@testing-library/react';
import Dashboard, { getServerSideProps } from '@/pages/dashboard';

describe('Dashboard page', () => {
  it('renders with authenticated user', () => {
    const result = render(<Dashboard user={{ id: 'user-123', tenantId: 'tenant-abc' }} />);
    expect(result.getByText(/Welcome/)).toBeInTheDocument();
  });
});

describe('getServerSideProps', () => {
  it('redirects when unauthenticated', async () => {
    vi.mocked(auth.verifyAuth).mockResolvedValue(null);

    const result = await getServerSideProps({});

    expect(result).toEqual({
      redirect: {
        destination: '/login',
        permanent: false
      }
    });
  });
});
```

---

## 10. Control 7: Logging & Observability

**Objective:** Capture API route execution and errors with correlation IDs.

### Requirement

- Structured logging on API routes
- Correlation ID propagation SS R → API
- Error tracking with context

### Compliant Implementation

```typescript
// lib/logger.ts
import pino from "pino";

const logger = pino({
  level: process.env.LOG_LEVEL || "info",
  transport:
    process.env.NODE_ENV === "production"
      ? undefined
      : {
          target: "pino-pretty",
        },
});

export function createLogger(component: string, correlationId?: string) {
  return logger.child({ component, correlationId });
}

// middleware.ts
export async function middleware(request: NextRequest) {
  const correlationId =
    request.headers.get("x-correlation-id") || crypto.randomUUID();

  const requestHeaders = new Headers(request.headers);
  requestHeaders.set("x-correlation-id", correlationId);

  return NextResponse.next({
    request: { headers: requestHeaders },
  });
}

// pages/api/invoices.ts
import { headers } from "next/headers";
import { createLogger } from "@/lib/logger";

export default async function handler(req, res) {
  const headersList = await headers();
  const correlationId = headersList.get("x-correlation-id");
  const logger = createLogger("api/invoices", correlationId);

  try {
    logger.info({ method: req.method, path: req.url }, "API request");

    const user = await verifyAuth();

    if (!user) {
      logger.warn({ correlationId }, "Unauthorized request");
      return res.status(401).end();
    }

    const invoices = await getInvoices(user.sub, user.tenant_id);
    logger.info({ count: invoices.length }, "Invoices retrieved");

    res.json(invoices);
  } catch (error) {
    logger.error(
      { error: error instanceof Error ? error.message : error },
      "API error",
    );
    res.status(500).end();
  }
}
```

---

## 11. Control 8: Zero Trust Networking

**Objective:** Enforce HTTPS, secure cookies, and CSP across full-stack app.

### Requirement

- HTTPS only (HTTP redirect)
- Secure cookie flags enforced
- CSP headers for both SSR and client

### Compliant Implementation

```typescript
// next.config.js
/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  productionBrowserSourceMaps: false,

  async headers() {
    return [
      {
        source: '/:path*',
        headers: [
          {
            key: 'Strict-Transport-Security',
            value: 'max-age=31536000; includeSubDomains; preload'
          },
          {
            key: 'Content-Security-Policy',
            value: "default-src 'self'; script-src 'self' 'unsafe-inline'; img-src * data:; font-src 'self'"
          },
          {
            key: 'X-Frame-Options',
            value: 'DENY'
          },
          {
            key: 'X-Content-Type-Options',
            value: 'nosniff'
          }
        ]
      }
    ];
  },

  async redirects() {
    return [
      // ✅ Redirect HTTP to HTTPS
      ...(process.env.ENFORCE_HTTPS === 'true' ? [{
        source: '/:path*',
        destination: 'https://:host/:path*',
        permanent: true
      }] : [])
    ];
  }
};

module.exports = nextConfig;

// middleware.ts (cookie security)
export async function middleware(request: NextRequest) {
  // ✅ Verify HTTPS in production
  if (process.env.NODE_ENV === 'production') {
    const protocol = request.headers.get('x-forwarded-proto');
    if (protocol !== 'https') {
      return NextResponse.redirect(`https://${request.headers.get('host')}${request.nextUrl.pathname}`);
    }
  }

  return NextResponse.next();
}

// pages/api/auth.ts (secure cookies)
export default async function handler(req, res) {
  // ... auth logic ...

  const token = jwt.sign({ ... }, process.env.JWT_SECRET);

  // ✅ MANDATORY flags: HttpOnly, Secure, SameSite
  res.setHeader('Set-Cookie',
    `auth_token=${token}; HttpOnly; Secure; SameSite=Strict; Path=/; Max-Age=3600`
  );

  res.json({ success: true });
}
```

---

## 12. Multi-Tenancy Controls

**Objective:** Enforce tenant isolation at both server (API) and client levels.

### Requirement

- Tenant ID from authenticated session only
- All queries filtered by tenant
- No tenant ID derivable from URL

### Compliant Implementation

```typescript
// middleware.ts
import { verifyAuth } from "@/lib/auth";

export async function middleware(request: NextRequest) {
  const user = await verifyAuth();

  if (user) {
    const requestHeaders = new Headers(request.headers);
    requestHeaders.set("x-tenant-id", user.tenant_id);
    requestHeaders.set("x-user-id", user.sub);

    return NextResponse.next({
      request: { headers: requestHeaders },
    });
  }

  return NextResponse.next();
}

// pages/api/invoices.ts
import { headers } from "next/headers";

export default async function handler(req, res) {
  const headersList = await headers();
  const tenantId = headersList.get("x-tenant-id");
  const userId = headersList.get("x-user-id");

  // ✅ Query enforces tenant boundary
  const invoices = await prisma.invoices.findMany({
    where: {
      tenantId, // ← SERVER enforces
      userId,
    },
  });

  res.json(invoices);
}

// pages/dashboard.tsx (SSR)
export const getServerSideProps = async (context) => {
  const user = await verifyAuth();

  const invoices = await prisma.invoices.findMany({
    where: {
      tenantId: user.tenant_id, // ← Never from URL
      userId: user.sub,
    },
  });

  return {
    props: {
      invoices,
      tenantId: user.tenant_id,
    },
  };
};
```

---

## 13. Dependency & Supply Chain Governance

**Objective:** Same as React with SSR-specific checks.

### Requirement

- npm audit passes (high/critical)
- All dependencies pinned
- Build-time verification

### Compliant Implementation

```json
{
  "scripts": {
    "audit": "npm audit --audit-level=high && npx license-checker --summary",
    "build": "next build",
    "verify": "npm audit && npx eslint . && npm run test"
  }
}
```

```yaml
# .github/workflows/ci.yml
- name: Audit dependencies
  run: npm ci && npm audit --audit-level=high

- name: Verify no secrets in build
  run: |
    npm run build
    ! grep -r "sk_live_\|password\|secret" .next/
```

---

## 14. Control Mapping

| EATGF Control    | ISO 27001:2022 | NIST SSDF 1.1 | OWASP ASVS 5.0 | COBIT 2019 |
| ---------------- | -------------- | ------------- | -------------- | ---------- |
| Authentication   | A.8.2, A.8.3   | PW.2.1        | V2             | DSS05.02   |
| Authorization    | A.8.5, A.8.9   | PW.2.2        | V4             | DSS05.03   |
| Versioning       | A.8.28         | PW.4.2        | V14            | BAI09.02   |
| Input Validation | A.8.22, A.8.28 | PW.8.1        | V5             | DSS05.04   |
| Rate Limiting    | A.8.22         | PW.8.2        | V11            | DSS01.05   |
| Testing          | A.8.28         | PW.9.1        | V14            | BAI03.07   |
| Logging          | A.8.15, A.8.23 | RV.1.1        | V15            | MEA01.02   |
| Zero Trust       | A.8.1, A.8.9   | PW.1.1        | V1             | DSS05.01   |

---

## 15. Developer Checklist

- [ ] Middleware enforces authentication on protected routes
- [ ] API routes validate input with Zod/similar schema
- [ ] No `process.env.SECRET_*` passed to `props` in getServerSideProps
- [ ] Hydration deterministic (no random rendering)
- [ ] Server components use 'use server' for sensitive operations
- [ ] Cookies set with HttpOnly, Secure, SameSite flags
- [ ] Environment variables properly prefixed (NEXT*PUBLIC*\* for client)
- [ ] XSS prevention: user input sanitized before dangerouslySetInnerHTML
- [ ] CSP headers configured in next.config.ts
- [ ] Rate limiting middleware protecting API routes
- [ ] Correlation ID propagated from middleware to API routes
- [ ] Tenant ID derived from authenticated session only
- [ ] npm audit passes (high/critical)
- [ ] Source maps disabled in production build
- [ ] API routes return proper HTTP status codes (401, 403, 422, 429)

---

## Official References

- Next.js Documentation: https://nextjs.org/docs
- Next.js Security & Performance: https://nextjs.org/docs/advanced-features/security-headers
- OWASP Server-Side Security: https://owasp.org/www-community/attacks/
- Vercel Security: https://vercel.com/docs/security
- NIST SP 800-218: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-218.pdf

---

## 16. Governance Implications

**Risk if not implemented:**

- XSS via server-rendered content
- Token leakage to client bundle
- Hydration mismatch exploited for injection
- CSRF via missing SameSite cookies
- Supply chain compromise via unaudited dependencies

**SOC2/ISO 27001:** Same as React + API governance standards

---

## 17. Version Information

| Field                | Value                   |
| -------------------- | ----------------------- |
| **Document Version** | 1.0                     |
| **Change Type**      | Major (Initial Release) |
| **Issue Date**       | February 15, 2026       |
| **EATGF Baseline**   | v1.0 (Block 2 Complete) |
| **Next.js Version**  | 14.0+                   |
| **React Version**    | 18.2+                   |
| **Node.js**          | 18.0+ (LTS)             |

---

## Formal Closure Statement

**Next.js Frontend Governance Profile is now PUBLISHED.**

This profile completes enterprise frontend SaaS governance alongside React, Vue, Angular, Flutter, Svelte, React Native, and Astro profiles.

All Next.js applications operating in SaaS/enterprise environments MUST conform to this governance model.

**Status: PRODUCTION READY**

---

**Authorization:** Enterprise Architecture Board (EATGF Governance)
**Last Reviewed:** February 15, 2026
**Next Review:** August 15, 2026
