# Angular Framework Governance Profile

## Enterprise Conformance Model (v1.0)

---

## Authority Notice

**CLASSIFICATION:** Framework Implementation Profile (Cross-Cutting)

**AUTHORITY LAYER:** 08_DEVELOPER_GOVERNANCE_LAYER → FRAMEWORK_PROFILES → FRONTEND

**CONTROL AUTHORITY RELATIONSHIP:**

- This profile **implements** governance controls defined in [02_API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md)
- This profile **references** secure SDLC requirements
- This profile **clarifies** dependency injection, RxJS services, and guard patterns
- This profile **does not** redefine any control from root governance documents

**COMPLIANCE STATEMENT:** This profile enforces security across Angular 15+ applications. Non-conformance impacts:

- Dependency injection attack surface
- Observable/subscription memory leaks
- Guard chain bypass
- Intereceptor security boundary

---

## 1. Purpose & Scope

This document defines governance conformance requirements for Angular applications (v15+) operating under EATGF.

**Scope:** Enterprise SPA, large-scale dashboard applications, administrative portals, framework-heavy applications

---

## 2. Architectural Position

**EATGF Layer Placement:**

```
08_DEVELOPER_GOVERNANCE_LAYER
├── FRAMEWORK_PROFILES
│   └── FRONTEND
│       ├── React (hooks-based)
│       ├── Vue.js (Composition API)
│       └── Angular (dependency injection) ← THIS PROFILE
```

**Angular operates as:**

- Opinionated framework with dependency injection
- Service-based architecture
- RxJS-driven reactivity
- Guard-enforced route protection
- Interceptor middleware chain

**Critical Principle:** Guards and interceptors create security layers. Improper ordering compromises authentication.

---

## 3. Governance Principles

### Principle 1: HTTP Interceptor Chain (MANDATORY)

```typescript
// ❌ PROHIBITED: Multiple fetch calls without interceptor
this.http.get("/api/invoices");
this.http.get("/api/users"); // No auth injection

// ✅ COMPLIANT: Single interceptor chain
@Injectable()
export class AuthInterceptor implements HttpInterceptor {
  constructor(private auth: AuthService) {}

  intercept(
    req: HttpRequest<any>,
    next: HttpHandler,
  ): Observable<HttpEvent<any>> {
    // ✅ Add correlationId to all requests
    const correlatedReq = req.clone({
      setHeaders: {
        "X-Correlation-ID": crypto.randomUUID(),
      },
    });

    return next.handle(correlatedReq).pipe(
      catchError((error: HttpErrorResponse) => {
        if (error.status === 401) {
          // ✅ Handle auth failure centrally
          this.auth.logout();
        }
        return throwError(() => error);
      }),
    );
  }
}

// app.config.ts
providers: [
  {
    provide: HTTP_INTERCEPTORS,
    useClass: AuthInterceptor,
    multi: true,
  },
];
```

### Principle 2: Route Guard Enforcement (MANDATORY)

```typescript
// ✅ COMPLIANT: Auth guard on protected routes
@Injectable({
  providedIn: "root",
})
export class AuthGuard implements CanActivate {
  constructor(
    private auth: AuthService,
    private router: Router,
  ) {}

  canActivate(
    route: ActivatedRouteSnapshot,
    state: RouterStateSnapshot,
  ): Observable<boolean> {
    return this.auth.user$.pipe(
      map((user) => !!user),
      tap((isAuthenticated) => {
        if (!isAuthenticated) {
          this.router.navigate(["/login"]);
        }
      }),
    );
  }
}

// routing.module.ts
routes: [
  {
    path: "dashboard",
    component: DashboardComponent,
    canActivate: [AuthGuard],
  },
];
```

### Principle 3: Service Injection Architecture (MANDATORY)

```typescript
// ✅ COMPLIANT: Centralized auth service
@Injectable({
  providedIn: "root",
})
export class AuthService {
  private userSubject$ = new BehaviorSubject<User | null>(null);
  public user$ = this.userSubject$.asObservable();

  constructor(private http: HttpClient) {
    this.initializeUser();
  }

  private initializeUser(): void {
    this.http.get<User>("/auth/user").subscribe(
      (user) => this.userSubject$.next(user),
      (error) => this.userSubject$.next(null),
    );
  }

  login(email: string, password: string): Observable<User> {
    return this.http
      .post<User>("/auth/login", { email, password })
      .pipe(tap((user) => this.userSubject$.next(user)));
  }
}
```

### Principle 4: RxJS Subscription Management (MANDATORY)

```typescript
// ❌ PROHIBITED: Memory leaks from unmanaged subscriptions
export class InvoiceComponent {
  invoices: Invoice[];

  constructor(private api: ApiService) {
    this.api.getInvoices().subscribe(
      (invoices) => (this.invoices = invoices),
      // No unsubscribe → memory leak
    );
  }
}

// ✅ COMPLIANT: Managed subscriptions with takeUntilDestroyed
export class InvoiceComponent {
  private destroy$ = new Subject<void>();
  public invoices$ = this.api.getInvoices();

  constructor(private api: ApiService) {}

  ngOnInit() {
    this.invoices$
      .pipe(takeUntil(this.destroy$))
      .subscribe((invoices) => console.log(invoices));
  }

  ngOnDestroy() {
    this.destroy$.next();
    this.destroy$.complete();
  }
}
```

### Principle 5: Dependency Injection Security (MANDATORY)

```typescript
// ❌ PROHIBITED: Directly instantiating services
export class InvoiceComponent {
  constructor() {
    const auth = new AuthService(); // ❌ Bypasses DI
  }
}

// ✅ COMPLIANT: DI provides singleton
export class InvoiceComponent {
  constructor(private auth: AuthService) {} // ✅ Managed by Angular
}

// ✅ Providers enforce singleton
providers: [
  {
    provide: AuthService,
    useClass: AuthService,
  },
];
```

### Principle 6: Template Security (MANDATORY)

```typescript
// ❌ PROHIBITED: Unescaped HTML in templates
<div [innerHTML]="userComment"></div>

// ✅ COMPLIANT: Text interpolation (auto-escaped)
<div>{{ userComment }}</div>

// ✅ COMPLIANT: DomSanitizer for HTML
import { DomSanitizer } from '@angular/platform-browser';

constructor(private sanitizer: DomSanitizer) {}

getSafeHtml(html: string) {
  return this.sanitizer.bypassSecurityTrustHtml(
    DOMPurify.sanitize(html)
  );
}
```

### Principle 7: Token Management in AuthService (MANDATORY)

```typescript
// ✅ COMPLIANT: Store tokens in memory, not localStorage
@Injectable({
  providedIn: "root",
})
export class TokenService {
  private token: string | null = null;

  setToken(token: string): void {
    this.token = token;
    // ✅ Server sends HTTP-only cookie
  }

  getToken(): string | null {
    return this.token;
  }

  clearToken(): void {
    this.token = null;
  }
}
```

### Principle 8: AOT Compilation & Build Security (MANDATORY)

```bash
# ✅ Production build enforces security
ng build --configuration production \
  --aot \
  --build-optimizer \
  --sourceMap=false
```

---

## 4. Control 1: Authentication

**Objective:** DI-based auth service with Observable streams.

### Compliant Implementation

```typescript
@Injectable({ providedIn: "root" })
export class AuthService {
  private userSubject$ = new BehaviorSubject<User | null>(null);
  public user$ = this.userSubject$.asObservable();

  constructor(private http: HttpClient) {
    this.restoreSession();
  }

  private restoreSession(): void {
    this.http.get<User>("/auth/user").subscribe(
      (user) => this.userSubject$.next(user),
      () => this.userSubject$.next(null),
    );
  }

  login(email: string, password: string): Observable<User> {
    return this.http
      .post<User>("/auth/login", { email, password })
      .pipe(tap((user) => this.userSubject$.next(user)));
  }

  logout(): void {
    this.http
      .post("/auth/logout", {})
      .subscribe(() => this.userSubject$.next(null));
  }
}
```

---

## 5. Control 2: Authorization

**Objective:** Guard-based authorization enforcement.

### Compliant Implementation

```typescript
@Injectable({ providedIn: "root" })
export class PermissionGuard implements CanActivate {
  constructor(
    private auth: AuthService,
    private http: HttpClient,
    private router: Router,
  ) {}

  canActivate(route: ActivatedRouteSnapshot): Observable<boolean> {
    const requiredAction = route.data["action"];

    return this.http
      .get<{ authorized: boolean }>("/auth/authorize", {
        params: { action: requiredAction },
      })
      .pipe(
        map((res) => res.authorized),
        tap((authorized) => {
          if (!authorized) {
            this.router.navigate(["/forbidden"]);
          }
        }),
      );
  }
}

routes: [
  {
    path: "invoices/:id/delete",
    component: DeleteComponent,
    canActivate: [PermissionGuard],
    data: { action: "delete_invoice" },
  },
];
```

---

## 6. Control 3: Versioning

**Objective:** API version management through interceptor.

### Compliant Implementation

```typescript
@Injectable()
export class VersionInterceptor implements HttpInterceptor {
  private API_VERSION = "v2";

  intercept(
    req: HttpRequest<any>,
    next: HttpHandler,
  ): Observable<HttpEvent<any>> {
    const versionedReq = req.clone({
      url: req.url.replace("/api/", `/api/${this.API_VERSION}/`),
    });

    return next.handle(versionedReq).pipe(
      tap((event) => {
        if (event instanceof HttpResponse) {
          const version = event.headers.get("x-api-version");
          if (version && version !== this.API_VERSION) {
            console.warn(
              `Version mismatch: expected ${this.API_VERSION}, got ${version}`,
            );
          }
        }
      }),
    );
  }
}
```

---

## 7. Control 4: Input Validation

**Objective:** Reactive form validation with schema.

### Compliant Implementation

```typescript
import { z } from "zod";

const InvoiceSchema = z.object({
  amount: z.number().positive(),
  currency: z.enum(["USD", "EUR"]),
});

@Component({})
export class InvoiceFormComponent {
  form = this.fb.group({
    amount: ["", [Validators.required, Validators.min(0)]],
    currency: ["USD", Validators.required],
  });

  onSubmit() {
    try {
      const validated = InvoiceSchema.parse(this.form.value);
      this.api.createInvoice(validated).subscribe();
    } catch (error) {
      if (error instanceof z.ZodError) {
        // Handle validation errors
      }
    }
  }

  constructor(
    private fb: FormBuilder,
    private api: ApiService,
  ) {}
}
```

---

## 8. Control 5: Rate Limiting

**Objective:** Interceptor-based rate limit handling.

### Compliant Implementation

```typescript
@Injectable()
export class RateLimitInterceptor implements HttpInterceptor {
  intercept(
    req: HttpRequest<any>,
    next: HttpHandler,
  ): Observable<HttpEvent<any>> {
    return next.handle(req).pipe(
      catchError((error: HttpErrorResponse) => {
        if (error.status === 429) {
          const retryAfter = parseInt(error.headers.get("retry-after") || "60");

          return timer(retryAfter * 1000).pipe(
            switchMap(() => next.handle(req)),
          );
        }

        return throwError(() => error);
      }),
    );
  }
}
```

---

## 9. Control 6: Testing & Documentation

**Objective:** Jasmine/Karma testing with provider mocking.

### Compliant Implementation

```typescript
describe("AuthService", () => {
  let service: AuthService;
  let httpMock: HttpTestingController;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule],
      providers: [AuthService],
    });

    service = TestBed.inject(AuthService);
    httpMock = TestBed.inject(HttpTestingController);
  });

  it("should fetch user on init", () => {
    service.user$.subscribe((user) => {
      expect(user).toEqual({ id: "user-123" });
    });

    const req = httpMock.expectOne("/auth/user");
    req.flush({ id: "user-123" });
  });
});
```

---

## 10. Control 7: Logging & Observability

**Objective:** Router events and HTTP logging.

### Compliant Implementation

```typescript
@Injectable()
export class LoggingInterceptor implements HttpInterceptor {
  intercept(
    req: HttpRequest<any>,
    next: HttpHandler,
  ): Observable<HttpEvent<any>> {
    const correlationId = crypto.randomUUID();

    const loggedReq = req.clone({
      setHeaders: {
        "X-Correlation-ID": correlationId,
      },
    });

    return next.handle(loggedReq).pipe(
      tap((event) => {
        if (event instanceof HttpResponse) {
          console.log(
            `[${correlationId}] ${req.method} ${req.url} → ${event.status}`,
          );
        }
      }),
    );
  }
}
```

---

## 11. Control 8: Zero Trust Networking

**Objective:** HTTPS enforcement in build configuration.

### Compliant Implementation

```typescript
// angular.json
"serve": {
  "builder": "@angular-devkit/build-angular:dev-server",
  "options": {
    "ssl": true,
    "sslCert": "localhost.crt",
    "sslKey": "localhost.key"
  }
}

// environment.prod.ts
export const environment = {
  production: true,
  apiUrl: 'https://api.example.com'
};
```

---

## 12. Multi-Tenancy Controls

**Objective:** Tenant context in DI service.

### Compliant Implementation

```typescript
@Injectable({ providedIn: "root" })
export class TenantService {
  private tenantSubject$ = new BehaviorSubject<string | null>(null);
  public tenant$ = this.tenantSubject$.asObservable();

  constructor(private auth: AuthService) {
    this.auth.user$.subscribe((user) => {
      this.tenantSubject$.next(user?.tenantId ?? null);
    });
  }

  getTenantId(): string | null {
    return this.tenantSubject$.value;
  }
}
```

---

## 13. Dependency & Supply Chain Governance

### Compliant Implementation

```bash
npm audit --audit-level=high
ng build --configuration production
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

- [ ] HTTP interceptors chained (auth, logging, error handling)
- [ ] Route guards protect all authenticated routes
- [ ] Services provided in root via DI
- [ ] RxJS subscriptions properly unsubscribed (takeUntil/async pipe)
- [ ] HTTP-only cookies used for tokens
- [ ] Templates use text interpolation (not [innerHTML])
- [ ] Reactive forms with validation
- [ ] AOT compilation enabled
- [ ] Source maps disabled in production build
- [ ] npm audit passes
- [ ] 80%+ test coverage

---

## Official References

- Angular Documentation: `https://angular.io/docs`
- Angular Security Guide: `https://angular.io/guide/security`
- OWASP Angular Security: `https://owasp.org/www-community/attacks/Angular_Security`
- NIST SP 800-218: `https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-218.pdf`
- MDN Web Security: `https://developer.mozilla.org/en-US/docs/Web/Security`

---

## 16. Version Information

| Field                | Value             |
| -------------------- | ----------------- |
| **Document Version** | 1.0               |
| **Change Type**      | Major             |
| **Issue Date**       | February 15, 2026 |
| **Angular Version**  | 15+               |
| **Node.js**          | 18+               |

---

**Authorization:** Enterprise Architecture Board
**Last Reviewed:** February 15, 2026
**Next Review:** August 15, 2026
