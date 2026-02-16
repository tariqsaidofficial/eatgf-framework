# Laravel Framework Governance Profile

> **Authority Notice:** This profile implements EATGF controls for Laravel-based backend systems. It does NOT define new controls, redefine severity, or override standards. This profile clarifies HOW Laravel applications satisfy Secure SDLC (Layer 01), API Governance (Layer 05), and DevSecOps (Layer 03) requirements.

## Purpose

This document defines the governance conformance model for Laravel-based backend systems operating under the Enterprise AI-Aligned Technical Governance Framework (EATGF).

It translates EATGF Secure SDLC, API Governance, DevSecOps, and Runtime Security standards into enforceable implementation controls for enterprise Laravel applications.

This profile applies to:

- Enterprise web applications
- Multi-tenant SaaS platforms
- Internal enterprise systems
- RESTful API-first backend services
- Laravel Vapor/Sail cloud deployments

## Architectural Position

**EATGF Layer:**

- Primary: `08_DEVELOPER_GOVERNANCE_LAYER` → `FRAMEWORK_PROFILES` → `BACKEND`
- References: Layer 01 (Secure SDLC), Layer 05 (API Governance), Layer 03 (DevSecOps)

**Scope:**
Backend application layer responsible for:

- HTTP request/response handling
- Eloquent ORM data access
- Authentication and authorization
- Multi-tenancy enforcement
- API exposure via Laravel Sanctum/Passport
- Session and token management

**Laravel Classification:**

- Full-stack PHP framework with API capabilities
- Policy enforcement boundary
- Data protection control surface
- Application security boundary
- Convention-over-configuration architecture

**Conformance Obligations:**

-  01_SECURE_SDLC standards
-  02_API_GOVERNANCE standards (REST-specific controls)
-  03_DEVSECOPS standards
-  04_CLOUD standards (if deployed in SaaS context via Vapor)

## Relationship to EATGF Layers

### Layer 01: Secure SDLC

Laravel profiles enforce:

- **Dependency scanning:** `composer audit`, PHP static analysis via PHPstan/Psalm
- **SAST rules:** Psalm, PHPstan with security plugins in CI/CD pipeline
- **Code review workflow:** PR-based gate with security checklist
- **Test coverage requirement:** Minimum 80% unit + feature test coverage via PHPUnit

### Layer 03: DevSecOps Governance

Laravel profiles reference:

- **Container security:** Dockerfile with non-root user, Alpine Linux optimization
- **CI/CD pipeline gates:** Pre-merge, pre-release, pre-production stages
- **Secrets management:** Laravel .env vault encryption or AWS Secrets Manager
- **Image scanning:** Trivy/Grype vulnerability scanning in build pipeline

### Layer 05: Domain Frameworks

Laravel profiles implement API Governance controls:

- **Authentication:** Laravel Sanctum (token-based) or Passport (OAuth2/OIDC)
- **Authorization:** Laravel Policies and Gates for fine-grained access control
- **Rate Limiting:** Laravel throttle middleware, per-IP and per-user enforcement
- **OpenAPI/Swagger:** Automated schema generation via Scramble or Laravel OpenAPI
- **Versioning:** URL-based API versioning (`/api/v1/`, `/api/v2/`)

### Layer 04: Cloud Governance (Conditional)

If deployed in cloud infrastructure:

- **HTTPS enforcement:** Force HTTPS via middleware, HSTS headers
- **Environment config:** Laravel .env with encrypted secrets, AWS Secrets Manager
- **Database encryption:** RDS encryption at rest + TLS in transit
- **IAM scoping:** Service-specific IAM roles for Vapor and Lambda deployments

## Governance Principles

### 1. Secure-by-Default Configuration

Production environments must never rely on default settings.

```php
// config/app.php (production)
'debug' => (bool) env('APP_DEBUG', false),
'url' => env('APP_URL', 'https://api.example.com'),
'trusted_proxies' => ['10.0.0.0/8'],
'trusted_hosts' => ['api.example.com'],

// config/session.php
'secure' => !app()->runningUnitTests(),
'http_only' => true,
'same_site' => 'strict',

// config/hashing.php
'driver' => env('HASH_DRIVER', 'bcrypt'),
'rounds' => 12,
```

**Failure to enforce:** MANDATORY violation

### 2. Tenant Isolation as a First-Class Control

All database queries must be tenant-scoped via Laravel's query scopes.

```php
// Models/Appeal.php
class Appeal extends Model
{
    protected static function booted(): void
    {
        static::addGlobalScope('tenant', function (Builder $query) {
            if (auth()->check()) {
                $query->where('tenant_id', auth()->user()->tenant_id);
            }
        });
    }
}
```

**Global scope enforcement:** Mandatory on all multi-tenant models

### 3. Authentication via Sanctum for APIs

Laravel must use Sanctum for APIs (not session authentication).

```php
// config/sanctum.php
'stateful' => explode(',', env('SANCTUM_STATEFUL_DOMAINS', 'localhost')),
'guard' => ['web', 'api'],
'expiration' => env('SANCTUM_TOKEN_EXPIRATION', 60), // minutes
'token_prefix' => env('SANCTUM_TOKEN_PREFIX', 'test_'),

// routes/api.php
Route::middleware('auth:sanctum')->group(function () {
    Route::get('/user', fn(Request $request) => $request->user());
    Route::apiResource('appeals', AppealController::class);
});
```

**Session authentication for APIs:** MANDATORY violation

### 4. Policy-Based Authorization Enforcement

```php
// Policies/AppealPolicy.php
class AppealPolicy
{
    use HandlesAuthorization;

    public function view(User $user, Appeal $appeal): bool
    {
        return $user->tenant_id === $appeal->tenant_id &&
               ($user->can('view_appeals') || $user->id === $appeal->created_by);
    }

    public function delete(User $user, Appeal $appeal): bool
    {
        return $user->tenant_id === $appeal->tenant_id &&
               $user->can('delete_appeals');
    }
}

// Controllers/AppealController.php
public function destroy(Appeal $appeal)
{
    $this->authorize('delete', $appeal);
    $appeal->delete();
    return response()->noContent();
}
```

**Authorization scope:** Must not rely solely on middleware checks

### 5. Secrets Governance

Secrets must not exist in source code or committed .env files.

**Acceptable patterns:**

- Laravel .env encryption
- AWS Secrets Manager
- Azure Key Vault
- HashiCorp Vault

```php
// config/database.php
'mysql' => [
    'driver' => 'mysql',
    'host' => env('DB_HOST', 'localhost'),
    'password' => env('DB_PASSWORD'),  // Never hardcoded
    'ssl' => true,
    'modes' => [
        'STRICT_ALL_TABLES',
        'NO_ZERO_DATE',
    ],
],
```

**Hardcoded credentials:** MANDATORY violation

### 6. Structured Logging & Auditability

All security-relevant events logged in structured JSON format.

```php
// config/logging.php
'stack' => [
    'driver' => 'stack',
    'channels' => ['single', 'security'],
    'ignore_exceptions' => false,
],

'security' => [
    'driver' => 'single',
    'path' => storage_path('logs/security.json'),
    'level' => 'info',
    'formatter' => JsonFormatter::class,
],

// Usage
Log::channel('security')->info('User authentication', [
    'user_id' => $user->id,
    'tenant_id' => $user->tenant_id,
    'method' => 'sanctum_token',
    'ip' => request()->ip(),
    'user_agent' => request()->userAgent(),
]);
```

**Constraint:** Logs must exclude PII unless legally justified

## Governance Conformance

### Control 1: Authentication

**Root Standard:** [API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md)

**Laravel Implementation Pattern:**

- Use Laravel Sanctum for token-based API authentication
- Validate token expiry; refresh tokens rotated server-side
- Reject sessions for API endpoints
- Use Laravel Hash for password verification (bcrypt minimum 12 rounds)

**Compliant Example:**

```php
// Routes/api.php
Route::middleware('auth:sanctum')->group(function () {
    Route::get('/appeals', [AppealController::class, 'index']);
    Route::post('/appeals', [AppealController::class, 'store']);
});

// AuthController.php
public function login(Request $request)
{
    $request->validate([
        'email' => 'required|email',
        'password' => 'required',
    ]);

    if (!Auth::attempt($request->only('email', 'password'))) {
        return response()->json(['message' => 'Unauthorized'], 401);
    }

    $token = auth()->user()->createToken('api-token', ['*'])->plainTextToken;
    return response()->json(['token' => $token]);
}
```

**Non-Compliant Example:**

```php
//  Session authentication for API
Route::middleware('auth:web')->group(function () {
    Route::get('/appeals', [AppealController::class, 'index']);
});
```

### Control 2: Authorization

**Root Standard:** [API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md)

**Laravel Implementation Pattern:**

- Define Policies for resource-level authorization checks
- Register policies in AuthServiceProvider
- Enforce tenant scoping at query layer
- Don't rely solely on route-level checks

**Compliant Example:**

```php
// app/Providers/AuthServiceProvider.php
protected $policies = [
    Appeal::class => AppealPolicy::class,
    Document::class => DocumentPolicy::class,
];

// app/Policies/AppealPolicy.php
public function update(User $user, Appeal $appeal): bool
{
    return $user->tenant_id === $appeal->tenant_id &&
           $user->can('edit_appeals');
}

// app/Http/Controllers/AppealController.php
public function update(Request $request, Appeal $appeal)
{
    $this->authorize('update', $appeal);
    $appeal->update($request->validated());
    return response()->json($appeal);
}
```

**Non-Compliant Example:**

```php
//  No Policy check
public function update(Request $request, Appeal $appeal)
{
    $appeal->update($request->validated()); // No authorization
    return response()->json($appeal);
}
```

### Control 3: API Versioning

**Root Standard:** [API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md)

**Laravel Implementation Pattern:**

- Use URL-based versioning: `/api/v1/`, `/api/v2/`
- Maintain backward compatibility for 12 months
- Namespace controllers by version
- Document breaking changes in migration guide

**Compliant Example:**

```php
// routes/api.php
Route::prefix('api/v1')->group(function () {
    Route::apiResource('appeals', 'App\Http\Controllers\Api\V1\AppealController');
});

Route::prefix('api/v2')->group(function () {
    Route::apiResource('appeals', 'App\Http\Controllers\Api\V2\AppealController');
});

// app/Http/Controllers/Api/V2/AppealController.php
class AppealController extends Controller
{
    public function index()
    {
        return Appeal::paginate(25);
    }
}
```

### Control 4: Rate Limiting

**Root Standard:** [API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md)

**Laravel Implementation Pattern:**

- Use Laravel's built-in throttle middleware
- Apply per-IP and per-user rate limits
- Return HTTP 429 on limit exceeded
- Expose rate limit info in response headers

**Compliant Example:**

```php
// config/rate_limiting.php (Fortify/Sanctum)
RateLimiter::for('api', function (Request $request) {
    return Limit::perMinute(60)
        ->by($request->user()?->id ?: $request->ip())
        ->response(function (Request $request, array $headers) {
            return response()->json([
                'message' => 'Too many requests. Please try again later.',
            ], 429, $headers);
        });
});

// routes/api.php
Route::middleware('throttle:api')->group(function () {
    Route::apiResource('appeals', AppealController::class);
});
```

### Control 5: Input Validation & Sanitization

**Root Standard:** [API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md)

**Laravel Implementation Pattern:**

- Use Laravel Form Requests for centralized validation
- Sanitize all user input before processing
- Validate against JSON Schema for complex payloads
- Reject invalid MIME types

**Compliant Example:**

```php
// app/Http/Requests/StoreAppealRequest.php
class StoreAppealRequest extends FormRequest
{
    public function authorize(): bool
    {
        return true;
    }

    public function rules(): array
    {
        return [
            'title' => 'required|string|max:255|regex:/^[a-zA-Z0-9\s\-\.]+$/',
            'description' => 'required|string|max:5000',
            'priority' => 'required|in:low,medium,high,critical',
            'tenant_id' => 'required|exists:tenants,id',
        ];
    }

    public function messages(): array
    {
        return [
            'title.regex' => 'Title contains invalid characters.',
        ];
    }
}

// app/Http/Controllers/AppealController.php
public function store(StoreAppealRequest $request)
{
    $appeal = Appeal::create($request->validated());
    return response()->json($appeal, 201);
}
```

### Control 6: Response Security Headers

**Root Standard:** [API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md)

**Laravel Implementation Pattern:**

- Enforce HTTPS via middleware
- Set security headers (CSP, X-Frame-Options, X-Content-Type-Options)
- Implement via middleware or config

**Compliant Example:**

```php
// app/Http/Middleware/SecurityHeaders.php
class SecurityHeaders
{
    public function handle(Request $request, Closure $next): Response
    {
        $response = $next($request);

        $response->headers->set('X-Content-Type-Options', 'nosniff');
        $response->headers->set('X-Frame-Options', 'DENY');
        $response->headers->set('X-XSS-Protection', '1; mode=block');
        $response->headers->set('Strict-Transport-Security', 'max-age=31536000; includeSubDomains');
        $response->headers->set('Content-Security-Policy', "default-src 'none'; script-src 'self'; style-src 'self'");
        $response->headers->set('Referrer-Policy', 'no-referrer');

        return $response;
    }
}

// app/Http/Kernel.php
protected $middleware = [
    \App\Http\Middleware\SecurityHeaders::class,
];
```

### Control 7: Exception Handling & Error Disclosure

**Root Standard:** [API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md)

**Laravel Implementation Pattern:**

- Never expose stack traces in production
- Log detailed errors internally
- Return generic error messages to clients

**Compliant Example:**

```php
// app/Exceptions/Handler.php
public function register(): void
{
    $this->reportable(function (Exception $e) {
        Log::channel('security')->error('Exception occurred', [
            'exception' => get_class($e),
            'message' => $e->getMessage(),
            'tenant_id' => auth()?->user()?->tenant_id,
            'url' => request()->url(),
        ]);
    });

    $this->renderable(function (Exception $e, Request $request) {
        if ($request->expectsJson()) {
            if ($e instanceof ValidationException) {
                return response()->json(['errors' => $e->errors()], 422);
            }

            if (app()->environment('production')) {
                return response()->json([
                    'message' => 'Internal server error',
                ], 500);
            }
        }
    });
}
```

### Control 8: CORS & Cross-Origin Requests

**Root Standard:** [API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md)

**Laravel Implementation Pattern:**

- Implement mTLS for inter-service communication
- Whitelist only trusted CORS origins
- Force HTTPS
- Validate JWT audience claims

**Compliant Example:**

```php
// config/cors.php
'paths' => ['api/*', 'sanctum/csrf-cookie'],
'allowed_methods' => ['GET', 'POST', 'PUT', 'DELETE'],
'allowed_origins' => ['https://app.example.com', 'https://admin.example.com'],
'allowed_origins_patterns' => [],
'allowed_headers' => ['*'],
'supports_credentials' => true,
'exposed_headers' => ['X-Request-ID'],

// app/Http/Middleware/TrustProxies.php
protected $proxies = ['10.0.0.0/8'];
protected $headers = [
    Request::HEADER_FORWARDED => 'FORWARDED',
    Request::HEADER_X_FORWARDED_FOR => 'X_FORWARDED_FOR',
    Request::HEADER_X_FORWARDED_HOST => 'X_FORWARDED_HOST',
    Request::HEADER_X_FORWARDED_PROTO => 'X_FORWARDED_PROTO',
    Request::HEADER_X_FORWARDED_PORT => 'X_FORWARDED_PORT',
    Request::HEADER_X_FORWARDED_AWS_ELB => 'X_FORWARDED_AWS_ELB',
];
```

## Multi-Tenancy Controls

### Tenant Context Propagation

- User authentication includes tenant ID via JWT claim or session
- Middleware extracts tenant ID from authenticated user
- Global scopes automatically filter queries by tenant

```php
// app/Http/Middleware/SetTenantContext.php
class SetTenantContext
{
    public function handle(Request $request, Closure $next): mixed
    {
        if ($request->user() && $request->user()->tenant_id) {
            app()->instance('tenant_id', $request->user()->tenant_id);
            DB::statement('SET @tenant_id = ?', [$request->user()->tenant_id]);
        }
        return $next($request);
    }
}
```

### Resource Isolation Verification

- Every Model uses global scopes enforcing `tenant_id == auth()->user()->tenant_id`
- Queries include eager loading for tenant context
- Cross-tenant resource access returns 403 Forbidden

```php
// Models/BaseModel.php (all models extend this)
abstract class BaseModel extends Model
{
    protected static function booted(): void
    {
        static::addGlobalScope('tenant', function (Builder $query) {
            if (auth()->check() && auth()->user()->tenant_id) {
                $query->where('tenant_id', auth()->user()->tenant_id);
            }
        });
    }
}

// Models/Appeal.php
class Appeal extends BaseModel
{
    // Automatic tenant scoping via global scope
}
```

### Audit Trail Isolation

- Logs include tenant_id for all operations
- Tenant-specific audit trail exports available only to tenant admins
- Compliance audit trails stored separately per tenant with 90-day minimum retention

```php
// app/Models/AuditLog.php
class AuditLog extends Model
{
    protected $fillable = ['tenant_id', 'user_id', 'action', 'model', 'record_id', 'data'];

    protected static function booted(): void
    {
        static::creating(function (self $model) {
            $model->tenant_id = auth()->user()->tenant_id;
            $model->user_id = auth()->user()->id;
        });
    }
}

// app/Observers/AppealObserver.php
class AppealObserver
{
    public function updated(Appeal $appeal): void
    {
        AuditLog::create([
            'action' => 'updated',
            'model' => 'Appeal',
            'record_id' => $appeal->id,
            'data' => $appeal->getChanges(),
        ]);
    }
}
```

## Dependency & Supply Chain Governance

### Dependency Declaration

Laravel projects declare dependencies in `composer.json`:

```json
{
  "require": {
    "php": "^8.3",
    "laravel/framework": "^11.0",
    "laravel/sanctum": "^4.0",
    "laravel/tinker": "^2.8",
    "doctrine/dbal": "^4.0",
    "spatie/laravel-permission": "^6.0"
  },
  "require-dev": {
    "phpstan/phpstan": "^1.0",
    "psalm/plugin-laravel": "^2.0",
    "phpunit/phpunit": "^11.0"
  }
}
```

### Vulnerability Scanning

CI/CD pipeline runs:

```bash
composer audit
composer audit --format=json
phpstan analyse --level=9 app/
psalm --show-info=true
```

- HIGH severity findings block merge
- MEDIUM findings require documented mitigation
- Security patches deployed within 7 days of CVE publication

### Composer Lock Discipline

- `composer.lock` committed to repository
- All dependencies pinned to exact versions
- Updates only via `composer update` with security review
- No dynamic version constraints in production

## CI/CD Integration Gates

### Pre-Merge Gate

- Testing: `php artisan test` (100% pass rate required)
- Code quality: `phpstan analyse --level=9`
- Security: `composer audit --strict`
- Code style: `php artisan pint --test`

```yaml
# .github/workflows/test.yml
- name: Run security audit
  run: composer audit --strict

- name: Run static analysis
  run: phpstan analyse --level=9 app/

- name: Run tests
  run: php artisan test --coverage --min=80

- name: Check code style
  run: php artisan pint --test
```

### Pre-Release Gate

- Integration tests passing (100% pass rate)
- Load test: p99 latency < 500ms for 100 RPS
- API schema stable (no breaking changes from v1.0)
- Database migrations tested on staging

```bash
php artisan migrate --force --env=staging
php artisan test --env=staging --parallel
```

### Pre-Production Gate

- Dependency audit passes: `composer audit` with no HIGH findings
- Secrets in production config validated (not in code)
- Canary deployment to 5% traffic (Laravel Vapor deployment)
- Monitor error rates for 15 minutes

## Implementation Risk Notes

### Deployment Risks

**Breaking API changes:**

- Risk: Clients using old endpoints fail silently
- Mitigation: Semantic versioning (v1 → v2 separate namespace), 6+ month deprecation window

**Database migration failures:**

- Risk: Locks production database during upgrade
- Mitigation: Zero-downtime migrations, test on staging replica, automated rollback via `php artisan migrate:rollback`

**Policy evaluation latency:**

- Risk: Authorization checks add overhead
- Mitigation: Cache policy results; eager load relationships

### Performance Impact

- Authentication adds ~15ms per request (token validation)
- Authorization (policy check) adds ~8ms per request
- Structured logging adds ~3ms per request (JSON serialization)
- **Total:** ~26ms overhead on typical request
- Acceptable for enterprise SaaS (p99 latency <500ms achievable)

### Operational Burden

- **RBAC/ABAC maintenance:** Quarterly governance review of policies
- **Rate limit tuning:** Monitor 429 error rates; adjust per-tier if complaints spike
- **Dependency updates:** Monthly security patch cycle with 30-day testing window

### Testing Gaps

- Hard to test cross-tenant isolation without multiple staging tenants
- Rate limit exhaustion testing requires load testing infrastructure
- Policy failover scenarios require comprehensive permission matrix testing

## Control Mapping

| EATGF Control         | ISO 27001:2022 | NIST SSDF | OWASP ASVS | NIST 800-53 | COBIT 2019 |
| --------------------- | -------------- | --------- | ---------- | ----------- | ---------- |
| Secure Config         | A.8.9          | PW.8      | V14        | CM-6        | DSS05.04   |
| Authentication        | A.8.5          | PW.2      | V2         | IA-2        | DSS05.03   |
| Tenant Isolation      | A.8.21         | PW.1      | V1.2       | AC-3        | APO13.01   |
| Logging               | A.8.15         | RV.1      | V15        | AU-2        | MEA01      |
| Dependency Governance | A.8.28         | PW.4      | V14        | SI-7        | BAI09      |
| Authorization         | A.8.35         | PW.3      | V4         | AC-2        | APO13.02   |
| Rate Limiting         | A.8.22         | PW.6      | V5         | SC-7        | DSS05.03   |
| Policy Enforcement    | A.8.23         | PW.7      | V1.1       | AC-4        | APO13.03   |

## Developer Checklist

Before production deployment:

- [ ] **APP_DEBUG=false** in `.env.production`
- [ ] **APP_KEY** sourced from Key Vault (not committed)
- [ ] **ALLOWED_HOSTS** explicitly defined in `config/app.php` (not `*`)
- [ ] **HTTPS enforced** (middleware or load balancer)
- [ ] **Sanctum tokens** configured with expiration
- [ ] **Policies** registered in AuthServiceProvider
- [ ] **Global scopes** implemented on all multi-tenant models
- [ ] **composer.lock** committed to repository
- [ ] **composer audit** passes (no HIGH findings)
- [ ] **Structured logging** enabled with tenant context
- [ ] **Security headers middleware** configured
- [ ] **CORS** configured with whitelisted origins only
- [ ] **Database connections** use SSL/TLS
- [ ] **Unit test coverage ≥80%** (phpunit coverage report)
- [ ] **Feature tests** passing for multi-tenant scenarios
- [ ] **Load test** completes with p99 < 500ms
- [ ] **Database migrations** tested on staging replica
- [ ] **Error handling** does not expose stack traces in production

**Deployment blocked if any MANDATORY item fails.**

## Governance Implications

### If Not Implemented

**Cross-tenant data exposure:**

- Risk: Tenant A queries Tenant B data
- Impact: GDPR/CCPA violations, contract breach, reputation damage
- Audit finding: ISO 27001 A.8.21 (Access control) violation

**Compromised API tokens:**

- Risk: Stale tokens accepted; session hijacking
- Impact: Account takeover, fraud, compliance failure
- Audit finding: NIST 800-53 IA-2 (Authentication) violation

**Vulnerable dependencies:**

- Risk: Compromised package deployed to production
- Impact: RCE, data breach, ransomware
- Audit finding: NIST SSDF PW.4 (Dependency management) violation

**PII exposure in logs:**

- Risk: Customer data in plain-text logs
- Impact: GDPR Article 32 violation, SOC2 Type I failure
- Audit finding: ISO 27001 A.8.15 (Logging) violation

**Audit failure:**

- Laravel without governance = non-compliant under EATGF
- SOC2 Type II certification blocked
- PCI-DSS requirement for code review, testing, logging failures

## Official References

- [NIST SP 800-218: Secure Software Development Framework](https://csrc.nist.gov/publications/detail/sp/800-218/final)
- [ISO/IEC 27001:2022 Annex A](https://www.iso.org/standard/27001)
- [OWASP ASVS 5.0](https://owasp.org/www-project-application-security-verification-standard/)
- [OWASP API Security Top 10 (2023)](https://owasp.org/www-project-api-security/)
- [NIST SP 800-53 Rev 5](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
- [COBIT 2019 Governance Framework](https://www.isaca.org/resources/cobit)
- [Laravel Security Best Practices](https://laravel.com/docs/security)
- [OWASP PHP Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/PHP_Security_Cheat_Sheet.html)

## Version Information

| Field              | Value                               |
| ------------------ | ----------------------------------- |
| **Version**        | 1.0                                 |
| **Release Date**   | 2026-02-15                          |
| **Change Type**    | Major (First Release)               |
| **EATGF Baseline** | v1.0 (Phases 12a-b Complete)        |
| **Next Review**    | Q2 2026 (Laravel 12 LTS release)    |
| **Author**         | EATGF Governance Council            |
| **Status**         | Ready for Enterprise Deployment     |
