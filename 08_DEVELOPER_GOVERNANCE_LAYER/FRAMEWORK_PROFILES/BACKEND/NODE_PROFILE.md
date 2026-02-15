# Node.js (Express/NestJS) Framework Governance Profile

> **Authority Notice:** This profile implements EATGF controls for Node.js backend systems built using Express or NestJS. It does NOT define new controls, redefine severity, or override standards. This profile clarifies HOW Node.js applications satisfy Secure SDLC (Layer 01), API Governance (Layer 05), and DevSecOps (Layer 03) requirements.

## Purpose

This document defines governance conformance requirements for Node.js backend systems built using Express or NestJS under the Enterprise AI-Aligned Technical Governance Framework (EATGF).

It establishes enforceable controls for:

- REST API security
- Middleware enforcement
- Authentication and authorization
- Multi-tenant isolation
- Dependency governance
- DevSecOps integration

This profile applies to:

- Enterprise SaaS backends
- Microservices architectures
- Public-facing REST APIs
- Internal service APIs
- Real-time event processing systems

## Architectural Position

**EATGF Layer:**

- Primary: `08_DEVELOPER_GOVERNANCE_LAYER` → `FRAMEWORK_PROFILES` → `BACKEND`
- References: Layer 01 (Secure SDLC), Layer 05 (API Governance), Layer 03 (DevSecOps)

**Scope:**
Node.js functions as:

- HTTP boundary enforcement layer
- Middleware execution chain
- Token validation layer
- Authorization enforcement surface
- Runtime request lifecycle controller

**Node.js Classification:**

- Middleware-driven enforcement framework
- TypeScript-capable (NestJS)
- Async callback-based (Express)
- Runtime container boundary
- Application security boundary

**Conformance Obligations:**

- ✅ 01_SECURE_SDLC standards
- ✅ 02_API_GOVERNANCE standards (REST-specific controls)
- ✅ 03_DEVSECOPS standards
- ✅ 04_CLOUD standards (if deployed in SaaS context)

## Relationship to EATGF Layers

### Layer 01: Secure SDLC

Node.js profiles enforce:

- **Dependency scanning:** `npm audit`, `yarn audit`, `snyk` in CI/CD
- **SAST rules:** ESLint with security plugins, `SonarQube`
- **Code review workflow:** PR-based with security checklist
- **Test coverage requirement:** Minimum 80% unit + integration test coverage

### Layer 03: DevSecOps Governance

Node.js profiles reference:

- **Container security:** Node.js Alpine/slim images, non-root user
- **CI/CD pipeline gates:** Pre-merge, pre-release, pre-production stages
- **Secrets management:** Environment variables from HashiCorp Vault or AWS Secrets Manager
- **Image scanning:** Trivy vulnerability scanning + SBOM generation

### Layer 05: Domain Frameworks

Node.js profiles implement API Governance controls:

- **Authentication:** JWT/OIDC via `@nestjs/jwt` or `passport.js`
- **Authorization:** Decorator-based or middleware-based guards
- **Rate Limiting:** `express-rate-limit` or NestJS throttle guards
- **OpenAPI/Swagger:** `@nestjs/swagger` for automatic schema generation
- **Versioning:** URL-based versioning (`/api/v1/`, `/api/v2/`)

### Layer 04: Cloud Governance (Conditional)

If deployed in cloud infrastructure:

- **HTTPS enforcement:** TLS termination at load balancer or via reverse proxy
- **Environment config:** CloudFormation/Terraform for Node.js instance configuration
- **Database encryption:** Database encryption at rest + TLS in transit
- **IAM scoping:** Service-specific IAM roles for Node.js application instances

## Governance Principles

### 1. Security Middleware First (Mandatory)

Security middleware must execute before any route logic.

```typescript
// Express
const helmet = require("helmet");
const rateLimit = require("express-rate-limit");

app.use(helmet()); // Security headers
app.use(
  rateLimit({
    windowMs: 15 * 60 * 1000,
    max: 100,
    standardHeaders: true,
    legacyHeaders: false,
  }),
);
app.use(express.json({ limit: "1mb" }));

// Routes added AFTER middleware
app.get("/api/v1/invoices", authMiddleware, getInvoices);

// NestJS
@Module({
  imports: [
    ThrottlerModule.forRoot([
      {
        ttl: 60000,
        limit: 10,
      },
    ]),
  ],
})
export class AppModule {}
```

**Constraint:** Routes must never execute before security middleware

### 2. Strict Body Parsing Limits

```typescript
// Express
app.use(express.json({ limit: "1mb" }));
app.use(express.urlencoded({ limit: "1mb", extended: false }));

// NestJS
app.use(new RawBodyMiddleware());
app.use(express.json({ limit: process.env.BODY_LIMIT || "1mb" }));
```

**Constraint:** Unbounded payload size classified as DoS risk

### 3. JWT / OIDC Authentication Enforcement

Session-based authentication is prohibited for API services.

```typescript
// NestJS
@Injectable()
export class JwtAuthGuard implements CanActivate {
  constructor(private jwtService: JwtService) {}

  async canActivate(context: ExecutionContext): Promise<boolean> {
    const request = context.switchToHttp().getRequest();
    const authHeader = request.headers.authorization;

    if (!authHeader) return false;

    const token = authHeader.split(" ")[1];

    try {
      const payload = await this.jwtService.verifyAsync(token, {
        secret: process.env.JWT_PUBLIC_KEY,
        audience: "https://api.example.com",
      });
      request.user = payload;
      return true;
    } catch (error) {
      return false;
    }
  }
}

// Express with Passport
const JwtStrategy = require("passport-jwt").Strategy;
passport.use(
  new JwtStrategy(
    {
      jwtFromRequest: ExtractJwt.fromAuthHeaderAsBearerToken(),
      secretOrKey: process.env.JWT_PUBLIC_KEY,
      audience: "https://api.example.com",
    },
    (payload, done) => {
      done(null, payload);
    },
  ),
);
```

**Token must include:**

- `exp` (expiration timestamp)
- `sub` (subject/user ID)
- `tenant_id` (tenant scope)
- `aud` (audience: API identifier)
- `iat` (issued at)

### 4. Role-Based Authorization (Decorator or Middleware)

```typescript
// NestJS Decorator approach
@UseGuards(JwtAuthGuard)
@SetMetadata("roles", ["tenant:read", "invoice:read"])
@Get()
async findAll(@Req() req: Request) {
  return this.service.findByTenant(req.user.tenant_id);
}

// Express middleware approach
const authorize = (role: string) => (req, res, next) => {
  if (!req.user.roles.includes(role)) {
    return res.status(403).json({ error: "Forbidden" });
  }
  next();
};

app.get("/invoices", authMiddleware, authorize("invoice:read"), getInvoices);
```

**Constraint:** Authorization must be explicit per route; implicit authorization is non-compliant

### 5. Tenant Isolation Enforcement

All database queries must be tenant-scoped.

```typescript
// NestJS with MongoDB
async findByTenant(tenantId: string) {
  return this.invoiceModel.find({ tenant_id: tenantId });
}

// Express with SQL
async function getInvoices(req, res) {
  const { tenant_id } = req.user;
  const invoices = await db.query(
    "SELECT * FROM invoices WHERE tenant_id = ?",
    [tenant_id]
  );
  res.json(invoices);
}
```

**Constraint:** Global queries without tenant filter are critical violation

### 6. Secrets Isolation

Secrets must originate from managed secret store, never hardcoded.

```typescript
// Correct: Environment sourced
const dbUrl = process.env.DATABASE_URL;
const jwtSecret = process.env.JWT_PUBLIC_KEY;
const apiKey = process.env.THIRD_PARTY_API_KEY;

// Vault integration (recommended)
import * as vault from "@hashicorp/vault-client";

const client = new vault.Client({ endpoint: process.env.VAULT_ADDR });
const secret = await client.secrets.kv2.read("secret/data/api-keys");
```

**Constraint:** Hardcoded credentials are MANDATORY violation

### 7. Structured JSON Logging

```typescript
import * as winston from "winston";

const logger = winston.createLogger({
  format: winston.format.combine(
    winston.format.timestamp({ format: "YYYY-MM-DD HH:mm:ss" }),
    winston.format.json(),
  ),
  transports: [
    new winston.transports.Console(),
    new winston.transports.File({ filename: "combined.log" }),
  ],
});

// Middleware for request logging
app.use((req, res, next) => {
  const correlationId = req.headers["x-correlation-id"] || generateId();
  logger.info({
    correlation_id: correlationId,
    tenant_id: req.user?.tenant_id,
    method: req.method,
    path: req.path,
    status_code: res.statusCode,
    latency_ms: Date.now() - req.startTime,
  });
  next();
});
```

**Logs must include:**

- `correlation_id` (request tracing)
- `tenant_id` (multi-tenant audit)
- `route` (endpoint identification)
- `status_code` (outcome tracking)
- `latency_ms` (performance monitoring)

## Governance Conformance

This section maps the 8 mandatory controls from Layer 05 (API Governance) to Node.js-specific implementation patterns.

### Control 1: Authentication

**Root Standard:** [API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md)

**Node.js Implementation Pattern:**

- NestJS: `@nestjs/jwt` with `JwtStrategy` guard
- Express: `passport-jwt` strategy for token validation
- Validate token signature against IdP public keys (cached)
- Enforce token expiry; refresh tokens rotated server-side
- Reject sessions for API endpoints

**Compliant Example (NestJS):**

```typescript
@Injectable()
export class JwtStrategy extends PassportStrategy(Strategy) {
  constructor(private jwtService: JwtService) {
    super({
      jwtFromRequest: ExtractJwt.fromAuthHeaderAsBearerToken(),
      secretOrKey: process.env.JWT_PUBLIC_KEY,
      audience: "https://api.example.com",
      algorithms: ["RS256"],
    });
  }

  validate(payload: any) {
    if (!payload.sub || !payload.tenant_id) {
      throw new UnauthorizedException("Invalid token");
    }
    return payload;
  }
}

@Controller("api/v1")
export class InvoiceController {
  @UseGuards(AuthGuard("jwt"))
  @Get("invoices")
  async getInvoices(@Req() req: Request) {
    return { user: req.user };
  }
}
```

**Non-Compliant Example:**

```typescript
// ❌ Session authentication for API
@Controller("api/v1")
export class InvoiceController {
  @UseGuards(SessionGuard) // Vulnerable
  @Get("invoices")
  async getInvoices(@Session() session: any) {
    return { user: session.user };
  }
}
```

### Control 2: Authorization

**Root Standard:** [API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md)

**Node.js Implementation Pattern:**

- Define custom guard classes (NestJS) or middleware (Express)
- Enforce tenant scoping + role checks
- Use decorators for permission composition
- Deny by default; explicitly grant scopes

**Compliant Example:**

```typescript
@Injectable()
export class RolesGuard implements CanActivate {
  constructor(private reflector: Reflector) {}

  canActivate(context: ExecutionContext): boolean {
    const requiredRoles = this.reflector.getAllAndOverride<string[]>("roles", [
      context.getHandler(),
      context.getClass(),
    ]);
    if (!requiredRoles) return true;

    const request = context.switchToHttp().getRequest();
    const user = request.user;

    // Tenant check + role check
    return requiredRoles.some(role =>
      user.roles?.includes(role) && user.tenant_id === request.params.tenant_id
    );
  }
}

@UseGuards(AuthGuard("jwt"), RolesGuard)
@SetMetadata("roles", ["invoice:read"])
@Get(":tenantId/invoices")
async getInvoices(@Req() req: Request) {
  return this.service.findByTenant(req.user.tenant_id);
}
```

**Non-Compliant Example:**

```typescript
// ❌ No object-level permission check
@Get(":tenantId/invoices")
async getInvoices(@Req() req: Request) {
  const tenantId = req.params.tenantId;
  // Missing tenant ownership validation
  return this.service.findByTenant(tenantId);
}
```

### Control 3: API Versioning

**Root Standard:** [API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md)

**Node.js Implementation Pattern:**

- URL-based versioning: `/api/v1/`, `/api/v2/`
- Maintain backward compatibility for 12 months
- Deprecate with HTTP `Sunset` header
- Document breaking changes in CHANGELOG

**Compliant Example:**

```typescript
// express-version-route package or manual routing
const v1Router = express.Router();
const v2Router = express.Router();

v1Router.get("/invoices", (req, res) => {
  res.json({ invoices: [], count: 0 }); // Legacy format
});

v2Router.get("/invoices", (req, res) => {
  res.set("Sunset", "Sun, 31 Dec 2026 23:59:59 GMT");
  res.json({ data: [], pagination: { count: 0, page: 1 } }); // New format
});

app.use("/api/v1", v1Router);
app.use("/api/v2", v2Router);
```

**Non-Compliant Example:**

```typescript
// ❌ No versioning; breaking changes in production
app.get("/api/invoices", (req, res) => {
  res.json({ data: [] }); // Breaking change from old format
});
```

### Control 4: Input Validation

**Root Standard:** [API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md)

**Node.js Implementation Pattern:**

- NestJS: `class-validator` with DTOs
- Express: `joi` or `express-validator`
- Reject unknown fields
- Validate field types and ranges
- Sanitize before database queries

**Compliant Example (NestJS):**

```typescript
import { IsString, IsNumber, Min, Max, Length } from "class-validator";

export class CreateInvoiceDto {
  @IsNumber()
  @Min(1)
  @Max(999999.99)
  amount: number;

  @IsString()
  @Length(3, 3)
  currency: string;

  @IsString()
  @Length(1, 500)
  description: string;
}

@Post("invoices")
@UsePipes(new ValidationPipe({ whitelist: true, forbidNonWhitelisted: true }))
async create(@Body() dto: CreateInvoiceDto) {
  return this.service.create(dto);
}
```

**Non-Compliant Example:**

```typescript
// ❌ No validation; raw request body
@Post("invoices")
async create(@Body() invoice: any) {
  return this.service.create(invoice);  // Injection risk
}
```

### Control 5: Rate Limiting

**Root Standard:** [API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md)

**Node.js Implementation Pattern:**

- `express-rate-limit` for Express
- `@nestjs/throttler` for NestJS
- Per-IP and per-user-tier enforcement
- Return 429 with `Retry-After` header
- Log hits for abuse detection

**Compliant Example:**

```typescript
// NestJS
@Module({
  imports: [
    ThrottlerModule.forRoot([{
      ttl: 60000,
      limit: 100,
      blockDuration: 60000,
    }]),
  ],
})
export class AppModule {}

@UseGuards(ThrottlerGuard)
@Get("invoices")
async getInvoices(@Req() req: Request) {
  return this.service.findByTenant(req.user.tenant_id);
}

// Express
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: (req, res) => {
    const tier = req.user?.tier || "free";
    return tier === "premium" ? 10000 : 100;
  },
  standardHeaders: true,
  legacyHeaders: false,
});

app.use(limiter);
app.get("/api/v1/invoices", limiter, getInvoices);
```

**Non-Compliant Example:**

```typescript
// ❌ No rate limiting; open to DoS
@Get("invoices")
async getInvoices(@Req() req: Request) {
  return this.service.findByTenant(req.user.tenant_id);  // No protection
}
```

### Control 6: Testing & Documentation

**Root Standard:** [API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md)

**Node.js Implementation Pattern:**

- Unit tests ≥80% coverage with Jest/Mocha
- Integration tests for all API endpoints
- OpenAPI schema auto-generated with `@nestjs/swagger`
- Document breaking changes in CHANGELOG.md

**Compliant Example:**

```typescript
// tests/invoice.controller.spec.ts
import { Test, TestingModule } from "@nestjs/testing";
import { INvoiceController } from "./invoice.controller";

describe("InvoiceController", () => {
  let controller: InvoiceController;
  let service: InvoiceService;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      controllers: [InvoiceController],
      providers: [InvoiceService],
    }).compile();

    controller = module.get<InvoiceController>(InvoiceController);
    service = module.get<InvoiceService>(InvoiceService);
  });

  it("should filter invoices by tenant", async () => {
    const mockInvoices = [{ id: 1, tenant_id: "tenant-1", amount: 100 }];
    jest.spyOn(service, "findByTenant").mockResolvedValue(mockInvoices);

    const result = await controller.getInvoices({
      user: { tenant_id: "tenant-1" },
    } as any);

    expect(result).toEqual(mockInvoices);
    expect(service.findByTenant).toHaveBeenCalledWith("tenant-1");
  });

  it("should deny cross-tenant access", async () => {
    const req = { user: { tenant_id: "tenant-1" } };
    const invoice = { id: 2, tenant_id: "tenant-2" };

    const result = await controller.getInvoice(2, req as any);
    expect(result).toBeNull(); // Or throw 403
  });
});
```

**Non-Compliant Example:**

```typescript
// ❌ No tests; no schema validation
// No test files present
// No OpenAPI/Swagger decorators
```

### Control 7: Logging & Observability

**Root Standard:** [API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md)

**Node.js Implementation Pattern:**

- Structured JSON logging via Winston/Pino
- Include correlation_id, user_id, tenant_id, action, result
- Retain logs ≥90 days
- Real-time alerting on 5xx errors, auth failures

**Compliant Example:**

```typescript
import { Injectable, NestMiddleware } from "@nestjs/common";
import * as winston from "winston";

const logger = winston.createLogger({
  format: winston.format.json(),
  transports: [
    new winston.transports.File({ filename: "security.log" }),
    new winston.transports.Console(),
  ],
});

@Injectable()
export class LoggerMiddleware implements NestMiddleware {
  use(req: any, res: any, next: () => void) {
    const correlationId = req.headers["x-correlation-id"] || generateId();
    const startTime = Date.now();

    res.on("finish", () => {
      logger.info({
        timestamp: new Date().toISOString(),
        correlation_id: correlationId,
        user_id: req.user?.sub,
        tenant_id: req.user?.tenant_id,
        method: req.method,
        path: req.path,
        status: res.statusCode,
        latency_ms: Date.now() - startTime,
        result: res.statusCode < 400 ? "ALLOW" : "DENY",
      });
    });

    next();
  }
}
```

**Non-Compliant Example:**

```typescript
// ❌ No structured logging
logger.info(`User ${req.user} accessed ${req.path}`); // Plain text
```

### Control 8: Zero Trust Networking

**Root Standard:** [API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md)

**Node.js Implementation Pattern:**

- Enforce HTTPS/TLS (via reverse proxy or middleware)
- CORS headers (whitelist origins)
- JWT audience validation
- Optional: mTLS for service-to-service

**Compliant Example:**

```typescript
import * as helmet from "helmet";
import * as cors from "cors";

// Security headers
app.use(helmet());

// CORS configuration
app.use(
  cors({
    origin: ["https://app.example.com", "https://admin.example.com"],
    credentials: true,
    methods: ["GET", "POST", "PUT", "DELETE"],
    allowedHeaders: ["Authorization", "Content-Type", "X-Correlation-ID"],
    maxAge: 3600,
  }),
);

// HTTPS redirect (optional if behind load balancer)
app.use((req, res, next) => {
  if (process.env.NODE_ENV === "production" && !req.secure) {
    return res.redirect(`https://${req.host}${req.url}`);
  }
  next();
});

// JWT audience validation (already in control 1)
```

**Non-Compliant Example:**

```typescript
// ❌ CORS wide open; HTTP allowed
app.use(cors({ origin: "*" })); // Dangerous
// No HTTPS redirect in production
```

## Multi-Tenancy Controls

### Tenant Context Propagation

- User authentication includes tenant ID in JWT claims
- Express middleware or NestJS guards extract tenant ID
- Tenant ID available in all request handlers

```typescript
@Injectable()
export class TenantGuard implements CanActivate {
  canActivate(context: ExecutionContext): boolean {
    const request = context.switchToHttp().getRequest();
    request.tenant_id = request.user?.tenant_id;
    if (!request.tenant_id) throw new UnauthorizedException();
    return true;
  }
}
```

### Resource Isolation Verification

- All queries filter by `tenant_id`
- Cross-tenant access returns 403
- ORM/query builders enforce scoping

### Audit Trail Isolation

- Logs include tenant_id for all operations
- Tenant-specific log export to authorized admins
- 90-day minimum retention per tenant

## Dependency & Supply Chain Governance

### Dependency Declaration

Node.js apps declare dependencies in `package.json` with locked versions:

```json
{
  "dependencies": {
    "express": "4.18.2",
    "@nestjs/core": "10.2.10",
    "@nestjs/jwt": "11.0.1",
    "passport-jwt": "4.0.1",
    "helmet": "7.1.0",
    "express-rate-limit": "7.1.5"
  }
}
```

### Vulnerability Scanning

CI/CD pipeline runs:

```bash
npm audit --audit-level high
snyk test
```

- HIGH severity findings block merge
- MEDIUM findings require documented mitigation
- Security patches deployed within 7 days

### Transitive Dependency Management

- `package-lock.json` pinned and committed
- Dependency updates reviewed monthly
- Breaking changes validated in staging

### License Compliance

Approved licenses:

- MIT
- Apache 2.0
- BSD (2-Clause, 3-Clause)
- ISC

Forbidden licenses:

- GPL 2.0 / AGPL

SBOM via `npm install cyclonedx-npm && cyclonedx-npm`

## Logging & Observability

### Structured Logging Format

All requests logged in JSON:

```json
{
  "timestamp": "2026-02-14T10:00:00Z",
  "correlation_id": "corr-node123",
  "user_id": "user-456",
  "tenant_id": "tenant-789",
  "method": "GET",
  "path": "/api/v1/invoices",
  "status": 200,
  "latency_ms": 45,
  "action": "READ",
  "result": "ALLOW"
}
```

### Retention & Indexing

- 90 days minimum retention
- Indexed by: correlation_id, user_id, tenant_id, status
- Enables: audit trail, error analysis, attack detection

### Real-Time Alerting

- Alert on 5xx > 5% per minute
- Alert on failed auth > 10/minute from same IP
- Alert on 403 denials > 100/hour

## CI/CD Integration

### Pre-Merge Gate

```yaml
name: Pre-Merge Security Gate

on:
  pull_request:
    branches:
      - main

jobs:
  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: NPM Dependency Audit
        run: npm audit --audit-level high

      - name: SAST (ESLint)
        run: npm run lint

      - name: Type Checking
        run: npm run type-check || echo "TypeScript check optional"

      - name: Unit Tests
        run: npm run test:cov -- --coverage-reporters=text

      - name: OpenAPI Schema Validation
        run: npm run build && npm run test:openapi || echo "Schema validation optional"
```

### Pre-Release Gate

- Integration tests passing (100% pass rate)
- Load test: p99 latency < 500ms for 100 RPS
- Schema validated + no breaking changes
- Database migrations tested on staging

### Pre-Production Gate

- Dependency audit: `npm audit --prod` passes
- Secrets validation: no credentials in config
- Canary deployment 5% traffic; monitor 15 minutes
- Health endpoint responding < 100ms

## Implementation Risk Notes

### Deployment Risks

**Middleware execution order:**

- Risk: Security middleware bypassed if added after routes
- Mitigation: Security middleware declared first in `app.ts`

**Connection pool exhaustion:**

- Risk: Database connections exhausted under load
- Mitigation: Configure pool size correctly; connection limits

**Unhandled promise rejections:**

- Risk: Silent failures; requests hang indefinitely
- Mitigation: Global error handlers + promise rejection listeners

### Performance Impact

- JWT validation: ~20ms
- Authorization checks: ~5ms
- Structured logging: ~2ms
- **Total:** ~27ms overhead acceptable for enterprise SaaS

### Operational Burden

- **Middleware debugging:** Complex chain interactions
- **Error handling:** Proper async error propagation
- **Rate limit tuning:** Monitor 429 rates per tier

### Testing Gaps

- Middleware chain ordering edge cases
- Error handling in async flows
- Concurrent request isolation (tenant context)

## Control Mapping

| EATGF Control             | ISO 27001:2022 | NIST SSDF | OWASP ASVS | NIST 800-53 | COBIT 2019 |
| ------------------------- | -------------- | --------- | ---------- | ----------- | ---------- |
| Security Headers (Helmet) | A.8.9          | PW.8      | V14        | SC-8        | DSS05.04   |
| Authentication            | A.8.5          | PW.2      | V2         | IA-2        | DSS05.03   |
| Tenant Isolation          | A.8.21         | PW.1      | V1.2       | AC-3        | APO13.01   |
| Authorization (Guards)    | A.8.35         | PW.3      | V4         | AC-2        | APO13.02   |
| Dependency Governance     | A.8.28         | PW.4      | V14        | SI-7        | BAI09      |
| Logging & Monitoring      | A.8.15         | RV.1      | V15        | AU-2        | MEA01      |
| Rate Limiting             | A.8.22         | PW.6      | V5         | SC-7        | DSS05.03   |
| Zero Trust (CORS/HTTPS)   | A.8.23         | PW.7      | V1.1       | AC-4        | APO13.03   |

## Developer Checklist

Before production deployment:

- [ ] **Helmet middleware enabled** (Express) or equivalent (NestJS)
- [ ] **Body parser size limited** (≤1MB)
- [ ] **JWT validation enforced** (no sessions)
- [ ] **Authorization guards implemented** (per route)
- [ ] **Tenant scoping enforced** on all queries
- [ ] **Dependencies locked** in package-lock.json
- [ ] **npm audit passes** (HIGH severity)
- [ ] **CORS restricted** (whitelist origins)
- [ ] **Structured JSON logging** enabled
- [ ] **HTTPS enforced** in production
- [ ] **No debug stack traces** in error responses
- [ ] **Type checking passes** (if TypeScript)
- [ ] **Unit test coverage ≥80%** (Jest/Mocha)
- [ ] **Integration tests passing** (multi-tenant scenarios)
- [ ] **Load test** completes p99 < 500ms
- [ ] **Middleware executed in correct order** (security first)

**Deployment blocked if any MANDATORY item fails.**

## Governance Implications

### If Not Implemented

**XSS exposure:**

- Risk: Unvalidated output in responses
- Impact: Account compromise, data theft
- Audit finding: OWASP ASVS V14 (Middleware) violation

**Injection vulnerabilities:**

- Risk: SQL/NoSQL/Command injection via unvalidated input
- Impact: Data breach, RCE
- Audit finding: OWASP ASVS V5 violation

**DoS attacks:**

- Risk: Unbounded payloads exhaust memory
- Impact: Service outage
- Audit finding: NIST 800-53 SC-7 violation

**Cross-tenant leakage:**

- Risk: Query without tenant filter
- Impact: GDPR violations, contract breach
- Audit finding: ISO 27001 A.8.21 violation

**Supply chain compromise:**

- Risk: Vulnerable dependency in production
- Impact: RCE, data breach
- Audit finding: NIST SSDF PW.4 violation

**Non-conformance consequences:**

- Audit findings escalate to board
- Customer SLAs violated
- Financial penalties if breach occurs

## Official References

- [NIST SP 800-218: Secure Software Development Framework](https://csrc.nist.gov/publications/detail/sp/800-218/final)
- [ISO/IEC 27001:2022 Annex A](https://www.iso.org/standard/27001)
- [OWASP ASVS 5.0](https://owasp.org/www-project-application-security-verification-standard/)
- [OWASP API Security Top 10 (2023)](https://owasp.org/www-project-api-security/)
- [NIST SP 800-53 Rev 5](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
- [COBIT 2019 Governance Framework](https://www.isaca.org/resources/cobit)
- [RFC 6749: OAuth 2.0 Authorization Framework](https://tools.ietf.org/html/rfc6749)
- [RFC 9110: HTTP Semantics](https://tools.ietf.org/html/rfc9110)
- [Express Security Documentation](https://expressjs.com/en/advanced/best-practice-security.html)
- [NestJS Security Documentation](https://docs.nestjs.com/security/authentication)

## Version Information

| Field              | Value                                     |
| ------------------ | ----------------------------------------- |
| **Version**        | 1.0                                       |
| **Release Date**   | 2026-02-14                                |
| **Change Type**    | Major (First Release)                     |
| **EATGF Baseline** | v1.0 (Phases 12a-b Complete)              |
| **Next Review**    | Q2 2026 (NestJS 11 release)               |
| **Author**         | EATGF Governance Council                  |
| **Status**         | Ready for Enterprise Deployment           |
| **Applies To**     | Express 4.x+, NestJS 9.x+, Node.js 18+LTS |
