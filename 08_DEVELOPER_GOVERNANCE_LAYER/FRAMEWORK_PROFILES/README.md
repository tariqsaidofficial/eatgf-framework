# FRAMEWORK_PROFILES

## Architectural Position

- **EATGF Layer:** 08_DEVELOPER_GOVERNANCE_LAYER / Cross-Layer (01, 03, 04, 05)
- **Governance Scope:** Framework Profile Patterns (Implementation, not Control Definition)
- **Control Authority:** Implements controls from multiple layers; never redefines

## Purpose

Framework Profiles translate EATGF governance controls into **technology-specific implementation patterns**. Unlike domain frameworks (Block 2: API Governance), Framework Profiles are **cross-cutting**—each profile implements standards from multiple layers:

- **Layer 01:** Secure SDLC (testing, code review, dependency scanning)
- **Layer 03:** DevSecOps Governance (CI/CD gates, SCA, supply chain)
- **Layer 04:** Cloud Governance (infrastructure, container security)
- **Layer 05:** Domain Frameworks (API, data, integration patterns)

## Structure

```
FRAMEWORK_PROFILES/
├── BACKEND/
│   ├── DJANGO_GOVERNANCE_PROFILE.md
│   ├── FASTAPI_GOVERNANCE_PROFILE.md
│   ├── NESTJS_GOVERNANCE_PROFILE.md
│   └── SPRING_BOOT_GOVERNANCE_PROFILE.md
├── FRONTEND/
│   ├── REACT_GOVERNANCE_PROFILE.md
│   ├── NEXTJS_GOVERNANCE_PROFILE.md
│   └── REACT_NATIVE_GOVERNANCE_PROFILE.md
└── INFRASTRUCTURE/
    ├── DOCKER_GOVERNANCE_PROFILE.md
    ├── KUBERNETES_GOVERNANCE_PROFILE.md
    └── TERRAFORM_GOVERNANCE_PROFILE.md
```

## Authority Notice

Framework Profiles are **implementation clarifications only**. They do NOT:
- Define new controls
- Override control severity/maturity
- Create new framework mappings
- Redefine policy

Framework Profiles reference and implement controls defined in:
- [API_GOVERNANCE_STANDARD.md](../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md) (Layer 05)
- [SECURE_SDLC_STANDARD.md](../01_SECURE_SDLC/SECURE_SDLC_STANDARD.md) (Layer 01)
- Future: DEVSECOPS_GOVERNANCE_STANDARD, CLOUD_GOVERNANCE_STANDARD

## Conformance Model

Each Framework Profile must include:
1. ✅ Title & Authority Notice
2. ✅ Purpose & Architectural Position
3. ✅ Relationship to EATGF Layers
4. ✅ Governance Conformance (8 controls × implementation)
5. ✅ Multi-Tenancy Controls (if applicable)
6. ✅ Dependency & Supply Chain Governance
7. ✅ Logging & Observability Standards
8. ✅ CI/CD Integration Gates
9. ✅ Implementation Risk Notes
10. ✅ Framework-Specific Best Practices
11. ✅ Developer Checklist
12. ✅ Version Information

## Control Implementation Examples

### BACKEND/

**Django Profile** implements:
- Layer 08.02.Control-1 (Authentication) → Django's `authentication_backends`, JWT integration
- Layer 08.02.Control-2 (Authorization) → `django-guardian` RBAC, custom permission checks
- Layer 05.API (Rate Limiting) → `django-ratelimit` decorator-based approach
- Layer 01.SDLC (Dependency Management) → `pip`, `requirements.txt`, `pip-audit` verification

**FastAPI Profile** implements:
- Same Layer 08.02 controls using `FastAPI` decorators + `python-jose` JWT library
- Layer 03.DevSecOps (SAST) → Bandit integration in CI/CD workflow
- Different from Django in: async-first design, built-in OpenAPI validation, `HTTPExceptionhandling`

**NestJS Profile** implements:
- Same Layer 08.02 controls using **TypeScript** + `@nestjs/` libraries
- Layer 04.Cloud (Container) → `Dockerfile` best practices for Node runtime
- Layer 03.DevSecOps (Docker scanning) → Trivy integration for image vulnerability scanning

### FRONTEND/

**React Profile** implements:
- Layer 08.02.Control-1 (Authentication) → `react-jwt`, OAuth2 integration
- Layer 05.Security (CSRF/XSS) → Content Security Policy headers, React's built-in XSS protection
- Layer 01.SDLC (Dependency Auditing) → `npm audit`, dependency-check integration
- Layer 04.Cloud (Static hosting) → CORS configuration for CloudFront, S3 deployment patterns

### INFRASTRUCTURE/

**Docker Profile** implements:
- Layer 04.Container (Security) → Multi-stage builds, non-root users, minimal base images
- Layer 03.DevSecOps (Image Scanning) → Trivy, Grype integration in Build step
- Layer 01.SDLC (SBOM) → CycloneDX/SPDX generation during build

**Kubernetes Profile** implements:
- Layer 04.Kubernetes (Network Policy) → Istio mTLS, Pod admission controllers
- Layer 03.DevSecOps (RBAC) → K8s RBAC for Team isolation, service account scoping
- Layer 05.API (Rate Limiting) → Envoy rate limit servers in service mesh

## Not In FRAMEWORK_PROFILES

- API architecture patterns (REST, GraphQL, gRPC) → Layer 05 / 02_API_GOVERNANCE/PROFILES
- DevSecOps standards (Linux hardening, container rootless) → Layer 03 / 03_DEVSECOPS_GOVERNANCE
- Cloud foundational security (VPC, IAM, encryption) → Layer 04 / 04_CLOUD_GOVERNANCE

---

**Ready for:** Profile creation using Conformance Model template  
**Next Phase:** BACKEND/DJANGO_GOVERNANCE_PROFILE.md (session N+1)  
**Maintenance:** Quarterly reviews to ensure no control redefinition creep
