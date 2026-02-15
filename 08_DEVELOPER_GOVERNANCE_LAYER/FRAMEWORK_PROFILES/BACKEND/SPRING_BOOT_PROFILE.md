# Spring Boot Framework Governance Profile

> **Authority Notice:** This profile implements EATGF controls for Spring Boot-based backend systems. It does NOT define new controls, redefine severity, or override standards. This profile clarifies HOW Spring Boot applications satisfy Secure SDLC (Layer 01), API Governance (Layer 05), and DevSecOps (Layer 03) requirements.

## Purpose

This document defines governance conformance requirements for Spring Boot backend systems operating under the Enterprise AI-Aligned Technical Governance Framework (EATGF).

It establishes enforceable controls for:

- REST API security via Spring Security
- Bean-based dependency injection
- JDBC/JPA database access patterns
- Multi-tenant architecture using Spring properties
- Microservices integration via Spring Cloud
- DevSecOps compliance via Maven/Gradle

This profile applies to:

- Enterprise SaaS backends
- Microservices distributed systems
- High-concurrency batch processing
- Spring Cloud deployments
- Cloud-native Java applications

## Architectural Position

**EATGF Layer:**

- Primary: `08_DEVELOPER_GOVERNANCE_LAYER` → `FRAMEWORK_PROFILES` → `BACKEND`
- References: Layer 01 (Secure SDLC), Layer 05 (API Governance), Layer 03 (DevSecOps)

**Scope:**
Spring Boot functions as:

- HTTP request-response handler (Spring Web/WebFlux)
- Spring Security authentication/authorization layer
- Spring Data entity-to-database mapping layer
- Configuration management (application.yml/properties)
- Health check / observability endpoint (Actuator)

**Spring Boot Classification:**

- Enterprise framework with bean management
- Annotation-driven configuration
- Built-in production readiness features
- Strong Spring Security integration
- Application security boundary

**Conformance Obligations:**

- ✅ 01_SECURE_SDLC standards
- ✅ 02_API_GOVERNANCE standards (REST-specific controls)
- ✅ 03_DEVSECOPS standards
- ✅ 04_CLOUD standards (if deployed in SaaS context)

## Relationship to EATGF Layers

### Layer 01: Secure SDLC

Spring Boot profiles enforce:

- **Dependency scanning:** `mvn dependency:check` + OWASP plugins in CI/CD
- **SAST rules:** SonarQube + Checkstyle for Java security patterns
- **Code review workflow:** PR-based with security checklist
- **Test coverage requirement:** Minimum 80% unit + integration test coverage via JaCoCo

### Layer 03: DevSecOps Governance

Spring Boot profiles reference:

- **Container security:** Docker multi-stage builds, non-root user, JVM security flags
- **CI/CD pipeline gates:** Pre-merge, pre-release, pre-production stages
- **Secrets management:** Spring Cloud Config + HashiCorp Vault integration
- **Image scanning:** Trivy vulnerability scanning + SBOM generation

### Layer 05: Domain Frameworks

Spring Boot profiles implement API Governance controls:

- **Authentication:** Spring Security + JWT | OIDC via OAuth2 resource server
- **Authorization:** `@PreAuthorize` + `@Secured` annotations + role-based access control
- **Rate Limiting:** Spring Cloud Gateway rate limiting or custom Bucket4j integration
- **OpenAPI/Swagger:** SpringDoc OpenAPI (`springdoc-openapi-ui`) for auto-generation
- **Versioning:** URL-based versioning (`/api/v1/`, `/api/v2/`)

### Layer 04: Cloud Governance (Conditional)

If deployed in cloud infrastructure:

- **HTTPS enforcement:** Spring Security configuration + server.ssl properties
- **Environment config:** Spring Cloud Config + Spring Boot Actuator configuration endpoints
- **Database encryption:** JDBC URL with SSL + Spring Data encryption at rest
- **IAM scoping:** Spring Cloud AWS for ECS/EKS IAM role management

## Governance Principles

### 1. Spring Security Configuration (Mandatory)

Spring Security must be configured with explicit bean declarations.

```java
@Configuration
@EnableWebSecurity
public class SecurityConfig {

    @Bean
    public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        http
            .csrf().disable()  // Disable if stateless REST API
            .authorizeRequests()
                .antMatchers("/actuator/health").permitAll()
                .antMatchers("/api/v1/**").authenticated()
            .and()
            .sessionManagement().sessionCreationPolicy(SessionCreationPolicy.STATELESS);

        return http.build();
    }

    @Bean
    public JwtAuthenticationProvider jwtAuthenticationProvider() {
        return new JwtAuthenticationProvider(jwtTokenProvider);
    }
}
```

**Constraint:** Using default Spring Security without explicit configuration is governance violation

### 2. JWT/OIDC Authentication Enforcement

Session-based authentication is prohibited for API services.

```java
@Component
public class JwtTokenProvider {

    private static final String JWT_ALGORITHM = "RS256";
    private static final long JWT_EXPIRATION = 3600000;  // 1 hour

    public String generateToken(UserDetails user) {
        return Jwts.builder()
            .setSubject(user.getUsername())
            .setIssuedAt(now())
            .setExpiration(expirationTime())
            .signWith(SignatureAlgorithm.RS256, getPrivateKey())
            .claim("tenant_id", getTenantId(user))
            .claim("aud", "https://api.example.com")
            .compact();
    }

    public boolean validateToken(String token) {
        try {
            Jwts.parser()
                .setSigningKey(getPublicKey())
                .parse(token);
            return true;
        } catch (JwtException | IllegalArgumentException e) {
            return false;
        }
    }
}
```

**Token must include:**

- `sub` (subject/user ID)
- `tenant_id` (tenant scope)
- `aud` (audience: API identifier)
- `exp` (expiration)
- `iat` (issued at)

### 3. Role-Based Authorization (Annotations)

```java
@RestController
@RequestMapping("/api/v1/invoices")
public class InvoiceController {

    @PreAuthorize("hasRole('ROLE_USER') and #tenantId == authentication.principal.tenantId")
    @GetMapping("/{tenantId}")
    public ResponseEntity<List<Invoice>> getInvoices(@PathVariable String tenantId) {
        return ResponseEntity.ok(invoiceService.findByTenant(tenantId));
    }

    @PreAuthorize("hasRole('ROLE_TENANT_ADMIN')")
    @PostMapping("/{tenantId}")
    public ResponseEntity<Invoice> createInvoice(@PathVariable String tenantId, @RequestBody InvoiceRequest request) {
        return ResponseEntity.ok(invoiceService.create(tenantId, request));
    }
}
```

**Constraint:** Authorization must be explicit per method; implicit is non-compliant

### 4. Tenant Isolation via Spring Data

```java
@Repository
public interface InvoiceRepository extends JpaRepository<Invoice, Long> {
    List<Invoice> findByTenantId(String tenantId);

    @Query("SELECT i FROM Invoice i WHERE i.tenantId = ?1")
    Page<Invoice> findByTenantIdWithPagination(String tenantId, Pageable pageable);
}

@Service
public class InvoiceService {

    @Autowired
    private InvoiceRepository repository;

    public List<Invoice> findByTenant(String tenantId) {
        // Filter enforced at repository layer
        return repository.findByTenantId(tenantId);
    }
}
```

**Constraint:** Global queries without tenant filter are critical violation

### 5. Configuration Externalization (Secrets)

Secrets must be externalized via Spring Cloud Config or environment variables.

```yaml
# application-production.yml
spring:
  datasource:
    url: ${DATABASE_URL}
    username: ${DB_USERNAME}
    password: ${DB_PASSWORD}
  security:
    oauth2:
      resourceserver:
        jwt:
          key-value: ${JWT_PUBLIC_KEY}
          issuer-uri: ${JWT_ISSUER}

jwt:
  secret: ${JWT_SECRET}
  audience: "https://api.example.com"
```

**Constraint:** Hardcoded secrets in source code are MANDATORY violation

### 6. Structured Logging with SLF4J

```java
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

@Component
public class SecurityAuditLogging {

    private static final Logger logger = LoggerFactory.getLogger("security.audit");

    public void logAuthenticationEvent(String userId, String tenantId, boolean success) {
        logger.info(
            "event=authentication user_id={} tenant_id={} result={} timestamp={}",
            userId, tenantId, success ? "ALLOW" : "DENY", Instant.now()
        );
    }
}
```

Configuration in `logback-spring.xml`:

```xml
<configuration>
    <appender name="json" class="ch.qos.logback.core.ConsoleAppender">
        <encoder class="net.logstash.logback.encoder.LogstashEncoder">
            <customFields>{"service":"api","environment":"production"}</customFields>
        </encoder>
    </appender>

    <root level="INFO">
        <appender-ref ref="json" />
    </root>
</configuration>
```

**Logs must include:**

- correlation_id (request tracing)
- tenant_id (multi-tenant audit)
- endpoint (API path)
- status (HTTP response code)
- latency_ms (request duration)

## Governance Conformance

This section maps the 8 mandatory controls from Layer 05 (API Governance) to Spring Boot-specific implementation patterns.

### Control 1: Authentication

**Root Standard:** [API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md#control-1-authentication)

**Spring Boot Implementation Pattern:**

- Spring Security + `JwtAuthenticationProvider`
- Token validation via `JwtTokenProvider.validateToken()`
- Enforce token expiry via `exp` claim validation
- Reject sessions; use stateless JWT only

**Compliant Example:**

```java
@Configuration
@EnableWebSecurity
public class SecurityConfig {

    @Bean
    public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        http
            .csrf().disable()
            .sessionManagement()
                .sessionCreationPolicy(SessionCreationPolicy.STATELESS)
            .and()
            .authorizeRequests()
                .antMatchers("/api/**").authenticated()
            .and()
            .oauth2ResourceServer()
                .jwt()
                .decoder(jwtDecoder());

        return http.build();
    }

    @Bean
    public JwtDecoder jwtDecoder() {
        return NimbusJwtDecoder.withPublicKey(rsaKey.getPublicKey()).build();
    }
}
```

**Non-Compliant Example:**

```java
// ❌ Session authentication for API
@Configuration
@EnableWebSecurity
public class SecurityConfig {
    @Bean
    public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        http
            .sessionManagement()
                .sessionCreationPolicy(SessionCreationPolicy.IF_REQUIRED)  // Vulnerable
            .and()
            .formLogin();  // Session-based login
        return http.build();
    }
}
```

### Control 2: Authorization

**Root Standard:** [API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md#control-2-authorization)

**Spring Boot Implementation Pattern:**

- `@PreAuthorize` annotations with SpEL expressions
- Tenant-aware permission checks
- Custom `PermissionEvaluator` for object-level authorization
- Deny by default via `authorizeRequests()`

**Compliant Example:**

```java
@Component
public class SecurityPermissionEvaluator implements PermissionEvaluator {

    @Autowired
    private InvoiceRepository invoiceRepository;

    @Override
    public boolean hasPermission(Authentication auth, Object o, Object permission) {
        if (!(auth.getPrincipal() instanceof UserDetails)) {
            return false;
        }

        UserDetails user = (UserDetails) auth.getPrincipal();
        Invoice invoice = (Invoice) o;

        // Tenant check + ownership check
        return invoice.getTenantId().equals(user.getTenantId()) &&
               invoice.getUserId().equals(user.getUsername());
    }
}

@RestController
@RequestMapping("/api/v1/invoices")
public class InvoiceController {

    @PreAuthorize("@securityPermissionEvaluator.hasPermission(authentication, #invoice, 'READ')")
    @GetMapping("/{id}")
    public ResponseEntity<Invoice> getInvoice(@PathVariable Long id) {
        Invoice invoice = invoiceService.findById(id);
        return ResponseEntity.ok(invoice);
    }
}
```

**Non-Compliant Example:**

```java
// ❌ No object-level permission check
@GetMapping("/{id}")
public ResponseEntity<Invoice> getInvoice(@PathVariable Long id) {
    // Missing tenant/ownership validation
    Invoice invoice = invoiceService.findById(id);
    return ResponseEntity.ok(invoice);
}
```

### Control 3: API Versioning

**Root Standard:** [API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md#control-3-versioning)

**Spring Boot Implementation Pattern:**

- URL-based versioning: `/api/v1/`, `/api/v2/`
- Maintain backward compatibility for 12 months
- Deprecation headers via Spring HTTP status
- Document in CHANGELOG.md

**Compliant Example:**

```java
@RestController
public class VersionedInvoiceController {

    @GetMapping("/api/v1/invoices")
    public ResponseEntity<InvoiceResponseV1> getInvoicesV1() {
        // Legacy response format
        return ResponseEntity.ok(new InvoiceResponseV1());
    }

    @GetMapping("/api/v2/invoices")
    public ResponseEntity<InvoiceResponseV2> getInvoicesV2(HttpServletResponse response) {
        // New response format
        response.setHeader("Sunset", "Sun, 31 Dec 2026 23:59:59 GMT");
        response.setHeader("Deprecation", "Sun, 31 Dec 2025 23:59:59 GMT");
        return ResponseEntity.ok(new InvoiceResponseV2());
    }
}
```

**Non-Compliant Example:**

```java
// ❌ No versioning; breaking changes in production
@GetMapping("/api/invoices")
public ResponseEntity<InvoiceResponseV2> getInvoices() {
    // Breaking change: removed fields from v1
    return ResponseEntity.ok(new InvoiceResponseV2());
}
```

### Control 4: Input Validation

**Root Standard:** [API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md#control-4-input-validation)

**Spring Boot Implementation Pattern:**

- Jakarta Validation (formerly javax.validation) annotations
- Custom validators for business logic
- Exception handlers for validation errors
- Sanitization before database operations

**Compliant Example:**

```java
@Data
public class InvoiceRequest {

    @NotNull(message = "Amount is required")
    @DecimalMin(value = "0.01", message = "Amount must be positive")
    @DecimalMax(value = "999999.99", message = "Amount exceeds limit")
    private BigDecimal amount;

    @NotBlank(message = "Currency is required")
    @Pattern(regexp = "^[A-Z]{3}$", message = "Currency must be 3 uppercase letters")
    private String currency;

    @NotBlank(message = "Description is required")
    @Size(min = 1, max = 500, message = "Description must be 1-500 characters")
    private String description;
}

@RestController
@RequestMapping("/api/v1/invoices")
public class InvoiceController {

    @PostMapping
    public ResponseEntity<Invoice> createInvoice(
        @Valid @RequestBody InvoiceRequest request,
        @AuthenticationPrincipal UserDetails user
    ) {
        // Validation already passed by @Valid
        Invoice invoice = invoiceService.create(user.getTenantId(), request);
        return ResponseEntity.status(HttpStatus.CREATED).body(invoice);
    }

    @ExceptionHandler(MethodArgumentNotValidException.class)
    public ResponseEntity<ValidationErrorResponse> handleValidationExceptions(
        MethodArgumentNotValidException ex
    ) {
        Map<String, String> errors = new HashMap<>();
        ex.getBindingResult()
            .getFieldErrors()
            .forEach(err -> errors.put(err.getField(), err.getDefaultMessage()));
        return ResponseEntity.badRequest().body(new ValidationErrorResponse(errors));
    }
}
```

**Non-Compliant Example:**

```java
// ❌ No validation; raw request body
@PostMapping
public ResponseEntity<Invoice> createInvoice(@RequestBody Map<String, Object> request) {
    // Injection risk; no type safety
    Invoice invoice = invoiceService.create(request);
    return ResponseEntity.ok(invoice);
}
```

### Control 5: Rate Limiting

**Root Standard:** [API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md#control-5-rate-limiting)

**Spring Boot Implementation Pattern:**

- Spring Cloud Gateway rate limiting (preferred for microservices)
- Bucket4j library for custom rate limiting
- Per-IP and per-user-tier enforcement
- Return 429 with `Retry-After` header

**Compliant Example:**

```java
@Component
public class RateLimitingFilter implements Filter {

    @Autowired
    private RateLimiterRegistry rateLimiterRegistry;

    @Override
    public void doFilter(ServletRequest request, ServletResponse response,
                        FilterChain chain) throws IOException, ServletException {
        HttpServletRequest httpRequest = (HttpServletRequest) request;
        String clientId = getClientId(httpRequest);

        RateLimiter rateLimiter = rateLimiterRegistry.rateLimiter(clientId);

        if (rateLimiter.acquirePermission()) {
            chain.doFilter(request, response);
        } else {
            sendTooManyRequests((HttpServletResponse) response);
        }
    }

    private void sendTooManyRequests(HttpServletResponse response) throws IOException {
        response.setStatus(HttpStatus.TOO_MANY_REQUESTS.value());
        response.setHeader("Retry-After", "60");
        response.getWriter().write("{\"error\": \"Rate limit exceeded\"}");
    }
}

// Configuration
@Configuration
public class RateLimitingConfig {

    @Bean
    public RateLimiterRegistry rateLimiterRegistry() {
        RateLimiterConfig config = RateLimiterConfig.custom()
            .limitRefreshPeriod(Duration.ofMinutes(1))
            .limitForPeriod(100)
            .timeoutDuration(Duration.ofSeconds(2))
            .build();

        return RateLimiterRegistry.of(config);
    }
}
```

**Non-Compliant Example:**

```java
// ❌ No rate limiting; open to DoS
@GetMapping("/api/v1/invoices")
public ResponseEntity<List<Invoice>> getInvoices(@AuthenticationPrincipal UserDetails user) {
    // No rate limit protection
    return ResponseEntity.ok(invoiceService.findAll());
}
```

### Control 6: Testing & Documentation

**Root Standard:** [API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md#control-6-testing)

**Spring Boot Implementation Pattern:**

- Unit tests ≥80% coverage via JaCoCo
- Integration tests with `@SpringBootTest`
- OpenAPI schema auto-generated via SpringDoc
- Document breaking changes in CHANGELOG.md

**Compliant Example:**

```java
@SpringBootTest
@AutoConfigureMockMvc
public class InvoiceControllerTest {

    @Autowired
    private MockMvc mockMvc;

    @Autowired
    private InvoiceService invoiceService;

    @Test
    public void testGetInvoiceFilteredByTenant() throws Exception {
        String jwt = generateTestJwt("user-1", "tenant-1");

        mockMvc.perform(get("/api/v1/invoices")
            .header("Authorization", "Bearer " + jwt))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$[0].tenantId").value("tenant-1"));
    }

    @Test
    public void testCrossTenantAccessDenied() throws Exception {
        String jwt = generateTestJwt("user-1", "tenant-1");

        mockMvc.perform(get("/api/v1/invoices/999")
            .header("Authorization", "Bearer " + jwt))
            .andExpect(status().isForbidden());
    }
}

// pom.xml
<dependency>
    <groupId>org.jacoco</groupId>
    <artifactId>jacoco-maven-plugin</artifactId>
    <version>0.8.8</version>
</dependency>

// springdoc-openapi for auto-generated OpenAPI
<dependency>
    <groupId>org.springdoc</groupId>
    <artifactId>springdoc-openapi-ui</artifactId>
    <version>1.7.0</version>
</dependency>
```

**Non-Compliant Example:**

```java
// ❌ No tests; no OpenAPI schema
// No test files present
// No @Operation annotations in controller
```

### Control 7: Logging & Observability

**Root Standard:** [API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md#control-7-logging)

**Spring Boot Implementation Pattern:**

- Structured JSON logging via Logstash encoder
- Spring MVC interceptors for request/response logging
- MDC (Mapped Diagnostic Context) for correlation IDs
- Spring Boot Actuator for health + metrics

**Compliant Example:**

```java
@Component
public class RequestLoggingInterceptor implements HandlerInterceptor {

    private static final Logger logger = LoggerFactory.getLogger("security.audit");

    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response,
                            Object handler) throws Exception {
        String correlationId = UUID.randomUUID().toString();
        MDC.put("correlation_id", correlationId);
        request.setAttribute("startTime", System.currentTimeMillis());
        return true;
    }

    @Override
    public void afterCompletion(HttpServletRequest request, HttpServletResponse response,
                               Object handler, Exception ex) throws Exception {
        long latency = System.currentTimeMillis() - (long) request.getAttribute("startTime");

        logger.info(
            "method={} path={} status={} latency_ms={} tenant_id={}",
            request.getMethod(),
            request.getRequestURI(),
            response.getStatus(),
            latency,
            request.getAttribute("tenantId")
        );

        MDC.remove("correlation_id");
    }
}

// logback-spring.xml with Logstash encoder
<configuration>
    <appender name="logstash" class="ch.qos.logback.core.ConsoleAppender">
        <encoder class="net.logstash.logback.encoder.LogstashEncoder" />
    </appender>
    <root level="INFO">
        <appender-ref ref="logstash" />
    </root>
</configuration>

// Actuator configuration
spring:
  endpoints:
    web:
      exposure:
        include: health,metrics,prometheus
  endpoint:
    health:
      show-details: when-authorized
```

**Non-Compliant Example:**

```java
// ❌ No structured logging
logger.info("User " + user + " accessed " + path);  // Plain text
```

### Control 8: Zero Trust Networking

**Root Standard:** [API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md#control-8-zero-trust)

**Spring Boot Implementation Pattern:**

- HTTPS/TLS enforcement via `server.ssl` configuration
- CORS restriction via Spring Security
- JWT audience validation
- Optional: mTLS for inter-service communication

**Compliant Example:**

```yaml
# application-production.yml
server:
  ssl:
    enabled: true
    key-store: ${SSL_KEYSTORE_PATH}
    key-store-password: ${SSL_KEYSTORE_PASSWORD}
    key-store-type: PKCS12
    key-alias: tomcat

spring:
  web:
    cors:
      allowed-origins: https://app.example.com,https://admin.example.com
      allowed-methods: GET,POST,PUT,DELETE
      allowed-headers: Authorization,Content-Type,X-Correlation-ID
      allow-credentials: true
      max-age: 3600
```

```java
@Configuration
public class SecurityConfig {

    @Bean
    public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        http
            .requiresChannel().anyRequest().requiresSecure()  // HTTPS only
            .and()
            .oauth2ResourceServer().jwt()
                .jwtAuthenticationConverter(jwtAuthenticationConverter());

        return http.build();
    }

    @Bean
    public JwtAuthenticationConverter jwtAuthenticationConverter() {
        JwtAuthenticationConverter converter = new JwtAuthenticationConverter();
        converter.setJwtGrantedAuthoritiesConverter(jwt ->
            List.of(new SimpleGrantedAuthority("ROLE_USER"))
        );
        return converter;
    }
}
```

**Non-Compliant Example:**

```yaml
# ❌ No HTTPS; HTTP allowed
server:
  ssl:
    enabled: false

# ❌ CORS wide open
spring:
  web:
    cors:
      allowed-origins: "*" # Dangerous
```

## Multi-Tenancy Controls

### Tenant Context Propagation

- JWT claims include tenant ID passed by authentication
- Tenant ID extracted in security context
- Available via `@AuthenticationPrincipal` in all request handlers

```java
@Component
public class TenantContextHolder {

    private static final ThreadLocal<String> tenantContext = new ThreadLocal<>();

    public static void setTenant(String tenantId) {
        tenantContext.set(tenantId);
    }

    public static String getTenant() {
        return tenantContext.get();
    }

    public static void clear() {
        tenantContext.remove();
    }
}

@Component
public class TenantInterceptor implements HandlerInterceptor {

    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response,
                            Object handler) throws Exception {
        Authentication auth = SecurityContextHolder.getContext().getAuthentication();
        if (auth instanceof JwtAuthenticationToken) {
            String tenantId = ((JwtAuthenticationToken) auth).getToken()
                .getClaimAsString("tenant_id");
            TenantContextHolder.setTenant(tenantId);
        }
        return true;
    }

    @Override
    public void afterCompletion(HttpServletRequest request, HttpServletResponse response,
                               Object handler, Exception ex) throws Exception {
        TenantContextHolder.clear();
    }
}
```

### Resource Isolation Verification

- All Spring Data JPA queries filtered by `tenantId`
- ORM automatically applies tenant scoping
- Cross-tenant access returns 403

### Audit Trail Isolation

- Logs include tenant_id for all operations
- Tenant-specific log export to determined admins
- 90-day minimum retention per tenant

## Dependency & Supply Chain Governance

### Dependency Declaration

Spring Boot applications declare dependencies via Maven `pom.xml` or Gradle `build.gradle`:

```xml
<!-- pom.xml -->
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
        <version>3.2.0</version>
    </dependency>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-security</artifactId>
        <version>3.2.0</version>
    </dependency>
    <dependency>
        <groupId>io.jsonwebtoken</groupId>
        <artifactId>jjwt-api</artifactId>
        <version>0.12.3</version>
    </dependency>
    <dependency>
        <groupId>org.springframework.data</groupId>
        <artifactId>spring-data-jpa</artifactId>
        <version>3.2.0</version>
    </dependency>
</dependencies>
```

### Vulnerability Scanning

CI/CD runs:

```bash
mvn org.owasp:dependency-check-maven:check
mvn clean verify  # Includes dependency resolution
```

- HIGH severity findings block merge
- MEDIUM findings require documented mitigation
- Security patches deployed within 7 days

### Transitive Dependency Management

- `pom.xml.lock` or similar pinned
- Dependency updates reviewed monthly with testing
- Spring Boot BOM ensures version compatibility

### License Compliance

Approved licenses:

- MIT
- Apache 2.0
- BSD (2-Clause, 3-Clause)
- ISC

Forbidden licenses:

- GPL 2.0 / AGPL

SBOM via `mvn cyclonedx:makeBom`

## Logging & Observability

### Structured Logging Format

All requests logged in JSON via Logstash:

```json
{
  "timestamp": "2026-02-15T10:00:00Z",
  "correlation_id": "corr-spring123",
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
- Enables: audit trail, error trend analysis, security events

### Real-Time Alerting

- Alert on 5xx error rate > 5% per minute
- Alert on failed auth > 10/minute from same IP
- Alert on 403 denials > 100/hour (permission brute-force)

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

      - name: Set up JDK 21
        uses: actions/setup-java@v3
        with:
          java-version: "21"
          distribution: "temurin"

      - name: Dependency Check (OWASP)
        run: mvn org.owasp:dependency-check-maven:check

      - name: SAST (SonarQube)
        run: mvn clean verify sonar:sonar

      - name: Unit Tests with Coverage
        run: mvn clean test jacoco:report

      - name: Coverage threshold check
        run: |
          COVERAGE=$(mvn jacoco:report | grep -oP '(?<=<lineCoverage>)\d+' | head -1)
          if [ "$COVERAGE" -lt 80 ]; then exit 1; fi

      - name: Build and validate SpringDoc OpenAPI
        run: mvn clean install -DskipTests
```

### Pre-Release Gate

- Integration tests passing (100% pass rate)
- Load test: p99 latency < 500ms for 100 RPS
- API schema validated via SpringDoc
- Database migrations tested on staging

### Pre-Production Gate

- Dependency check: `mvn dependency-check:check` passes
- Secrets validation: no credentials in config files
- Canary deployment to 5% traffic; monitor 15 minutes
- Health endpoint responding < 100ms

## Implementation Risk Notes

### Deployment Risks

**Spring Security misconfiguration:**

- Risk: Authentication bypass if bean not properly wired
- Mitigation: Use `@EnableWebSecurity` + explicit `SecurityFilterChain` bean

**N+1 query problem:**

- Risk: Lazy loading causes database query explosion
- Mitigation: Use `@Transactional(readOnly=true)` + `@EntityGraph` for eager loading

**Connection pool exhaustion:**

- Risk: JDBC connections exhausted under load
- Mitigation: Configure HikariCP pool size correctly (max-pool-size ≤ 20 per instance)

### Performance Impact

- JWT validation: ~20ms (signature check cached)
- Authorization checks: ~5ms (permission lookup)
- Structured logging: ~2ms (JSON serialization)
- **Total:** ~27ms overhead acceptable for enterprise SaaS (p99 <500ms)

### Operational Burden

- **Spring version management:** LTS releases recommended (Spring Boot 3.2 LTS)
- **Configuration management:** Spring Cloud Config for centralized secrets
- **Actuator monitoring:** Dashboard setup for health + metrics endpoints

### Testing Gaps

- Integration test database isolation (tenant separation)
- Load testing with realistic connection pool scenarios
- Spring Security filter chain ordering edge cases

## Control Mapping

| EATGF Control                 | ISO 27001:2022 | NIST SSDF | OWASP ASVS | NIST 800-53 | COBIT 2019 |
| ----------------------------- | -------------- | --------- | ---------- | ----------- | ---------- |
| Spring Security Config        | A.8.9          | PW.8      | V14        | SC-8        | DSS05.04   |
| Authentication (JWT)          | A.8.5          | PW.2      | V2         | IA-2        | DSS05.03   |
| Tenant Isolation              | A.8.21         | PW.1      | V1.2       | AC-3        | APO13.01   |
| Authorization (@PreAuthorize) | A.8.35         | PW.3      | V4         | AC-2        | APO13.02   |
| Dependency Governance         | A.8.28         | PW.4      | V14        | SI-7        | BAI09      |
| Logging & Auditing            | A.8.15         | RV.1      | V15        | AU-2        | MEA01      |
| Rate Limiting                 | A.8.22         | PW.6      | V5         | SC-7        | DSS05.03   |
| Zero Trust (HTTPS/CORS)       | A.8.23         | PW.7      | V1.1       | AC-4        | APO13.03   |

## Developer Checklist

Before production deployment:

- [ ] **Spring Security configured** with explicit `SecurityFilterChain` bean
- [ ] **JWT validation enabled** (no sessions)
- [ ] **@PreAuthorize annotations** on all endpoints
- [ ] **Tenant filtering** in all repository queries
- [ ] **Secrets externalized** (not in source code)
- [ ] **Dependencies locked** in pom.xml / build.gradle with versions
- [ ] **OWASP Dependency Check passes** (HIGH severity)
- [ ] **CORS configured** with whitelist of origins
- [ ] **Structured JSON logging** enabled (Logstash format)
- [ ] **HTTPS enforced** (server.ssl.enabled=true)
- [ ] **Error handling configured** (no stack traces in responses)
- [ ] **Unit test coverage ≥80%** (JaCoCo report)
- [ ] **Integration tests passing** (multi-tenant scenarios)
- [ ] **Load test** completes p99 < 500ms
- [ ] **Spring Boot Actuator health** endpoint responding
- [ ] **SonarQube scan** passes (no critical issues)

**Deployment blocked if any MANDATORY item fails.**

## Governance Implications

### If Not Implemented

**Authentication bypass:**

- Risk: Session cookies or weak JWT validation
- Impact: Account compromise, unauthorized access
- Audit finding: NIST 800-53 IA-2 violation

**SQL injection / N+1 queries:**

- Risk: Unvalidated input in JPA queries, lazy loading explosion
- Impact: Data breach, performance degradation
- Audit finding: OWASP ASVS V5 violation

**Cross-tenant data access:**

- Risk: Query without tenant filtering
- Impact: GDPR violations, contract breach
- Audit finding: ISO 27001 A.8.21 violation

**Supply chain compromise:**

- Risk: Known CVE in transitive Spring dependency
- Impact: RCE, data breach
- Audit finding: NIST SSDF PW.4 violation

**Audit trail loss:**

- Risk: Logs not retained or searchable
- Impact: Forensics failure, compliance violation
- Audit finding: SOC2 Type II failure

**Non-conformance consequences:**

- Audit findings escalate to board level
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
- [Spring Security Documentation](https://spring.io/projects/spring-security)
- [Spring Data JPA Documentation](https://spring.io/projects/spring-data-jpa)
- [Spring Cloud Config Documentation](https://spring.io/projects/spring-cloud-config)

## Version Information

| Field              | Value                                                  |
| ------------------ | ------------------------------------------------------ |
| **Version**        | 1.0                                                    |
| **Release Date**   | 2026-02-15                                             |
| **Change Type**    | Major (First Release)                                  |
| **EATGF Baseline** | v1.0 (Phases 12a-b Complete)                           |
| **Next Review**    | Q2 2026 (Spring Boot 3.3 LTS release)                  |
| **Author**         | EATGF Governance Council                               |
| **Status**         | Ready for Enterprise Deployment                        |
| **Applies To**     | Spring Boot 3.2+ LTS, Java 21 LTS, Spring Security 6.x |
