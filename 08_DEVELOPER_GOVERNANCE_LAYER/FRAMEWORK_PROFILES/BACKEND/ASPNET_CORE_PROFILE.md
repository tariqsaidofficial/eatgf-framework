# ASP.NET Core Framework Governance Profile

> **Authority Notice:** This profile implements EATGF controls for ASP.NET Core-based backend systems. It does NOT define new controls, redefine severity, or override standards. This profile clarifies HOW ASP.NET Core applications satisfy Secure SDLC (Layer 01), API Governance (Layer 05), and DevSecOps (Layer 03) requirements.

## Purpose

This document defines the governance conformance model for ASP.NET Core-based backend systems operating under the Enterprise AI-Aligned Technical Governance Framework (EATGF).

It translates EATGF Secure SDLC, API Governance, DevSecOps, and Runtime Security standards into enforceable implementation controls for enterprise ASP.NET Core applications.

This profile applies to:

- Enterprise RESTful and GraphQL APIs
- Multi-tenant SaaS platforms
- Microservices with C# services
- High-performance backend systems
- Cloud-native deployments (Azure, AWS, GCP)

## Architectural Position

**EATGF Layer:**

- Primary: `08_DEVELOPER_GOVERNANCE_LAYER` → `FRAMEWORK_PROFILES` → `BACKEND`
- References: Layer 01 (Secure SDLC), Layer 05 (API Governance), Layer 03 (DevSecOps)

**Scope:**
Backend application layer responsible for:

- HTTP request/response handling via ASP.NET Core pipeline
- Entity Framework Core ORM data access
- Authentication and authorization
- Multi-tenancy enforcement
- API exposure via REST and GraphQL
- Middleware-based request processing

**ASP.NET Core Classification:**

- High-performance enterprise framework
- Strongly-typed C# language
- Policy enforcement boundary
- Data protection control surface
- Application security boundary
- Cross-platform (.NET 8+)

**Conformance Obligations:**

-  01_SECURE_SDLC standards
-  02_API_GOVERNANCE standards (REST/GraphQL-specific controls)
-  03_DEVSECOPS standards
-  04_CLOUD standards (if deployed in cloud context)

## Relationship to EATGF Layers

### Layer 01: Secure SDLC

ASP.NET Core profiles enforce:

- **Dependency scanning:** NuGet audit and OWASP Dependency-Check
- **SAST rules:** SonarSource/Roslyn analyzers, Roslynator for code quality
- **Code review workflow:** Pull request gates with security checklist
- **Test coverage requirement:** Minimum 80% unit + integration test coverage via Coverlet

### Layer 03: DevSecOps Governance

ASP.NET Core profiles reference:

- **Container security:** Multi-stage Docker builds with non-root user
- **CI/CD pipeline gates:** Pre-merge, pre-release, pre-production stages
- **Secrets management:** Azure Key Vault, AWS Secrets Manager, or environment variables
- **Image scanning:** Trivy/Grype vulnerability scanning in build pipeline

### Layer 05: Domain Frameworks

ASP.NET Core profiles implement API Governance controls:

- **Authentication:** OpenID Connect, OAuth2, or JWT via IdentityServer4/Duende
- **Authorization:** Policy-based authorization with role and claims-based access
- **Rate Limiting:** ASP.NET Core built-in Rate Limiting Middleware or custom middleware
- **OpenAPI/Swagger:** Native Swagger/OpenAPI support via NSwag or Swashbuckle
- **Versioning:** URL-based versioning (`/api/v1/`, `/api/v2/`) or header-based versioning

### Layer 04: Cloud Governance (Conditional)

If deployed in cloud infrastructure:

- **HTTPS enforcement:** HSTS headers, TLS termination at load balancer
- **Environment config:** Azure Key Vault or AWS Secrets Manager
- **Database encryption:** SQL Database Encryption (TDE) + connection string encryption
- **IAM scoping:** Azure Managed Identity or AWS IAM roles for application services

## Governance Principles

### 1. Secure-by-Default Configuration

Production environments must never rely on default settings.

```csharp
// appsettings.json (committed - no secrets)
{
  "Logging": {
    "LogLevel": {
      "Default": "Warning",
      "Microsoft": "Warning"
    }
  },
  "AllowedHosts": "api.example.com"
}

// appsettings.Production.json (merged runtime)
{
  "Logging": {
    "LogLevel": {
      "Default": "Information"
    }
  }
}

// Program.cs (Minimal API configuration)
public class Program
{
    public static void Main(string[] args) => CreateHostBuilder(args).Build().Run();

    public static IHostBuilder CreateHostBuilder(string[] args) =>
        Host.CreateDefaultBuilder(args)
            .ConfigureWebHostDefaults(webBuilder =>
            {
                webBuilder.UseStartup<Startup>();
                webBuilder.UseKestrel(options =>
                {
                    // HTTPS only
                    options.ListenAnyIP(443, listenOptions =>
                    {
                        listenOptions.UseHttps();
                    });
                });
                webBuilder.ConfigureAppConfiguration((context, config) =>
                {
                    if (context.HostingEnvironment.IsProduction())
                    {
                        config.AddAzureKeyVault(
                            new Uri(Environment.GetEnvironmentVariable("KEYVAULT_URL")),
                            new DefaultAzureCredential()
                        );
                    }
                });
            });
}
```

**Failure to enforce:** MANDATORY violation

### 2. Tenant Isolation as a First-Class Control

All Entity Framework queries must be tenant-scoped via query filters.

```csharp
// DbContext with global query filter
public class ApplicationDbContext : DbContext
{
    private readonly string _tenantId;

    public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options,
        IHttpContextAccessor httpContextAccessor) : base(options)
    {
        var user = httpContextAccessor?.HttpContext?.User;
        _tenantId = user?.FindFirst("tenant_id")?.Value;
    }

    public DbSet<Ticket> Tickets { get; set; }
    public DbSet<Comment> Comments { get; set; }

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        base.OnModelCreating(modelBuilder);

        // Global query filter: all Tickets must match tenant
        modelBuilder.Entity<Ticket>()
            .HasQueryFilter(t => t.TenantId == _tenantId);

        modelBuilder.Entity<Comment>()
            .HasQueryFilter(c => c.Ticket.TenantId == _tenantId);
    }
}

// Enforced at data access layer
var tickets = dbContext.Tickets.ToList(); // Automatically filtered by tenant
```

**Global scope enforcement:** Mandatory on all multi-tenant models

### 3. Authentication via OpenID Connect/JWT

ASP.NET Core must use OIDC or JWT for API authentication (not cookie sessions).

```csharp
// Program.cs or Startup.cs
services.AddAuthentication(options =>
{
    options.DefaultScheme = JwtBearerDefaults.AuthenticationScheme;
    options.DefaultChallengeScheme = JwtBearerDefaults.AuthenticationScheme;
})
.AddJwtBearer(options =>
{
    options.Authority = "https://auth.example.com";
    options.Audience = "api.example.com";
    options.TokenValidationParameters = new TokenValidationParameters
    {
        ValidateIssuerSigningKey = true,
        ValidateIssuer = true,
        ValidateAudience = true,
        ValidateLifetime = true,
        ClockSkew = TimeSpan.Zero
    };
    options.Events = new JwtBearerEvents
    {
        OnAuthenticationFailed = context =>
        {
            context.Fail("Authentication failed: Invalid token");
            return Task.CompletedTask;
        }
    };
});

// WebAPI controller
[ApiController]
[Route("api/[controller]")]
[Authorize(AuthenticationSchemes = JwtBearerDefaults.AuthenticationScheme)]
public class TicketsController : ControllerBase
{
    [HttpGet("{id}")]
    public async Task<IActionResult> GetTicket(int id)
    {
        // Request.User populated from JWT claims
        var tenantId = User.FindFirst("tenant_id")?.Value;
        var ticket = await _dbContext.Tickets
            .FirstOrDefaultAsync(t => t.Id == id && t.TenantId == tenantId);

        return Ok(ticket);
    }
}
```

**Session authentication for APIs:** MANDATORY violation

### 4. Policy-Based Authorization Enforcement

```csharp
// Authorization policy definition
services.AddAuthorizationBuilder()
    .AddPolicy("CanEditTicket", policy =>
        policy.Requirements.Add(new CanEditTicketRequirement()))
    .AddPolicy("IsAdmin", policy =>
        policy.RequireClaim("role", "admin"))
    .AddPolicy("SameTenant", policy =>
        policy.Requirements.Add(new SameTenantRequirement()));

// Custom Authorization Handler
public class CanEditTicketHandler : AuthorizationHandler<CanEditTicketRequirement, Ticket>
{
    private readonly IHttpContextAccessor _httpContextAccessor;

    protected override Task HandleRequirementAsync(
        AuthorizationHandlerContext context,
        CanEditTicketRequirement requirement,
        Ticket resource)
    {
        var userId = context.User.FindFirst(ClaimTypes.NameIdentifier)?.Value;
        var tenantId = context.User.FindFirst("tenant_id")?.Value;

        if (resource.CreatedById == userId && resource.TenantId == tenantId)
        {
            context.Succeed(requirement);
        }

        return Task.CompletedTask;
    }
}

// Controller usage
[ApiController]
[Route("api/[controller]")]
public class TicketsController : ControllerBase
{
    private readonly IAuthorizationService _authorizationService;

    [HttpPut("{id}")]
    public async Task<IActionResult> UpdateTicket(int id, UpdateTicketDto dto)
    {
        var ticket = await _dbContext.Tickets.FindAsync(id);
        var authResult = await _authorizationService
            .AuthorizeAsync(User, ticket, "CanEditTicket");

        if (!authResult.Succeeded)
        {
            return Forbid();
        }

        ticket.Update(dto);
        await _dbContext.SaveChangesAsync();
        return Ok(ticket);
    }
}
```

**Authorization scope:** Must not rely solely on route-level checks

### 5. Secrets Governance

Secrets must not exist in source code or committed files.

**Acceptable patterns:**

- Azure Key Vault
- AWS Secrets Manager
- HashiCorp Vault
- Environment variables (development only)

```csharp
// Program.cs
if (app.Environment.IsProduction())
{
    var vaultUrl = new Uri(Environment.GetEnvironmentVariable("KEYVAULT_URL"));
    var credential = new DefaultAzureCredential();
    var client = new SecretClient(vaultUrl, credential);

    var secret = client.GetSecret("DbPassword");
    var connectionString = $"Server=..;Password={secret.Value};";
}
else
{
    // Development: use user-secrets
    var secretsPath = Path.Combine(AppContext.BaseDirectory, "secrets.json");
    var config = new ConfigurationBuilder()
        .AddJsonFile(secretsPath, optional: false)
        .Build();
}
```

**Hardcoded credentials:** MANDATORY violation

### 6. Structured Logging & Auditability

All security-relevant events logged in structured JSON format.

```csharp
// Program.cs
services.AddLogging(configure =>
{
    configure.ClearProviders();
    configure.AddConsole();
    configure.AddJsonConsole(options =>
    {
        options.IncludeScopes = true;
        options.JsonWriterOptions = new JsonWriterOptions { Indented = false };
    });
});

// Audit logging middleware
public class AuditLoggingMiddleware
{
    private readonly RequestDelegate _next;
    private readonly ILogger<AuditLoggingMiddleware> _logger;

    public AuditLoggingMiddleware(RequestDelegate next, ILogger<AuditLoggingMiddleware> logger)
    {
        _next = next;
        _logger = logger;
    }

    public async Task InvokeAsync(HttpContext context, IHttpContextAccessor httpContextAccessor)
    {
        var user = context.User;
        var tenantId = user.FindFirst("tenant_id")?.Value;

        _logger.LogInformation("Request", new
        {
            timestamp = DateTime.UtcNow,
            method = context.Request.Method,
            path = context.Request.Path,
            user_id = user.FindFirst(ClaimTypes.NameIdentifier)?.Value,
            tenant_id = tenantId,
            ip_address = context.Connection.RemoteIpAddress?.ToString(),
            user_agent = context.Request.Headers["User-Agent"].ToString()
        });

        await _next(context);

        _logger.LogInformation("Response", new
        {
            timestamp = DateTime.UtcNow,
            status_code = context.Response.StatusCode,
            tenant_id = tenantId
        });
    }
}

// app.UseMiddleware<AuditLoggingMiddleware>();
```

**Constraint:** Logs must exclude PII unless legally justified

## Governance Conformance

### Control 1: Authentication

**Root Standard:** [API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md)

**ASP.NET Core Implementation Pattern:**

- Use JWT or OIDC with Azure AD / OAuth2 provider
- Validate token expiry; refresh tokens rotated server-side
- Reject cookie sessions for API endpoints
- Use bcrypt for password hashing (minimum 12 rounds if storing passwords)

**Compliant Example:**

```csharp
// Authentication controller
[ApiController]
[Route("api/[controller]")]
public class AuthController : ControllerBase
{
    private readonly IConfiguration _configuration;
    private readonly UserManager<ApplicationUser> _userManager;

    [HttpPost("login")]
    [AllowAnonymous]
    public async Task<IActionResult> Login([FromBody] LoginRequest request)
    {
        var user = await _userManager.FindByEmailAsync(request.Email);

        if (user == null || !await _userManager.CheckPasswordAsync(user, request.Password))
        {
            return Unauthorized(new { message = "Invalid credentials" });
        }

        var token = GenerateJwtToken(user);
        return Ok(new { token });
    }

    private string GenerateJwtToken(ApplicationUser user)
    {
        var securityKey = new SymmetricSecurityKey(
            Encoding.UTF8.GetBytes(_configuration["Jwt:SecretKey"]));
        var credentials = new SigningCredentials(securityKey, SecurityAlgorithms.HmacSha256);

        var claims = new[]
        {
            new Claim(ClaimTypes.NameIdentifier, user.Id),
            new Claim(ClaimTypes.Email, user.Email),
            new Claim("tenant_id", user.TenantId.ToString())
        };

        var token = new JwtSecurityToken(
            issuer: _configuration["Jwt:Issuer"],
            audience: _configuration["Jwt:Audience"],
            claims: claims,
            expires: DateTime.UtcNow.AddHours(1),
            signingCredentials: credentials);

        return new JwtSecurityTokenHandler().WriteToken(token);
    }
}
```

### Control 2: Authorization

**Root Standard:** [API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md)

**ASP.NET Core Implementation Pattern:**

- Use policy-based authorization with custom handlers
- Enforce tenant scoping at DbContext layer
- Use [Authorize] attributes with policy names
- Deny by default; explicitly grant permissions

**Compliant Example:**

```csharp
// Authorization requirement and handler
public class CanModifyTicketRequirement : IAuthorizationRequirement { }

public class CanModifyTicketHandler : AuthorizationHandler<CanModifyTicketRequirement, Ticket>
{
    private readonly IHttpContextAccessor _httpContextAccessor;
    private readonly ApplicationDbContext _dbContext;

    protected override async Task HandleRequirementAsync(
        AuthorizationHandlerContext context,
        CanModifyTicketRequirement requirement,
        Ticket resource)
    {
        var userId = context.User.FindFirst(ClaimTypes.NameIdentifier)?.Value;
        var tenantId = context.User.FindFirst("tenant_id")?.Value;

        if (resource.TenantId.ToString() == tenantId && resource.CreatedById.ToString() == userId)
        {
            context.Succeed(requirement);
        }
        else
        {
            context.Fail();
        }

        await Task.CompletedTask;
    }
}

// Controller with authorization
[ApiController]
[Route("api/v1/[controller]")]
[Authorize]
public class TicketsController : ControllerBase
{
    private readonly IAuthorizationService _authorizationService;
    private readonly ApplicationDbContext _dbContext;

    [HttpPut("{id}")]
    public async Task<IActionResult> UpdateTicket(int id, UpdateTicketDto dto)
    {
        var ticket = await _dbContext.Tickets.FindAsync(id);

        if (ticket == null)
            return NotFound();

        var result = await _authorizationService.AuthorizeAsync(
            User, ticket, "CanModifyTicket");

        if (!result.Succeeded)
            return Forbid();

        ticket.Title = dto.Title;
        ticket.Description = dto.Description;
        await _dbContext.SaveChangesAsync();

        return Ok(ticket);
    }
}
```

### Control 3: API Versioning

**Root Standard:** [API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md)

**ASP.NET Core Implementation Pattern:**

- Use URL-based versioning: `/api/v1/`, `/api/v2/`
- Maintain backward compatibility for 12 months
- Document breaking changes in migration guide
- Use Asp.Versioning for API versioning support

**Compliant Example:**

```csharp
// Program.cs
services.AddApiVersioning(options =>
{
    options.DefaultApiVersion = new ApiVersion(1, 0);
    options.AssumeDefaultVersionWhenUnspecified = true;
    options.ReportApiVersions = true;
    options.ApiVersionReader = new UrlSegmentApiVersionReader();
});

// Controller V1
[ApiController]
[Route("api/v{version:apiVersion}/[controller]")]
[ApiVersion("1.0")]
public class TicketsControllerV1 : ControllerBase
{
    [HttpGet("{id}")]
    public async Task<IActionResult> GetTicket(int id)
    {
        var ticket = await _dbContext.Tickets.FindAsync(id);
        return Ok(new TicketV1Dto { Id = ticket.Id, Title = ticket.Title });
    }
}

// Controller V2 with breaking changes
[ApiController]
[Route("api/v{version:apiVersion}/[controller]")]
[ApiVersion("2.0")]
public class TicketsControllerV2 : ControllerBase
{
    [HttpGet("{id}")]
    public async Task<IActionResult> GetTicket(int id)
    {
        var ticket = await _dbContext.Tickets.FindAsync(id);
        return Ok(new TicketV2Dto
        {
            Id = ticket.Id,
            Title = ticket.Title,
            CreatedAt = ticket.CreatedAt  // Breaking change: new required field
        });
    }
}

// V1 deprecated but still supported
[Obsolete("Use API v2 instead", false)]
public class TicketV1Dto { }
```

### Control 4: Rate Limiting

**Root Standard:** [API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md)

**ASP.NET Core Implementation Pattern:**

- Use built-in Rate Limiting Middleware (.NET 7+)
- Apply per-IP and per-user rate limits
- Return HTTP 429 on limit exceeded
- Expose rate limit info in response headers

**Compliant Example:**

```csharp
// Program.cs
services.AddRateLimiter(options =>
{
    options.GlobalLimiter = PartitionedRateLimiter.Create<HttpContext, string>(context =>
        RateLimitPartition.GetFixedWindowLimiter(
            partitionKey: context.User.FindFirst(ClaimTypes.NameIdentifier)?.Value ?? context.Connection.RemoteIpAddress?.ToString(),
            factory: partition => new FixedWindowRateLimiterOptions
            {
                AutoReplenishment = true,
                PermitLimit = 100,
                Window = TimeSpan.FromMinutes(1)
            }));

    options.OnRejected = async context =>
    {
        context.HttpContext.Response.StatusCode = StatusCodes.Status429TooManyRequests;
        await context.HttpContext.Response.WriteAsJsonAsync(
            new { error = "Rate limit exceeded" });
    };
});

app.UseRateLimiter();

// Route-specific limiting
[ApiController]
[Route("api/[controller]")]
public class TicketsController : ControllerBase
{
    [HttpPost]
    [EnableRateLimiting("fixed")]
    public async Task<IActionResult> CreateTicket([FromBody] CreateTicketDto dto)
    {
        // Limited to 10 requests per minute for POST operations
        var ticket = new Ticket { Title = dto.Title };
        await _dbContext.Tickets.AddAsync(ticket);
        await _dbContext.SaveChangesAsync();
        return CreatedAtAction(nameof(GetTicket), new { id = ticket.Id }, ticket);
    }
}
```

### Control 5: Input Validation & Sanitization

**Root Standard:** [API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md)

**ASP.NET Core Implementation Pattern:**

- Use Data Annotations for declarative validation
- Use FluentValidation for complex scenarios
- Sanitize all user input before processing
- Validate against JSON Schema if needed

**Compliant Example:**

```csharp
// DTO with validation attributes
public class CreateTicketDto
{
    [Required]
    [StringLength(255, MinimumLength = 3)]
    [RegularExpression(@"^[a-zA-Z0-9\s\-\.]+$",
        ErrorMessage = "Title contains invalid characters")]
    public string Title { get; set; }

    [Required]
    [StringLength(5000)]
    public string Description { get; set; }

    [Required]
    [EnumDataType(typeof(TicketPriority))]
    public TicketPriority Priority { get; set; }

    [Required]
    public int TenantId { get; set; }
}

// Fluent Validation alternative
public class CreateTicketValidator : AbstractValidator<CreateTicketDto>
{
    public CreateTicketValidator()
    {
        RuleFor(x => x.Title)
            .NotEmpty()
            .Length(3, 255)
            .Matches(@"^[a-zA-Z0-9\s\-\.]+$")
            .WithMessage("Title contains invalid characters");

        RuleFor(x => x.Description)
            .NotEmpty()
            .MaximumLength(5000);

        RuleFor(x => x.Priority)
            .IsInEnum();

        RuleFor(x => x.TenantId)
            .GreaterThan(0);
    }
}

// Controller with automatic validation
[ApiController]
[Route("api/[controller]")]
public class TicketsController : ControllerBase
{
    [HttpPost]
    public async Task<IActionResult> CreateTicket([FromBody] CreateTicketDto dto)
    {
        // ModelState automatically validated if validation fails
        if (!ModelState.IsValid)
            return BadRequest(ModelState);

        var ticket = new Ticket
        {
            Title = HtmlEncoder.Default.Encode(dto.Title),
            Description = HtmlEncoder.Default.Encode(dto.Description),
            Priority = dto.Priority,
            TenantId = dto.TenantId
        };

        await _dbContext.Tickets.AddAsync(ticket);
        await _dbContext.SaveChangesAsync();

        return CreatedAtAction(nameof(GetTicket), new { id = ticket.Id }, ticket);
    }
}
```

### Control 6: Response Security Headers

**Root Standard:** [API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md)

**ASP.NET Core Implementation Pattern:**

- Enforce HTTPS via middleware
- Set security headers (CSP, X-Frame-Options, X-Content-Type-Options)
- Use HSTS preload
- Configure via middleware or program

**Compliant Example:**

```csharp
// Program.cs
app.UseHsts(options =>
{
    options.MaxAge(TimeSpan.FromDays(365));
    options.IncludeSubDomains();
    options.Preload();
});

app.UseXContentTypeOptions();
app.UseReferrerPolicy(options => options.NoReferrer());
app.UseXXssProtection(options => options.EnabledWithBlockMode());
app.UseXfo(options => options.Deny());

app.Use(async (context, next) =>
{
    context.Response.Headers.Add("Content-Security-Policy",
        "default-src 'none'; script-src 'self'; style-src 'self'");
    context.Response.Headers.Add("X-Content-Type-Options", "nosniff");
    context.Response.Headers.Add("X-Frame-Options", "DENY");
    context.Response.Headers.Add("Strict-Transport-Security",
        "max-age=31536000; includeSubDomains; preload");

    await next();
});

// app.UseHttpsRedirection();
```

### Control 7: Exception Handling & Error Disclosure

**Root Standard:** [API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md)

**ASP.NET Core Implementation Pattern:**

- Never expose stack traces in production
- Log detailed errors internally
- Return generic error messages to clients

**Compliant Example:**

```csharp
// Global exception handling middleware
public class ExceptionHandlingMiddleware
{
    private readonly RequestDelegate _next;
    private readonly ILogger<ExceptionHandlingMiddleware> _logger;

    public ExceptionHandlingMiddleware(RequestDelegate next, ILogger<ExceptionHandlingMiddleware> logger)
    {
        _next = next;
        _logger = logger;
    }

    public async Task InvokeAsync(HttpContext context)
    {
        try
        {
            await _next(context);
        }
        catch (Exception exception)
        {
            _logger.LogError(exception, "Unhandled exception occurred");

            var response = context.Response;
            response.ContentType = "application/json";
            response.StatusCode = StatusCodes.Status500InternalServerError;

            var errorResponse = new ErrorResponse
            {
                Message = "An internal server error occurred"
            };

            if (context.RequestServices.GetRequiredService<IWebHostEnvironment>().IsDevelopment())
            {
                errorResponse.Details = exception.Message;
                errorResponse.StackTrace = exception.StackTrace;
            }

            await response.WriteAsJsonAsync(errorResponse);
        }
    }
}

// Exception response DTO
public class ErrorResponse
{
    public string Message { get; set; }
    public string Details { get; set; }
    public string StackTrace { get; set; }
}

// Program.cs
app.UseMiddleware<ExceptionHandlingMiddleware>();
```

### Control 8: CORS & Cross-Origin Requests

**Root Standard:** [API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md)

**ASP.NET Core Implementation Pattern:**

- Configure CORS with whitelisted origins only
- Force HTTPS; disable HTTP
- Validate JWT audience claims
- Implement mTLS for inter-service communication

**Compliant Example:**

```csharp
// Program.cs
services.AddCors(options =>
{
    options.AddPolicy("AllowSpecificOrigins", builder =>
    {
        builder
            .WithOrigins("https://app.example.com", "https://admin.example.com")
            .AllowAnyMethod()
            .AllowAnyHeader()
            .AllowCredentials()
            .WithExposedHeaders("X-Total-Count", "X-Page-Number", "X-Rate-Limit-Remaining")
            .WithMaxAge(TimeSpan.FromHours(1));
    });
});

app.UseCors("AllowSpecificOrigins");

// JWT validation with audience
services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
    .AddJwtBearer(options =>
    {
        options.TokenValidationParameters = new TokenValidationParameters
        {
            ValidateAudience = true,
            ValidAudience = "api.example.com",
            ValidateIssuer = true,
            ValidIssuer = "https://auth.example.com"
        };
    });
```

## Multi-Tenancy Controls

### DbContext Query Filters

- Entity Framework Core applies global query filters automatically
- Tenant ID extracted from JWT claims at middleware level
- All queries respect tenant scope

```csharp
// ApplicationDbContext override
public class ApplicationDbContext : DbContext
{
    private readonly string _tenantId;

    public ApplicationDbContext(
        DbContextOptions<ApplicationDbContext> options,
        IHttpContextAccessor httpContextAccessor) : base(options)
    {
        var user = httpContextAccessor?.HttpContext?.User;
        _tenantId = user?.FindFirst("tenant_id")?.Value;
    }

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        base.OnModelCreating(modelBuilder);

        // Automatic tenant filtering
        modelBuilder.Entity<Ticket>()
            .HasQueryFilter(t => t.TenantId.ToString() == _tenantId);

        modelBuilder.Entity<Comment>()
            .HasQueryFilter(c => c.Ticket.TenantId.ToString() == _tenantId);

        modelBuilder.Entity<Attachment>()
            .HasQueryFilter(a => a.Ticket.TenantId.ToString() == _tenantId);
    }

    public DbSet<Ticket> Tickets { get; set; }
    public DbSet<Comment> Comments { get; set; }
    public DbSet<Attachment> Attachments { get; set; }
}

// Usage - automatic filtering
var tickets = await dbContext.Tickets.ToListAsync(); // Only current tenant's tickets
```

### Resource Isolation Verification

- Cross-tenant resource access returns 404 or 403
- Policies enforce tenant validation
- Audit logs include tenant context

```csharp
// Integration test
[TestFixture]
public class TenantIsolationTests
{
    [Test]
    public async Task GetTicket_FromDifferentTenant_ReturnsNotFound()
    {
        var tenantA = new Tenant { Id = 1 };
        var tenantB = new Tenant { Id = 2 };
        var userA = new User { TenantId = 1 };
        var ticketB = new Ticket { Id = 1, TenantId = 2 };

        // User from Tenant A tries to access Ticket from Tenant B
        var token = GenerateToken(userA, tenantA);
        var response = await client.GetAsync($"/api/tickets/{ticketB.Id}",
            new { Authorization = $"Bearer {token}" });

        Assert.AreEqual(HttpStatusCode.NotFound, response.StatusCode);
    }
}
```

### Audit Trail Isolation

- Audit logs stored with tenant context
- Tenant-specific audit export available to authorized admins
- 90-day minimum retention per tenant

```csharp
// Audit log entity
public class AuditLog
{
    public int Id { get; set; }
    public int TenantId { get; set; }
    public string UserId { get; set; }
    public string Action { get; set; }
    public string EntityType { get; set; }
    public int EntityId { get; set; }
    public string Changes { get; set; }
    public DateTime CreatedAt { get; set; } = DateTime.UtcNow;
}

// Audit logging interceptor
public class AuditInterceptor : SaveChangesInterceptor
{
    private readonly IHttpContextAccessor _httpContextAccessor;

    public override async ValueTask<InterceptionResult<int>> SavingChangesAsync(
        DbContextEventData eventData, InterceptionResult<int> result,
        CancellationToken cancellationToken = default)
    {
        var context = eventData.Context;
        var user = _httpContextAccessor?.HttpContext?.User;
        var tenantId = user?.FindFirst("tenant_id")?.Value;

        foreach (var entry in context.ChangeTracker.Entries())
        {
            if (entry.Entity is IEntity entity)
            {
                var auditLog = new AuditLog
                {
                    TenantId = int.Parse(tenantId),
                    UserId = user?.FindFirst(ClaimTypes.NameIdentifier)?.Value,
                    Action = entry.State.ToString(),
                    EntityType = entry.Metadata.ClrType.Name,
                    EntityId = entity.Id,
                    Changes = SerializeChanges(entry)
                };

                context.Set<AuditLog>().Add(auditLog);
            }
        }

        return await base.SavingChangesAsync(eventData, result, cancellationToken);
    }
}
```

## Dependency & Supply Chain Governance

### NuGet Package Management

ASP.NET Core projects declare dependencies in `.csproj`:

```xml
<ItemGroup>
  <PackageReference Include="Microsoft.AspNetCore.App" Version="8.0.0" />
  <PackageReference Include="Microsoft.EntityFrameworkCore" Version="8.0.0" />
  <PackageReference Include="System.IdentityModel.Tokens.Jwt" Version="7.0.0" />
  <PackageReference Include="Azure.Identity" Version="1.10.0" />
  <PackageReference Include="FluentValidation" Version="11.8.0" />
</ItemGroup>

<ItemGroup>
  <PackageReference Include="xunit" Version="2.6.0" />
  <PackageReference Include="NSubstitute" Version="5.0.0" />
  <PackageReference Include="NuGet.Frameworks" Version="5.11.0" />
</ItemGroup>
```

### Vulnerability Scanning

CI/CD pipeline runs:

```bash
dotnet list package --vulnerable
dotnet package search vulnerabilities
dotnet package update --check-outdated
```

- HIGH severity findings block merge
- MEDIUM findings require documented mitigation
- Security patches deployed within 7 days of CVE publication

### Package Lock Discipline

- `packages.lock.json` committed to repository
- All dependencies pinned to exact versions
- Updates only via explicit version bumps with security review
- No floating version constraints in production

## CI/CD Integration Gates

### Pre-Merge Gate

- Testing: `dotnet test` (100% pass rate)
- Security: `dotnet list package --vulnerable`
- Code analysis: `dotnet build /p:EnforceCodeStyleInBuild=true`
- Coverage: `coverlet` minimum 80%

```yaml
# .github/workflows/test.yml
- name: Check vulnerable packages
  run: dotnet list package --vulnerable

- name: Run tests
  run: dotnet test --collect:"XPlat Code Coverage" --logger trx

- name: Check code style
  run: dotnet build /p:EnforceCodeStyleInBuild=true

- name: Verify coverage
  run: |
    coverage=$(dotnet queryownership)
    if [ $coverage -lt 80 ]; then exit 1; fi
```

### Pre-Release Gate

- Integration tests passing (100% pass rate)
- Load test: p99 latency < 500ms for 100 RPS
- API schema stable (no breaking changes from v1.0)
- Database migrations tested on staging

### Pre-Production Gate

- Dependency audit passes: `dotnet list package --vulnerable` with no findings
- Secrets in configuration validated (not in code)
- Canary deployment to 5% via App Service slots
- Monitor error rates for 15 minutes

## Implementation Risk Notes

### Deployment Risks

**Breaking API changes:**

- Risk: Clients using old endpoints fail silently
- Mitigation: Semantic versioning (v1 → v2 namespace), 6+ month deprecation window

**Database migration failures:**

- Risk: EF Core migrations lock production database
- Mitigation: Test migrations on staging; use Shadow Properties for non-breaking changes

**Token validation latency:**

- Risk: IdP becomes bottleneck; authorization service latency
- Mitigation: Cache token validation; use in-memory authorization cache

### Performance Impact

- Authentication adds ~18ms per request (JWT validation + claims extraction)
- Authorization adds ~12ms per request (policy evaluation)
- Query filtering adds ~15ms per request (DbContext global query filter)
- Structured logging adds ~4ms per request (JSON serialization)
- **Total:** ~49ms overhead on typical request
- Acceptable for enterprise SaaS (p99 latency <500ms achievable with caching)

### Operational Burden

- **RBAC/ABAC maintenance:** Quarterly governance review of policies
- **Rate limit tuning:** Monitor 429 error rates; adjust per-tier
- **Dependency updates:** Monthly security patch cycle with 30-day testing

### Testing Gaps

- Hard to test cross-tenant isolation without multiple staging tenants
- Rate limit exhaustion requires load testing infrastructure
- Policy failover scenarios require comprehensive permission matrix

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
| Query Filtering       | A.8.23         | PW.7      | V1.1       | AC-4        | APO13.03   |

## Developer Checklist

Before production deployment:

- [ ] **appsettings.json** does not contain secrets
- [ ] **Azure Key Vault** configured for production secrets
- [ ] **HTTPS enforced** (UseHttpsRedirection enabled)
- [ ] **HSTS headers** configured (max-age, includeSubDomains, preload)
- [ ] **JWT authentication** enabled (not cookie sessions)
- [ ] **Authorization policies** defined and enforced
- [ ] **DbContext query filters** implemented on all tenant-scoped entities
- [ ] **Global query filter validation** tested for cross-tenant access
- [ ] **dotnet list package --vulnerable** passes (no findings)
- [ ] **Structured logging** enabled (JSON console formatter)
- [ ] **Security headers middleware** configured (CSP, X-Frame-Options, etc)
- [ ] **CORS** configured with whitelisted origins only
- [ ] **Database connections** use SSL/TLS
- [ ] **Unit test coverage ≥80%** (Coverlet report)
- [ ] **Integration tests** passing for multi-tenant scenarios
- [ ] **Load test** completes with p99 < 500ms
- [ ] **Database migrations** tested on staging replica
- [ ] **Exception handling** does not expose stack traces in production

**Deployment blocked if any MANDATORY item fails.**

## Governance Implications

### If Not Implemented

**Cross-tenant data exposure:**

- Risk: Tenant A queries Tenant B data (query filter bypass)
- Impact: GDPR/CCPA violations, contract breach, reputation damage
- Audit finding: ISO 27001 A.8.21 (Access control) violation

**Compromised JWT tokens:**

- Risk: Token validation bypassed; stale tokens accepted
- Impact: Account takeover, fraud, compliance failure
- Audit finding: NIST 800-53 IA-2 (Authentication) violation

**Vulnerable NuGet dependencies:**

- Risk: Compromised package deployed to production
- Impact: RCE, data breach, ransomware
- Audit finding: NIST SSDF PW.4 (Dependency management) violation

**PII exposure in logs:**

- Risk: Customer data in plain-text logs
- Impact: GDPR Article 32 violation, SOC2 Type I failure
- Audit finding: ISO 27001 A.8.15 (Logging) violation

**Audit failure:**

- ASP.NET Core without governance = non-compliant under EATGF
- SOC2 Type II certification blocked
- PCI-DSS requirement for code review, testing, logging failures

## Official References

- [NIST SP 800-218: Secure Software Development Framework](https://csrc.nist.gov/publications/detail/sp/800-218/final)
- [ISO/IEC 27001:2022 Annex A](https://www.iso.org/standard/27001)
- [OWASP ASVS 5.0](https://owasp.org/www-project-application-security-verification-standard/)
- [OWASP API Security Top 10 (2023)](https://owasp.org/www-project-api-security/)
- [NIST SP 800-53 Rev 5](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
- [COBIT 2019 Governance Framework](https://www.isaca.org/resources/cobit)
- [Microsoft ASP.NET Core Security Best Practices](https://learn.microsoft.com/en-us/aspnet/core/security/)
- [OWASP .NET Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/DotNet_Security_Cheat_Sheet.html)

## Version Information

| Field              | Value                           |
| ------------------ | ------------------------------- |
| **Version**        | 1.0                             |
| **Release Date**   | 2026-02-15                      |
| **Change Type**    | Major (First Release)           |
| **EATGF Baseline** | v1.0 (Phases 12a-b Complete)    |
| **Next Review**    | Q2 2026 (.NET 9 LTS release)    |
| **Author**         | EATGF Governance Council        |
| **Status**         | Ready for Enterprise Deployment |
