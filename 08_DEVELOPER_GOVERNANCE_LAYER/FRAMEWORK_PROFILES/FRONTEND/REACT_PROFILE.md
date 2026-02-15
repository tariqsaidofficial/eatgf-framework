# React Framework Governance Profile

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

**COMPLIANCE STATEMENT:** This profile enforces multi-layered client-side security for React applications. Non-conformance may result in:

- XSS-based token theft
- Cross-tenant data exposure
- Credential compromise from supply chain attacks
- SOC2/ISO 27001 audit failures

React applications are classified as **Client Attack Surface Layer** under EATGF and must assume the browser runtime is untrusted.

---

## 1. Purpose & Scope

This document defines governance conformance requirements for React-based frontend applications operating under the Enterprise AI-Aligned Technical Governance Framework (EATGF).

**Scope:** SaaS web applications, enterprise dashboards, customer portals, multi-tenant SPAs

**Non-Scope:** Server-side React rendering (covered under Node.js Profile), React Native mobile (separate profile)

---

## 2. Architectural Position

**EATGF Layer Placement:**

```
08_DEVELOPER_GOVERNANCE_LAYER
├── FRAMEWORK_PROFILES
│   ├── BACKEND (Django, FastAPI, Node.js, Spring Boot)
│   ├── FRONTEND (React, Next.js*, React Native)
│   └── INFRASTRUCTURE (Docker, K8s, Terraform)
```

**React operates as:**

- Browser-executed runtime
- API consumer (stateless)
- Token holder (ephemeral)
- UX rendering engine
- Client-side state manager
- Attack surface boundary

**React must conform to:**

- **01_SECURE_SDLC:** Development lifecycle security
- **02_API_GOVERNANCE:** API client contractual compliance
- **03_DEVSECOPS:** Build pipeline, supply chain verification
- **05_DOMAIN_FRAMEWORKS:** Domain-specific rules (if applicable)

**Critical Principle:** React is not a trust boundary. All security decisions must be made server-side. Frontend checks are UX enhancements only.

---

## 3. Governance Principles

### Principle 1: Zero-Trust Client Model (MANDATORY)

The browser is treated as an untrusted network edge. Client-side logic must never enforce:

- Authorization decisions
- Tenant isolation
- Data validation (beyond UX)
- Rate limiting
- Access control

**Enforcement:**

```typescript
// ❌ PROHIBITED: Trusting client-side tenant check
function RenderInvoices() {
  const { tenantId } = localStorage.getItem("tenant"); // VIOLATES zero-trust
  return <InvoiceList tenantId={tenantId} />;
}

// ✅ COMPLIANT: Server provides validated tenant
function RenderInvoices() {
  const { tenantId } = useUserContext(); // from authenticated /user endpoint
  return <InvoiceList tenantId={tenantId} />;
}
```

**Implication:** Backend must independently validate every request. Frontend UI cannot be security enforcement.

---

### Principle 2: Secure Token Handling (MANDATORY)

Access tokens must **NEVER** be stored persistently on client.

**Prohibited Storage:**

```typescript
// ❌ localStorage
localStorage.setItem("token", accessToken);

// ❌ sessionStorage
sessionStorage.setItem("token", accessToken);

// ❌ Redux store (persisted)
store.dispatch(setToken(accessToken));

// ❌ IndexedDB
db.tokens.add({ token: accessToken });

// ❌ plain JavaScript variable (survives refresh)
window.authToken = accessToken;
```

**Mandatory Model: HTTP-Only Secure Cookies**

```typescript
// ✅ Server sends HTTP-only cookie on login
// Response headers:
// Set-Cookie: access_token=<JWT>; HttpOnly; Secure; SameSite=Strict; Path=/api

// ✅ Frontend automatically includes cookie
fetch("/api/users", {
  method: "GET",
  credentials: "include", // sends HTTP-only cookies
});

// ✅ Short-lived access token + silent refresh
fetch("/api/auth/refresh", {
  method: "POST",
  credentials: "include",
}).then((res) => res.json());
// New token issued server-side in Set-Cookie header
```

**Advanced Pattern: Token Rotation on Every Request**

```typescript
// ✅ Backend rotates token on each API response
// Frontend automatically receives new token in Set-Cookie
// Old token invalidated immediately

// This prevents token replay and theft window
```

**Implication:** Tokens are opaque to frontend. Duration, refresh timing, rotation all server-controlled.

---

### Principle 3: XSS Mitigation Strategy (MANDATORY)

Rendering user input as HTML is prohibited without explicit sanitization.

```typescript
// ❌ CRITICAL VIOLATION
<div dangerouslySetInnerHTML={{ __html: userInput }} />

// ❌ Also dangerous
<div innerHTML={userInput} />

// ❌ Even with toString()
<p>{userInput.toString()}</p> // if userInput is <img src=x onerror=steal()>
```

**Mandatory Sanitization:**

```typescript
import DOMPurify from "dompurify";

// ✅ COMPLIANT: Sanitize before rendering
const sanitized = DOMPurify.sanitize(userInput);
<div dangerouslySetInnerHTML={{ __html: sanitized }} />;

// ✅ PREFERRED: Treat as text (no HTML)
<div>{userInput}</div>
```

**Configuration:**

```typescript
// ✅ Strict DOMPurify config
const config = {
  ALLOWED_TAGS: ["b", "i", "em", "strong"],
  ALLOWED_ATTR: [],
  KEEP_CONTENT: true,
};

const sanitized = DOMPurify.sanitize(userInput, config);
```

**Restriction:** dangerouslySetInnerHTML usage must be:

1. Documented in code comments
2. Justified by security team
3. Sanitization enforced
4. Audited quarterly

---

### Principle 4: Content Security Policy (MANDATORY)

Backend must enforce strict CSP headers. Frontend must align with CSP directives.

**Mandatory CSP Header:**

```http
Content-Security-Policy:
  default-src 'self';
  script-src 'self';
  style-src 'self' https://fonts.googleapis.com;
  font-src 'self' https://fonts.gstatic.com;
  img-src 'self' data: https:;
  connect-src 'self' https://api.example.com;
  frame-ancestors 'none';
  base-uri 'self';
  form-action 'self';
  upgrade-insecure-requests;
```

**Frontend Compliance:**

```typescript
// ❌ VIOLATES CSP: Inline script
<script>console.log("hello");</script>

// ❌ VIOLATES CSP: Inline style
<div style={{ color: "red" }}>Error</div>

// ✓ COMPLIANT: External stylesheet
<link rel="stylesheet" href="/styles.css" />

// ✓ COMPLIANT: CSS-in-JS with nonce (if supported)
// Backend provides nonce in CSP-Nonce header
<style nonce={cspNonce}>
  .error { color: red; }
</style>
```

**Implication:** React bundler must not inject inline styles or scripts. Build verification required.

---

### Principle 5: API Interaction Governance (MANDATORY)

All HTTP requests must use a centralized, configured API client. No scattered fetch() or axios() calls.

```typescript
// ❌ PROHIBITED: Scattered fetch calls
function UserProfile() {
  useEffect(() => {
    fetch("https://api.example.com/user")
      .then((res) => res.json())
      .then(setUser);
  }, []);
}

// ✓ COMPLIANT: Centralized client
import { api } from "@/lib/api-client";

function UserProfile() {
  const { data: user } = useQuery("user", () => api.get("/user"));
}
```

**Mandatory API Client Pattern:**

```typescript
// src/lib/api-client.ts (centralized)
import axios, { AxiosInstance } from "axios";
import { v4 as uuidv4 } from "uuid";

export const api: AxiosInstance = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL,
  withCredentials: true, // sends HTTP-only cookies
  timeout: 5000,
  headers: {
    "Content-Type": "application/json",
    Accept: "application/json",
  },
});

// ✅ Request interceptor: Add correlation ID
api.interceptors.request.use((config) => {
  config.headers["X-Correlation-ID"] = uuidv4();
  config.headers["X-Request-Timestamp"] = new Date().toISOString();
  return config;
});

// ✅ Response interceptor: Handle auth failures
api.interceptors.response.use(
  (response) => response,
  async (error) => {
    if (error.response?.status === 401) {
      // Server invalidated session, clear UI state
      sessionStorage.clear();
      window.location.href = "/login";
    }
    return Promise.reject(error);
  },
);

export default api;
```

**Implication:** Every API call includes correlation ID, automatic retry logic, centralized error handling.

---

### Principle 6: Dependency Governance (MANDATORY)

All dependencies must be locked, audited, and tracked.

```json
// ✅ package.json: Pinned versions
{
  "dependencies": {
    "react": "18.2.0",
    "react-dom": "18.2.0",
    "axios": "1.6.0",
    "dompurify": "3.0.6"
  },
  "devDependencies": {
    "vitest": "1.0.0",
    "eslint": "8.52.0"
  }
}
```

**Lockfile Enforcement:**

```bash
# ✅ MANDATORY: Commit lockfile
git add package-lock.json
git commit -m "deps: update packages"

# ✅ CI: Enforce lockfile consistency
npm ci --omit=dev

# ✅ CI: Audit for vulnerabilities
npm audit --audit-level=high
# Fails build on high/critical severity
```

**Advanced Supply Chain:**

```bash
# ✅ License compliance check
npx license-checker --summary

# ✅ SBOM generation
npm ls --json > sbom.json

# ✅ Dependency audit with known vulnerabilities
npx npm-check-updates --doctored
```

**Restricted Packages:** Organizations must maintain blocklist:

```javascript
// eslintplugin-no-unsanctioned-packages
"no-unsanctioned-packages/no-unsanctioned": [
  "error",
  {
    blocklist: [
      "eval-package", // dynamic code execution risk
      "unmaintained-http-server", // security history
      "crypto-js" // use native crypto instead
    ]
  }
]
```

---

### Principle 7: Environment Variable Governance (MANDATORY)

Frontend environment variables must **NEVER** contain secrets. Only public configuration.

```typescript
// ❌ CRITICAL VIOLATION: Secrets in frontend env
REACT_APP_STRIPE_SECRET_KEY=sk_live_... // EXPOSED in bundle
REACT_APP_DATABASE_PASSWORD=... // VIOLATES security boundary

// ✓ COMPLIANT: Public configuration only
VITE_API_URL=https://api.example.com
VITE_ENVIRONMENT=production
VITE_ANALYTICS_KEY=pk_prod_... // public analytics key
VITE_FEATURE_FLAGS_ENDPOINT=https://api.example.com/features
```

**Access Pattern:**

```typescript
// ✓ COMPLIANT: Import from centralized config
const config = {
  apiUrl: import.meta.env.VITE_API_URL,
  environment: import.meta.env.VITE_ENVIRONMENT,
  analyticsKey: import.meta.env.VITE_ANALYTICS_KEY,
};

// ✗ PROHIBITED: Direct env variable in component
const secret = process.env.REACT_APP_TOKEN; // VIOLATES principle
```

**Build-Time Verification:**

```bash
# ✅ CI script: Verify no secrets in build
grep -r "sk_live" dist/ && exit 1
grep -r "password" dist/ && exit 1
echo "✓ No hardcoded secrets in build artifact"
```

---

## 4. Control 1: Authentication

**Objective:** Establish and validate user identity in a zero-trust browser environment.

### Requirement

- Frontend must not make authentication decisions
- Server-side session validation mandatory on every request
- Token refresh must be automatic and server-controlled
- Multi-factor authentication (MFA) support required

### Compliant Implementation

```typescript
// src/hooks/useAuth.ts
import { useQuery } from "@tanstack/react-query";
import { api } from "@/lib/api-client";

export interface User {
  id: string;
  email: string;
  tenantId: string;
  roles: string[];
  mfaEnabled: boolean;
}

// ✅ COMPLIANT: Fetch user identity from server
export function useAuth() {
  const { data, isLoading, error } = useQuery({
    queryKey: ["auth", "user"],
    queryFn: async () => {
      const response = await api.get<User>("/auth/user");
      return response.data;
    },
    staleTime: 5 * 60 * 1000, // re-validate every 5 min
    retry: 1 // single retry on transient failure
  });

  return {
    user: data,
    isAuthenticated: !!data?.id,
    isLoading,
    error
  };
}

// ✅ Usage: Protect routes based on server response
function ProtectedRoute({ children }) {
  const { isAuthenticated, isLoading } = useAuth();

  if (isLoading) return <Spinner />;
  if (!isAuthenticated) return <Navigate to="/login" />;

  return children;
}
```

### Non-Compliant (Violation Examples)

```typescript
// ❌ VIOLATION: Trusting JWT decoded on client
import jwtDecode from "jwt-decode";

function useAuth() {
  const token = localStorage.getItem("token"); // Storage violation
  const decoded = jwtDecode(token); // Trusting client decode
  return { userId: decoded.sub }; // No server validation
}

// ❌ VIOLATION: Login stores token, assumes success
fetch("/auth/login", {
  method: "POST",
  body: JSON.stringify({ email, password }),
})
  .then((res) => res.json())
  .then((data) => {
    localStorage.setItem("token", data.token); // Storage violation
    setIsAuthenticated(true); // Trusting client state
  });
```

### MFA Support Pattern

```typescript
export function useAuthFlow() {
  const [step, setStep] = useState<"credentials" | "mfa" | "authenticated">(
    "credentials",
  );

  const submitCredentials = async (email: string, password: string) => {
    const response = await api.post("/auth/login", { email, password });

    if (response.data.mfaRequired) {
      setStep("mfa"); // Move to MFA challenge
    } else {
      setStep("authenticated"); // Server validated, cookies set
    }
  };

  const submitMFA = async (mfaCode: string) => {
    await api.post("/auth/mfa/verify", { mfaCode });
    setStep("authenticated"); // Server sets secure cookie
  };

  return { step, submitCredentials, submitMFA };
}
```

---

## 5. Control 2: Authorization

**Objective:** Verify user permissions for requested resources server-side. Frontend shows appropriate UI only.

### Requirement

- All authorization decisions made server-side
- Frontend must request permission from backend for operations
- Role-based access control (RBAC) enforced server-side
- Tenant isolation boundary must be validated server-side

### Compliant Implementation

```typescript
// src/hooks/useAuthorization.ts
import { api } from "@/lib/api-client";

export function useCanAccessResource(resourceId: string, action: "read" | "write" | "delete") {
  const { data: canAccess, isLoading } = useQuery({
    queryKey: ["auth", "authorize", resourceId, action],
    queryFn: async () => {
      const response = await api.get<{ authorized: boolean }>(
        `/auth/authorize`,
        { params: { resource: resourceId, action } }
      );
      return response.data.authorized;
    },
    // Re-verify every 10 minutes
    staleTime: 10 * 60 * 1000
  });

  return { canAccess: canAccess ?? false, isLoading };
}

// ✅ COMPLIANT: Frontend checks server auth, shows/hides UI
function InvoiceActions({ invoiceId }) {
  const { canAccess: canDelete, isLoading } = useCanAccessResource(invoiceId, "delete");

  if (isLoading) return <Spinner />;

  return (
    <>
      {canDelete && (
        <button onClick={() => deleteInvoice(invoiceId)}>
          Delete Invoice
        </button>
      )}
      {!canDelete && <span>No delete permission</span>}
    </>
  );
}

// ✅ Server-side verification happens ALSO on delete
async function deleteInvoice(invoiceId: string) {
  try {
    await api.delete(`/invoices/${invoiceId}`);
    // Server deleted only if authorization check passed internally
  } catch (error) {
    if (error.response?.status === 403) {
      // Permission denied: User did not have role/tenant match
      window.location.href = "/unauthorized";
    }
  }
}
```

### Non-Compliant (Violation Examples)

```typescript
// ❌ VIOLATION: Trust client-side role
const userRoles = ["admin"]; // hardcoded or localStorage
function DeleteButton() {
  return userRoles.includes("admin") ? <button>Delete</button> : null;
  // No server verification
}

// ❌ VIOLATION: Derive tenant from URL
function InvoiceList() {
  const { tenantId } = useParams(); // User can change URL param
  const invoices = fetchInvoices(tenantId); // Server trusts URL param
}

// ✗ RISK: Showing UI button doesn't mean action is permitted
// ✗ User can bypass by calling API directly with wrong tenantId
```

### Row-Level Security Pattern

```typescript
export function InvoiceEditor({ invoiceId }: { invoiceId: string }) {
  // ✅ MANDATORY: Server indicates if editing allowed
  const { data: invoice, error } = useQuery({
    queryKey: ["invoices", invoiceId],
    queryFn: () => api.get(`/invoices/${invoiceId}`)
      .then(res => res.data)
      .catch(err => {
        if (err.response?.status === 404) {
          throw new Error("Invoice not found or access denied");
        }
      })
  });

  if (error) {
    return <div>Access denied or not found</div>;
  }

  return (
    <form onSubmit={(data) => api.put(`/invoices/${invoiceId}`, data)}>
      {/* Server response contains only accessible fields */}
      <input value={invoice.amount} />
    </form>
  );
}
```

---

## 6. Control 3: Versioning

**Objective:** Manage API contract versioning and compatibility with server.

### Requirement

- API client must support versioned endpoints
- Breaking changes require client update
- Version mismatch must be detected and handled
- Deprecation warnings in console during development

### Compliant Implementation

```typescript
// src/lib/api-client.ts
const API_VERSION = "v2";
const MINIMUM_SUPPORTED_VERSION = "v1";

export const api = axios.create({
  baseURL: `${import.meta.env.VITE_API_URL}/${API_VERSION}`,
  withCredentials: true,
});

// ✅ Response interceptor: Detect version mismatch
api.interceptors.response.use(
  (response) => {
    const serverVersion = response.headers["x-api-version"];

    if (serverVersion && serverVersion !== API_VERSION) {
      if (import.meta.env.DEV) {
        console.warn(
          `⚠️ API version mismatch: client=${API_VERSION}, server=${serverVersion}`,
        );
      }
    }

    return response;
  },
  (error) => {
    if (error.response?.status === 410) {
      // HTTP 410 Gone: API version no longer supported
      alert("Your app version is outdated. Please refresh.");
      window.location.reload();
    }
    return Promise.reject(error);
  },
);

// ✅ Development mode: Warn on deprecations
if (import.meta.env.DEV) {
  api.interceptors.response.use((response) => {
    const deprecationWarning = response.headers["warning"];
    if (deprecationWarning?.includes("299")) {
      console.warn(`⚠️ Deprecated API: ${deprecationWarning}`);
    }
    return response;
  });
}
```

### Schema Versioning with Zod

```typescript
import { z } from "zod";

// ✅ Define schema per API version
const UserV1 = z.object({
  id: z.string(),
  email: z.string().email(),
  createdAt: z.string().datetime(),
});

const UserV2 = z.object({
  id: z.string(),
  email: z.string().email(),
  createdAt: z.string().datetime(),
  mfaEnabled: z.boolean(), // new in v2
  lastLogin: z.string().datetime().nullable(), // new in v2
});

// ✅ Request handler with schema validation
async function getUser(userId: string) {
  const response = await api.get(`/users/${userId}`);

  // ✅ Validate response matches expected schema
  const validated = UserV2.parse(response.data);
  return validated;
}
```

### Non-Compliant (Violation Examples)

```typescript
// ❌ VIOLATION: Hardcoded endpoint, no versioning
const response = await fetch(`/api/users`); // No version

// ❌ VIOLATION: Assuming response shape without validation
const user = response.data;
console.log(user.mfaEnabled); // Undefined if server is older version
```

---

## 7. Control 4: Input Validation

**Objective:** Validate all user input before sending to API (UX only). ServerMust re-validate.

### Requirement

- Client-side validation is UX only
- Server must independently validate all input
- Validation schema defined once, reused in schemas
- Trim, type-check, length enforcement

### Compliant Implementation

```typescript
// src/schemas/invoice.ts
import { z } from "zod";

// ✅ Share validation schema between frontend/backend
export const CreateInvoiceSchema = z.object({
  tenantId: z.string().uuid(), // from server, not user input
  customerId: z.string().min(1, "Customer required"),
  amount: z.number().positive("Amount must be positive").max(999999.99),
  currency: z.enum(["USD", "EUR", "GBP"]),
  dueDate: z.string().datetime().refine(
    (date) => new Date(date) > new Date(),
    "Due date must be in future"
  ),
  items: z.array(
    z.object({
      description: z.string().min(1).max(500),
      quantity: z.number().min(1).int(),
      unitPrice: z.number().positive()
    })
  ).min(1)
});

export type CreateInvoiceInput = z.infer<typeof CreateInvoiceSchema>;

// ✅ Form component with validation
function InvoiceForm() {
  const form = useForm<CreateInvoiceInput>({
    resolver: zodResolver(CreateInvoiceSchema),
    defaultValues: {
      currency: "USD"
    }
  });

  const onSubmit = async (data: CreateInvoiceInput) => {
    try {
      // ✅ Send to API (server re-validates)
      const response = await api.post("/invoices", data);
      navigate(`/invoices/${response.data.id}`);
    } catch (error) {
      if (error.response?.status === 422) {
        // Server validation failed
        form.setError("root", {
          message: error.response.data.message
        });
      }
    }
  };

  return (
    <form onSubmit={form.handleSubmit(onSubmit)}>
      <input {...form.register("amount")} />
      {form.formState.errors.amount && (
        <span>{form.formState.errors.amount.message}</span>
      )}
      <button type="submit" disabled={!form.formState.isValid}>
        Create Invoice
      </button>
    </form>
  );
}
```

### Non-Compliant (Violation Examples)

```typescript
// ❌ VIOLATION: No validation before send
function InvoiceForm() {
  const [amount, setAmount] = useState("");

  const handleSubmit = () => {
    fetch("/api/invoices", {
      method: "POST",
      body: JSON.stringify({ amount }) // No validation
    });
  };
}

// ❌ VIOLATION: Trusting client validation prevents API call
function SubmitButton({ isFormValid }) {
  return (
    <button disabled={!isFormValid}>Submit</button> // Disables button, but data could be sent another way
  );
}
```

---

## 8. Control 5: Rate Limiting

**Objective:** Prevent client from overwhelming API with requests (UX only). Server enforces hard limits.

### Requirement

- Client-side throttling/debouncing for UX
- Request queue management
- Exponential backoff on failures
- Server responds with 429 (Too Many Requests) on limit violation

### Compliant Implementation

```typescript
// src/lib/api-client.ts
import pRetry from "p-retry";

// ✅ Exponential backoff for retries
export const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
  withCredentials: true,
  timeout: 5000
});

api.interceptors.response.use(
  (response) => response,
  async (error) => {
    // ✅ Handle rate limit (429) with backoff
    if (error.response?.status === 429) {
      const retryAfter = parseInt(
        error.response.headers["retry-after"] || "60"
      );

      if (import.meta.env.DEV) {
        console.warn(`Rate limited. Retrying after ${retryAfter}s`);
      }

      // Wait server-specified duration
      await new Promise(resolve => setTimeout(resolve, retryAfter * 1000));

      // Retry original request once
      return api.request(error.config);
    }

    return Promise.reject(error);
  }
);

// ✅ Debounce search input (UX smoothing only)
import { debounce } from "lodash-es";

function SearchUsers({ onResults }) {
  const [query, setQuery] = useState("");

  const debouncedSearch = useMemo(
    () => debounce(async (q: string) => {
      try {
        const results = await api.get("/users/search", { params: { q } });
        onResults(results.data);
      } catch (error) {
        console.error("Search failed");
      }
    }, 300),
    []
  );

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setQuery(e.target.value);
    debouncedSearch(e.target.value);
  };

  return <input onChange={handleChange} />;
}

// ✅ Request queue to prevent duplicate API calls
function useFetchOnce<T>(
  url: string,
  options?: RequestInit
): { data: T | null; loading: boolean; error: Error | null } {
  const cache = useRef<Map<string, Promise<T>>>(new Map());

  const { data, isLoading, error } = useQuery({
    queryKey: [url, options],
    queryFn: async () => {
      if (!cache.current.has(url)) {
        cache.current.set(url, api.get<T>(url).then(res => res.data));
      }
      return cache.current.get(url)!;
    }
  });

  return { data: data ?? null, loading: isLoading, error };
}
```

### Non-Compliant (Violation Examples)

```typescript
// ❌ VIOLATION: No throttling on API calls
function SearchUsers() {
  const handleChange = (e) => {
    api.get("/users/search", { params: { q: e.target.value } }); // Called on every keystroke
  };

  return <input onChange={handleChange} />;
}

// ❌ VIOLATION: Ignoring 429 response
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 429) {
      // Silently fail, no retry
      return Promise.reject(error);
    }
  }
);
```

---

## 9. Control 6: Testing & Documentation

**Objective:** Ensure code quality, security, and maintainability through automated testing.

### Requirement

- Unit test coverage > 80%
- Integration tests for API contract
- Security-focused tests (XSS, CSRF, injection)
- API documentation via OpenAPI/Swagger

### Compliant Implementation

```typescript
// src/__tests__/hooks/useAuth.test.ts
import { renderHook, waitFor } from "@testing-library/react";
import { useAuth } from "@/hooks/useAuth";
import { api } from "@/lib/api-client";

vi.mock("@/lib/api-client");

describe("useAuth", () => {
  it("fetches user from authenticated endpoint", async () => {
    const mockUser = {
      id: "user-123",
      email: "user@example.com",
      tenantId: "tenant-abc",
      roles: ["user"],
    };

    vi.mocked(api.get).mockResolvedValue({ data: mockUser });

    const { result } = renderHook(() => useAuth());

    await waitFor(() => {
      expect(result.current.isAuthenticated).toBe(true);
    });

    expect(result.current.user).toEqual(mockUser);
  });

  it("clears auth state on 401 response", async () => {
    vi.mocked(api.get).mockRejectedValue({
      response: { status: 401 },
    });

    const { result } = renderHook(() => useAuth());

    await waitFor(() => {
      expect(result.current.isAuthenticated).toBe(false);
    });
  });
});

// ✅ Security test: Verify no XSS from user input
describe("Input Sanitization", () => {
  it("sanitizes HTML in user comments", () => {
    const maliciousInput = "<img src=x onerror=\"alert('XSS')\" />";
    const sanitized = DOMPurify.sanitize(maliciousInput);

    expect(sanitized).not.toContain("onerror");
  });

  it("prevents dangerouslySetInnerHTML without sanitization", () => {
    // ESLint rule catches violations
    // Test verifies the rule is enabled
    const configFile = readFileSync(".eslintrc.json", "utf-8");
    expect(configFile).toContain("no-danger-with-children");
  });
});

// ✅ Integration test: API contract validation
describe("API Client", () => {
  it("includes correlation ID on all requests", async () => {
    await api.get("/test");

    const lastRequest = vi.mocked(api.get).mock.results[0];
    expect(lastRequest[1]?.headers?.["X-Correlation-ID"]).toBeDefined();
  });

  it("enforces HTTP-only cookie transport", async () => {
    await api.get("/user");

    const config = vi.mocked(api.get).mock.calls[0][1];
    expect(config?.withCredentials).toBe(true);
  });
});
```

### API Documentation (OpenAPI)

```yaml
# API documentation (auto-generated or maintained)
openapi: 3.0.0
info:
  title: Invoice API
  version: v2

paths:
  /invoices:
    post:
      summary: Create invoice
      security:
        - BearerAuth: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/CreateInvoice"
      responses:
        "201":
          description: Invoice created
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Invoice"
        "422":
          description: Validation error
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ValidationError"

components:
  schemas:
    CreateInvoice:
      type: object
      required: [customerId, amount, currency, items]
      properties:
        customerId:
          type: string
        amount:
          type: number
          minimum: 0.01
          maximum: 999999.99
        currency:
          enum: [USD, EUR, GBP]
        items:
          type: array
          minItems: 1
```

### Non-Compliant (Violation Examples)

```typescript
// ❌ VIOLATION: No test coverage for security
function dangerousComponent({ html }) {
  return <div dangerouslySetInnerHTML={{ __html: html }} />;
  // No tests verifying sanitization
}

// ❌ VIOLATION: Missing integration tests
// API client modified, but no tests verify contract
export const api = axios.create({
  baseURL: "https://api.example.com" // No test with mock
});
```

---

## 10. Control 7: Logging & Observability

**Objective:** Capture security events and errors for audit and debugging without exposing sensitive data.

### Requirement

- Correlation ID on all API requests
- Structured logging (JSON format)
- No sensitive data in logs (tokens, passwords, PII)
- Error tracking with context
- User action audit trail (server-side)

### Compliant Implementation

```typescript
// src/lib/logger.ts
import pino from "pino";

// ✅ Browser-compatible structured logging
const logger = pino({
  level: import.meta.env.DEV ? "debug" : "info",
  browser: {
    asObject: true, // Output JSON, not formatted strings
  },
});

// ✅ Enrich logs with correlation ID
import { v4 as uuidv4 } from "uuid";

export const createLogger = (component: string) => {
  const correlationId = sessionStorage.getItem("correlation-id") || uuidv4();

  return {
    info: (message: string, data?: any) => {
      logger.info({
        timestamp: new Date().toISOString(),
        correlationId,
        component,
        message,
        ...data,
      });
    },
    error: (message: string, error?: Error, context?: any) => {
      logger.error({
        timestamp: new Date().toISOString(),
        correlationId,
        component,
        message,
        errorName: error?.name,
        errorMessage: error?.message,
        errorStack: error?.stack,
        ...context,
      });
    },
  };
};

// ✅ Usage in components
function InvoiceList() {
  const logger = createLogger("InvoiceList");

  useEffect(() => {
    api
      .get("/invoices")
      .then((response) => {
        logger.info("Invoices loaded", {
          count: response.data.length,
        });
      })
      .catch((error) => {
        logger.error("Failed to load invoices", error, {
          component: "InvoiceList",
          action: "fetch_invoices",
        });
        // ✅ Send to error tracking service
        sentry.captureException(error, {
          tags: {
            component: "InvoiceList",
            action: "fetch_invoices",
          },
        });
      });
  }, []);
}

// ✅ Redact sensitive data from logs
function sanitizeForLogging(data: any): any {
  const redacted = JSON.parse(JSON.stringify(data));

  const sensitiveKeys = ["token", "password", "secret", "apiKey", "creditCard"];
  const redactRecursive = (obj: any) => {
    Object.keys(obj).forEach((key) => {
      if (sensitiveKeys.some((k) => key.toLowerCase().includes(k))) {
        obj[key] = "[REDACTED]";
      } else if (typeof obj[key] === "object") {
        redactRecursive(obj[key]);
      }
    });
  };

  redactRecursive(redacted);
  return redacted;
}

// ✅ Log API calls with sanitization
api.interceptors.request.use((config) => {
  const sanitizedData = sanitizeForLogging(config.data);

  createLogger("api").info("API Request", {
    method: config.method?.toUpperCase(),
    url: config.url,
    data: sanitizedData,
  });

  return config;
});

// ✅ Error tracking (Sentry/similar)
import * as Sentry from "@sentry/react";

export function initErrorTracking() {
  Sentry.init({
    dsn: import.meta.env.VITE_SENTRY_DSN,
    environment: import.meta.env.VITE_ENVIRONMENT,
    tracesSampleRate: 0.1,
    beforeSend(event) {
      // ✅ Remove sensitive data before sending to tracking service
      if (event.request) {
        delete event.request.cookies;
        delete event.request.headers["authorization"];
      }
      return event;
    },
  });
}
```

### Non-Compliant (Violation Examples)

```typescript
// ❌ VIOLATION: Logging sensitive data
logger.info("User logged in", {
  email: user.email,
  password: user.password, // EXPOSED
  token: accessToken, // EXPOSED
});

// ❌ VIOLATION: No correlation ID
api.get("/invoices"); // No correlation tracking

// ❌ VIOLATION: Console.log in production
console.log("Debugging info:", sensitiveData);
```

---

## 11. Control 8: Zero Trust Networking

**Objective:** Assume network is untrusted. Enforce encryption and origin verification.

### Requirement

- HTTPS only (no HTTP fallback)
- Secure Cookie flags (HttpOnly, Secure, SameSite)
- CORS policy alignment with backend
- Fetch with credentials only to same-origin API
- CSP enforced for cross-origin resources

### Compliant Implementation

```typescript
// ✅ vite.config.ts: Enforce HTTPS in production
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],

  server: {
    // Development server must use HTTPS
    https: true,
    // Intercept origin validation
    middlewareMode: true,
  },

  // Production build excludes HTTP references
  build: {
    rollupOptions: {
      output: {
        // Ensure all imports use HTTPS
        assetFileNames: (assetInfo) => {
          return assetInfo.name;
        },
      },
    },
  },
});

// ✅ API client: HTTPS enforcement
export const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL,
  // Verify HTTPS
  httpAgent: new http.Agent({ protocol: "https:" }),
  httpsAgent: new https.Agent(),
  withCredentials: true, // Sends HTTP-only cookies
});

// ✅ Validate secure cookies from server
api.interceptors.response.use((response) => {
  const setCookie = response.headers["set-cookie"]?.[0] || "";

  // ✅ MANDATORY: Validate Secure, HttpOnly, SameSite flags
  if (setCookie.includes("token")) {
    if (!setCookie.includes("Secure")) {
      console.error("⚠️ Cookie missing Secure flag");
    }
    if (!setCookie.includes("HttpOnly")) {
      console.error("⚠️ Cookie missing HttpOnly flag");
    }
    if (!setCookie.includes("SameSite")) {
      console.error("⚠️ Cookie missing SameSite flag");
    }
  }

  return response;
});

// ✅ CORS enforcement: Only call same-origin API
async function fetchUserData() {
  // ✓ COMPLIANT: Same-origin (browser enforces CORS)
  return api.get("/api/user");

  // ✗ VIOLATES same-origin: Browser blocks unless CORS header
  // return fetch("https://different-domain.example.com/api/user");
}

// ✅ Subresource integrity for external libraries
// HTML: <script src="https://cdn.example.com/lib.js"
//        integrity="sha384-abc123..." />

// ✅ CSP headers (enforced by server)
// Content-Security-Policy:
//   default-src 'self';
//   connect-src 'self' https://api.example.com;
//   script-src 'self' https://cdn.example.com;
```

### Non-Compliant (Violation Examples)

```typescript
// ❌ VIOLATION: HTTP fallback
const api = axios.create({
  baseURL: "http://api.example.com", // No HTTPS
});

// ❌ VIOLATION: Cookies without flags
// Set-Cookie: token=abc123; Path=/
// Missing: Secure, HttpOnly, SameSite

// ❌ VIOLATION: Cross-origin without credentials control
fetch("https://another-domain.com/api/data", {
  credentials: "include", // Sends cookies to different origin
});

// ❌ VIOLATION: Hardcoded CDN without integrity
// <script src="https://cdn.example.com/library.js"></script>
// No integrity hash
```

---

## 12. Multi-Tenancy Controls

**Objective:** Ensure tenant isolation at client-side (UX only). Server enforces boundary.

### Requirement

- Tenant ID from authenticated server response only
- UI prevents tenant switching without re-authentication
- Requests include tenant context (for logging)
- No derived tenant ID from URL or localStorage

### Compliant Implementation

```typescript
// src/context/TenantContext.tsx
import { createContext, useContext } from "react";
import { api } from "@/lib/api-client";

interface TenantContext {
  tenantId: string;
  tenantName: string;
}

const TenantCtx = createContext<TenantContext | null>(null);

// ✅ Provide tenant from authenticated user endpoint
export function TenantProvider({ children }: { children: React.ReactNode }) {
  const { data: user } = useQuery({
    queryKey: ["auth", "user"],
    queryFn: () => api.get("/auth/user")
  });

  if (!user?.tenantId) {
    return <div>Loading tenant context...</div>;
  }

  return (
    <TenantCtx.Provider value={{
      tenantId: user.tenantId, // from server only
      tenantName: user.tenantName
    }}>
      {children}
    </TenantCtx.Provider>
  );
}

export function useTenant() {
  const ctx = useContext(TenantCtx);
  if (!ctx) throw new Error("useTenant must be within TenantProvider");
  return ctx;
}

// ✅ Usage: Tenant ID in requests
async function fetchInvoices() {
  const { tenantId } = useTenant();

  const response = await api.get("/invoices", {
    params: { tenantId } // Server validates tenantId matches request user
  });

  return response.data;
}

// ✅ UI cannot switch tenant without logout
function TenantSwitcher() {
  const { tenantId, tenantName } = useTenant();

  return (
    <div>
      <p>Current Tenant: {tenantName}</p>
      <button onClick={() => {
        api.post("/auth/logout").then(() => {
          window.location.href = "/login"; // Redirect to login
        });
      }}>
        Switch Tenant
      </button>
    </div>
  );
}
```

### Non-Compliant (Violation Examples)

```typescript
// ❌ VIOLATION: Derive tenant from URL
function InvoiceList() {
  const { tenantId } = useParams(); // User can change URL
  const invoices = api.get(`/invoices?tenantId=${tenantId}`);
  // Server trusts URL param
}

// ❌ VIOLATION: Store tenant in localStorage
localStorage.setItem("tenantId", tenantId);
const { tenantId } = JSON.parse(localStorage.getItem("user-context"));
// User can modify value

// ❌ VIOLATION: Allow tenant switch without re-auth
const switchTenant = (newTenantId) => {
  setTenant(newTenantId); // No logout, just change in-memory
};
```

---

## 13. Dependency & Supply Chain Governance

**Objective:** Maintain integrity of dependencies from ecosystem.

### Requirement

- Lockfile committed and verified
- Audit for known vulnerabilities automated
- License compliance tracking
- Deprecated package detection
- Build fails on violations

### Compliant Implementation

```json
// package.json with pinned, audited versions
{
  "name": "invoice-app",
  "version": "1.0.0",
  "engines": {
    "node": ">=18.0.0",
    "npm": ">=9.0.0"
  },
  "dependencies": {
    "react": "18.2.0",
    "react-dom": "18.2.0",
    "react-router-dom": "6.18.0",
    "axios": "1.6.0",
    "dompurify": "3.0.6",
    "pino": "8.16.2",
    "@tanstack/react-query": "5.25.0",
    "zod": "3.22.4"
  },
  "devDependencies": {
    "vitest": "1.0.0",
    "eslint": "8.52.0",
    "@typescript-eslint/eslint-plugin": "6.10.0",
    "prettier": "3.0.3"
  },
  "scripts": {
    "audit": "npm audit --audit-level=high && npx license-checker --summary",
    "build": "GENERATE_SOURCEMAP=false vite build",
    "test": "vitest"
  }
}
```

### CI/CD Supply Chain Verification

```yaml
# .github/workflows/build.yml
name: Build & Security

on: [push, pull_request]

jobs:
  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      # ✅ NPM audit
      - name: Audit dependencies
        run: npm ci --omit=dev && npm audit --audit-level=high

      # ✅ License compliance
      - name: Check licenses
        run: npx license-checker --summary --onlyAllow "Apache-2.0,MIT,ISC,BSD-2-Clause,BSD-3-Clause"

      # ✅ SBOM generation
      - name: Generate SBOM
        run: npm ls --json > sbom.json

      # ✅ Build verification
      - name: Build verification
        run: npm run build

      # ✅ No hardcoded secrets
      - name: Secrets check
        run: |
          ! grep -r "sk_live_" dist/
          ! grep -r "password" dist/
          ! grep -r "secret" dist/

      # ✅ Dependency deprecation check
      - name: Check for deprecated packages
        run: npx npm-check-updates --doctor

      # ✅ ESLint security rules
      - name: Lint
        run: npx eslint src --max-warnings=0

      # ✅ Test coverage
      - name: Test coverage
        run: |
          vitest run --coverage
          npx nyc check-coverage --lines 80 --functions 80
```

### Non-Compliant (Violation Examples)

```json
// ❌ VIOLATION: Unpinned versions
{
  "dependencies": {
    "react": "^18.2.0", // Caret version
    "axios": "*" // Wildcard
  }
}

// ❌ VIOLATION: No lockfile committed
// package-lock.json not in git
```

---

## 14. Control Mapping

**Explicit alignment with governance frameworks:**

| EATGF Control                       | ISO 27001:2022 | NIST SSDF 1.1 | OWASP ASVS 5.0      | COBIT 2019 |
| ----------------------------------- | -------------- | ------------- | ------------------- | ---------- |
| Authentication (Control 1)          | A.8.2, A.8.3   | PW.2.1        | V2 (Authentication) | DSS05.02   |
| Authorization (Control 2)           | A.8.5, A.8.9   | PW.2.2        | V4 (Access Control) | DSS05.03   |
| Versioning (Control 3)              | A.8.28         | PW.4.2        | V14 (SCM)           | BAI09.02   |
| Input Validation (Control 4)        | A.8.22, A.8.28 | PW.8.1        | V5 (XSS, Injection) | DSS05.04   |
| Rate Limiting (Control 5)           | A.8.22         | PW.8.2        | V11 (API)           | DSS01.05   |
| Testing & Documentation (Control 6) | A.8.28         | PW.9.1        | V14 (Automation)    | BAI03.07   |
| Logging & Observability (Control 7) | A.8.15, A.8.23 | RV.1.1        | V15 (Audit)         | MEA01.02   |
| Zero Trust Networking (Control 8)   | A.8.1, A.8.9   | PW.1.1        | V1 (HTTPS)          | DSS05.01   |

---

## 15. Developer Checklist

Before deploying React application to production:

- [ ] **Authentication:** User identity fetched from `/auth/user` endpoint, no JWT stored in localStorage
- [ ] **Authorization:** All access control decisions delegated to backend, frontend shows/hides UI only
- [ ] **Versioning:** API client supports versioned endpoints, version mismatch handled gracefully
- [ ] **Input Validation:** Zod/Yup schema used for form validation, server re-validates all input
- [ ] **Rate Limiting:** Debouncing/throttling implemented, 429 responses handled with exponential backoff
- [ ] **Testing:** Unit tests > 80% coverage, security tests for XSS/CSRF included
- [ ] **Logging:** Correlation ID on all API requests, structured logging enabled, sensitive data redacted
- [ ] **Zero Trust:** HTTPS only, secure cookies enforced (HttpOnly, Secure, SameSite), CORS validated
- [ ] **Dependency Audit:** `npm audit --audit-level=high` passes, lockfile committed
- [ ] **Secrets:** No hardcoded tokens/passwords, env vars prefixed (VITE*/REACT_APP*)
- [ ] **Sanitization:** DOMPurify used for user-generated HTML, dangerouslySetInnerHTML justified
- [ ] **CSP:** Content-Security-Policy header enforced server-side, inline scripts removed
- [ ] **Build:** Source maps disabled (`GENERATE_SOURCEMAP=false`), minification enabled
- [ ] **Error Tracking:** Sentry/similar integrated, sensitive data redacted before sending
- [ ] **Multi-Tenancy:** Tenant ID from server response only, no URL/localStorage derivation
- [ ] **Documentation:** API client methods documented, security patterns explained in code comments

---

## 16. Governance Implications

**Risk if not implemented:**

- **XSS Token Theft:** Unprotected tokens in localStorage → attacker steals session
- **Cross-Tenant Data Leak:** Missing server-side authorization → users query other tenant data
- **Supply Chain Compromise:** Unpinned dependencies → malicious package version installed
- **CSRF Bypass:** Missing SameSite cookie flag → attacker-initiated requests succeed
- **Secrets Exposure:** Hardcoded keys in source → credentials committed to git, leaked in bundle
- **Audit Trail Loss:** No correlation ID → impossible to trace user actions across logs

**SOC2/ISO 27001 Impact:**

- **SOC2 CC7.2:** (Change Management) Unaudited dependencies violate SCM control
- **ISO 27001 A.8.28:** (Vulnerability Management) npm audit failures indicate non-conformance
- **ISO 27001 A.8.15:** (Access Control) Missing server-side authorization checks
- **NIST SP 800-218 PW.2:** (Authentication & Authorization) Frontend trusting its own decisions

**Operational Impact:**

- Frontend compromise → backend compromise (entry point for lateral movement)
- Token theft → session hijacking, account takeover
- Missing audit trail → SOC investigations fail, incident response hampered

---

## 17. Implementation Risks

| Risk                                     | Severity | Mitigation                               |
| ---------------------------------------- | -------- | ---------------------------------------- |
| Tokens leaked from localStorage          | CRITICAL | Use HTTP-only secure cookies only        |
| XSS bypasses via dangerouslySetInnerHTML | CRITICAL | Mandatory DOMPurify + code review        |
| Trusting client-side authorization       | CRITICAL | Server re-validates every request        |
| Missing dependency audit                 | HIGH     | Automated npm audit in CI/CD             |
| Hardcoded secrets in build artifact      | HIGH     | Environment variable verification script |
| No correlation tracking                  | MEDIUM   | Automatic correlation ID injection       |
| Expired token sent to API                | MEDIUM   | Silent refresh with token rotation       |
| CSP bypassed via inline scripts          | MEDIUM   | Build tooling forbids inline injection   |

---

## 18. Official References

**Normative (Governance):**

- NIST SP 800-218: Secure Software Development Framework (SSDF)
- ISO/IEC 27001:2022 Annex A: Control Objectives and Controls
- NIST SP 800-53 Rev. 5: Security and Privacy Controls for Information Systems

**Informative (Frontend Security):**

- OWASP ASVS 5.0: Application Security Verification Standard
- OWASP Top 10 2021: Web Application Security Risks
- OWASP API Security Top 10 2023: API-Specific Risks
- RFC 6265: HTTP State Management Mechanism (Cookies)
- NIST SP 800-63B: Authentication Guidance
- COBIT 2019: Governance of Enterprise IT Framework

**Libraries & Standards:**

- Zod: TypeScript-first schema validation (<https://zod.dev>)
- DOMPurify: XSS sanitization (<https://github.com/cure53/DOMPurify>)
- Pino: Structured logging (<https://getpino.io>)
- TanStack React Query: Async state management (<https://tanstack.com/query>)

---

## 19. Version Information

| Field                | Value                                                    |
| -------------------- | -------------------------------------------------------- |
| **Document Version** | 1.0                                                      |
| **Change Type**      | Major (Initial Release)                                  |
| **Issue Date**       | February 15, 2026                                        |
| **EATGF Baseline**   | v1.0 (Foundation + Block 2 Complete)                     |
| **React Version**    | 18.2+                                                    |
| **Build Tool**       | Vite 5.0+ or Create React App 5.0+                       |
| **Node.js**          | 18.0+ (LTS recommended)                                  |
| **Target Audience**  | Frontend engineers, security architects, DevSecOps teams |

**Compliance Statement:** This profile is 100% conformant to EATGF_DOCUMENT_SIGNATURE_TEMPLATE.md and enforces all governance principles at Layer 08 level.

---

**Authorization:** Enterprise Architecture Board (EATGF Governance)
**Last Reviewed:** February 15, 2026
**Next Review:** August 15, 2026 (6-month cycle)
