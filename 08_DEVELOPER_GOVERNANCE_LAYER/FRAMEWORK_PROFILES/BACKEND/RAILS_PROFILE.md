# Ruby on Rails Framework Governance Profile

> **Authority Notice:** This profile implements EATGF controls for Ruby on Rails-based backend systems. It does NOT define new controls, redefine severity, or override standards. This profile clarifies HOW Rails applications satisfy Secure SDLC (Layer 01), API Governance (Layer 05), and DevSecOps (Layer 03) requirements.

## Purpose

This document defines the governance conformance model for Ruby on Rails-based backend systems operating under the Enterprise AI-Aligned Technical Governance Framework (EATGF).

It translates EATGF Secure SDLC, API Governance, DevSecOps, and Runtime Security standards into enforceable implementation controls for enterprise Rails applications.

This profile applies to:

- Enterprise web applications and APIs
- Multi-tenant SaaS platforms
- Microservices with Rails services
- GraphQL and REST API backends
- Rails on cloud platforms (Heroku, AWS, GCP)

## Architectural Position

**EATGF Layer:**

- Primary: `08_DEVELOPER_GOVERNANCE_LAYER` → `FRAMEWORK_PROFILES` → `BACKEND`
- References: Layer 01 (Secure SDLC), Layer 05 (API Governance), Layer 03 (DevSecOps)

**Scope:**
Backend application layer responsible for:

- HTTP request/response handling via Action Pack
- ActiveRecord ORM data access
- Authentication and authorization
- Multi-tenancy enforcement via middleware
- API exposure via Rails/GraphQL
- Session and token management

**Rails Classification:**

- Convention-over-configuration Ruby framework
- Policy enforcement boundary
- Data protection control surface
- Application security boundary
- MVC architectural pattern

**Conformance Obligations:**

-  01_SECURE_SDLC standards
-  02_API_GOVERNANCE standards (REST/GraphQL-specific controls)
-  03_DEVSECOPS standards
-  04_CLOUD standards (if deployed in cloud context)

## Relationship to EATGF Layers

### Layer 01: Secure SDLC

Rails profiles enforce:

- **Dependency scanning:** Bundler Audit, Brakeman for Rails security issues
- **SAST rules:** Brakeman with custom security rules in CI/CD pipeline
- **Code review workflow:** GitHub PR-based gate with security checklist
- **Test coverage requirement:** Minimum 80% unit + integration test coverage via SimpleCov

### Layer 03: DevSecOps Governance

Rails profiles reference:

- **Container security:** Docker multi-stage builds with minimal Ruby image
- **CI/CD pipeline gates:** Pre-merge, pre-release, pre-production stages
- **Secrets management:** Rails credentials (encrypted) or AWS Secrets Manager
- **Image scanning:** Trivy/Grype vulnerability scanning in build pipeline

### Layer 05: Domain Frameworks

Rails profiles implement API Governance controls:

- **Authentication:** JWT via `jwt` gem or Devise for sessions + tokens
- **Authorization:** Pundit for policy-based authorization
- **Rate Limiting:** Rack-attack or Turnstile for per-IP and per-user enforcement
- **OpenAPI/Swagger:** Automated schema generation via Rails OpenAPI/JSONAPI
- **Versioning:** URL-based or header-based API versioning (`/api/v1/`, `/api/v2/`)

### Layer 04: Cloud Governance (Conditional)

If deployed in cloud infrastructure:

- **HTTPS enforcement:** Forced redirect via Rails config
- **Environment config:** Rails credentials encryption, environment-specific secrets
- **Database encryption:** RDS encryption at rest + TLS in transit
- **IAM scoping:** Service-specific IAM roles for Rails deployments

## Governance Principles

### 1. Secure-by-Default Configuration

Production environments must never rely on default settings.

```ruby
# config/environments/production.rb
Rails.application.configure do
  config.force_ssl = true
  config.ssl_options = { redirect: { status: 308 } }
  config.x.security.hsts_max_age = 63072000 # 2 years
  config.x.security.hsts_include_subdomains = true
  config.x.security.hsts_preload = true

  config.session_store :cookie_store, key: '_app_session',
    secure: !Rails.env.development?,
    httponly: true,
    same_site: :strict

  config.action_mailer.delivery_method = :smtp
  config.action_mailer.smtp_settings = {
    host: ENV.fetch('SMTP_HOST'),
    port: ENV.fetch('SMTP_PORT'),
    authentication: 'plain',
    enable_starttls_auto: true,
  }
end
```

**Failure to enforce:** MANDATORY violation

### 2. Tenant Isolation as a First-Class Control

All ActiveRecord queries must be tenant-scoped via default scopes.

```ruby
# app/models/application_record.rb
class ApplicationRecord < ActiveRecord::Base
  primary_abstract_class

  default_scope { where(tenant_id: Current.tenant_id) if Current.tenant_id.present? }

  validates :tenant_id, presence: true
end

# app/models/ticket.rb
class Ticket < ApplicationRecord
  belongs_to :tenant
  belongs_to :user
  has_many :comments, dependent: :destroy

  # Global scope is automatically applied
end

# Used in Current context
class Current < ActiveSupport::CurrentAttributes
  attribute :user, :tenant_id
end
```

**Global scope enforcement:** Mandatory on all multi-tenant models

### 3. Authentication via JWT for APIs

Rails must use JWT for APIs (not session-based authentication).

```ruby
# Gemfile
gem 'jwt'
gem 'devise'

# config/jwt.rb
JWT_SECRET = ENV.fetch('JWT_SECRET_KEY')
JWT_ALGORITHM = 'HS256'
JWT_EXPIRATION = 3600 # 1 hour

# app/controllers/concerns/authenticable.rb
module Authenticable
  extend ActiveSupport::Concern

  included do
    before_action :authenticate_request!, except: [:login, :create]
  end

  private

  def authenticate_request!
    token = extract_token_from_request
    raise UnauthorizedException unless token

    decoded = decode_token(token)
    @current_user = User.find(decoded['user_id'])
  rescue => e
    raise UnauthorizedException, e.message
  end

  def extract_token_from_request
    header = request.headers['Authorization']
    header.split(' ').last if header&.match?(/^Bearer\s/)
  end

  def decode_token(token)
    JWT.decode(token, JWT_SECRET, true, algorithm: JWT_ALGORITHM).first
  rescue JWT::ExpiredSignature
    raise UnauthorizedException, 'Token has expired'
  rescue JWT::DecodeError
    raise UnauthorizedException, 'Invalid token'
  end
end

# app/controllers/api/v1/auth_controller.rb
class Api::V1::AuthController < ApplicationController
  def login
    user = User.find_by(email: params[:email])

    if user&.authenticate(params[:password])
      token = generate_token(user)
      render json: { token: token, user_id: user.id }
    else
      render json: { error: 'Unauthorized' }, status: :unauthorized
    end
  end

  private

  def generate_token(user)
    payload = { user_id: user.id, tenant_id: user.tenant_id, exp: 1.hour.from_now.to_i }
    JWT.encode(payload, JWT_SECRET, JWT_ALGORITHM)
  end
end
```

**Session authentication for APIs:** MANDATORY violation

### 4. Pundit Policy-Based Authorization Enforcement

```ruby
# Gemfile
gem 'pundit'

# app/policies/application_policy.rb
class ApplicationPolicy
  attr_reader :user, :record

  def initialize(user, record)
    @user = user
    @record = record
  end

  def index?
    user.present? && same_tenant?
  end

  def show?
    user.present? && same_tenant?
  end

  def create?
    user.present? && user.can?('create_records') && same_tenant?
  end

  def update?
    user.present? && user.can?('update_records') && same_tenant? && owner?
  end

  def destroy?
    user.present? && user.can?('delete_records') && same_tenant? && owner?
  end

  private

  def same_tenant?
    record.tenant_id == user.tenant_id
  end

  def owner?
    record.user_id == user.id
  end
end

# app/policies/ticket_policy.rb
class TicketPolicy < ApplicationPolicy
  def reply?
    user.present? && same_tenant? && user.can?('reply_tickets')
  end
end

# app/controllers/api/v1/tickets_controller.rb
class Api::V1::TicketsController < ApplicationController
  include Pundit::Authorization

  after_action :verify_authorized

  def update
    @ticket = Ticket.find(params[:id])
    authorize @ticket

    if @ticket.update(ticket_params)
      render json: @ticket
    else
      render json: { errors: @ticket.errors }, status: :unprocessable_entity
    end
  end

  private

  def ticket_params
    params.require(:ticket).permit(:title, :description, :priority)
  end
end
```

**Authorization scope:** Must not rely solely on middleware checks

### 5. Secrets Governance

Secrets must not exist in source code or committed files.

**Acceptable patterns:**

- Rails credentials (encrypted)
- AWS Secrets Manager
- HashiCorp Vault
- GCP Secret Manager

```ruby
# config/credentials.yml.enc (encrypted)
# Use: rails credentials:edit

# config/initializers/secrets.rb
module Secrets
  def self.database_password
    Rails.application.credentials.database_password || ENV['DB_PASSWORD']
  end

  def self.jwt_secret_key
    Rails.application.credentials.jwt_secret_key || ENV['JWT_SECRET_KEY']
  end

  def self.api_key
    AWS::SecretsManager.get_secret_value(
      secret_id: 'myapp/api_key'
    )
  rescue => e
    Rails.logger.error("Failed to retrieve secret: #{e.message}")
    nil
  end
end
```

**Hardcoded credentials:** MANDATORY violation

### 6. Structured Logging & Auditability

All security-relevant events logged in structured JSON format.

```ruby
# Gemfile
gem 'jsonapi-serializer'
gem 'logstash-event'
gem 'logstash-logger'

# config/initializers/logging.rb
Rails.application.config.log_formatter = proc do |severity, datetime, progname, msg|
  timestamp = datetime.strftime("%Y-%m-%dT%H:%M:%S.%LZ")

  if msg.is_a?(Hash)
    msg.merge(timestamp: timestamp, severity: severity, progname: progname).to_json
  else
    JSON.generate({ timestamp: timestamp, severity: severity, message: msg })
  end
end

if Rails.env.production?
  logger = LogstashLogger.new("udp://#{ENV['LOGSTASH_HOST']}:#{ENV['LOGSTASH_PORT']}")
  Rails.logger = logger
end

# app/models/audit_log.rb
class AuditLog < ApplicationRecord
  belongs_to :user
  belongs_to :tenant

  def self.log_action(action:, model_class:, record_id:, changes: nil)
    create!(
      tenant_id: Current.tenant_id,
      user_id: Current.user&.id,
      action: action,
      model_class: model_class,
      record_id: record_id,
      changes: changes&.to_json,
      ip_address: request.ip,
      user_agent: request.user_agent
    )

    Rails.logger.info({
      event: 'audit',
      action: action,
      model: model_class,
      record_id: record_id,
      tenant_id: Current.tenant_id,
      user_id: Current.user&.id,
      ip: request.ip
    })
  end
end

# Use in model callbacks
class Ticket < ApplicationRecord
  after_update :log_update

  private

  def log_update
    AuditLog.log_action(
      action: 'updated',
      model_class: self.class.name,
      record_id: self.id,
      changes: saved_changes
    )
  end
end
```

**Constraint:** Logs must exclude PII unless legally justified

## Governance Conformance

### Control 1: Authentication

**Root Standard:** [API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md)

**Rails Implementation Pattern:**

- Use JWT via `jwt` gem for API authentication
- Validate token expiry; refresh tokens rotated server-side
- Reject sessions for stateless API endpoints
- Use bcrypt for password hashing (13+ rounds)

**Compliant Example:**

```ruby
# app/models/user.rb
class User < ApplicationRecord
  has_secure_password

  def generate_auth_token
    payload = {
      user_id: id,
      tenant_id: tenant_id,
      exp: 1.hour.from_now.to_i
    }
    JWT.encode(payload, Secrets.jwt_secret_key, 'HS256')
  end
end

# routes/api.rb
namespace :api do
  namespace :v1 do
    post '/login', to: 'auth#login'
    post '/refresh', to: 'auth#refresh'
  end
end

# app/controllers/api/v1/auth_controller.rb
class Api::V1::AuthController < ApplicationController
  def login
    user = User.find_by(email: params[:email])

    if user&.authenticate(params[:password])
      render json: { token: user.generate_auth_token }
    else
      render json: { error: 'Invalid credentials' }, status: :unauthorized
    end
  end
end
```

**Non-Compliant Example:**

```ruby
#  Session authentication for API
def login
  if user = User.authenticate(params[:email], params[:password])
    session[:user_id] = user.id  # Wrong for APIs
    redirect_to root_url
  end
end
```

### Control 2: Authorization

**Root Standard:** [API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md)

**Rails Implementation Pattern:**

- Use Pundit for resource-level authorization checks
- Enforce tenant scoping at model layer via default_scope
- Use Rails policies decorators
- Deny by default; explicitly grant permissions

**Compliant Example:**

```ruby
# app/models/ticket.rb
class Ticket < ApplicationRecord
  belongs_to :tenant
  belongs_to :user

  validates :tenant_id, presence: true
end

# app/policies/ticket_policy.rb
class TicketPolicy < ApplicationPolicy
  def update?
    same_tenant? && (owner? || admin?)
  end

  private

  def same_tenant?
    record.tenant_id == user.tenant_id
  end

  def owner?
    record.user_id == user.id
  end

  def admin?
    user.admin?
  end
end

# app/controllers/api/v1/tickets_controller.rb
class Api::V1::TicketsController < ApplicationController
  include Pundit::Authorization

  before_action :authenticate_request!
  after_action :verify_authorized

  def update
    @ticket = Ticket.find(params[:id])
    authorize @ticket, :update?

    if @ticket.update(ticket_params)
      render json: @ticket
    else
      render json: { errors: @ticket.errors }, status: :unprocessable_entity
    end
  end
end
```

### Control 3: API Versioning

**Root Standard:** [API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md)

**Rails Implementation Pattern:**

- Use URL-based versioning: `/api/v1/`, `/api/v2/`
- Maintain backward compatibility for 12 months
- Document breaking changes in migration guide
- Use namespace in routes

**Compliant Example:**

```ruby
# config/routes.rb
namespace :api do
  namespace :v1 do
    resources :tickets
  end

  namespace :v2 do
    resources :tickets
  end
end

# app/controllers/api/v1/tickets_controller.rb
class Api::V1::TicketsController < ApplicationController
  def index
    @tickets = Ticket.page(params[:page]).per(20)
    render json: @tickets
  end
end

# app/controllers/api/v2/tickets_controller.rb
class Api::V2::TicketsController < ApplicationController
  def index
    # Breaking change: returns paginated results with metadata
    render json: {
      data: Ticket.page(params[:page]).per(25),
      meta: { page: params[:page], total: Ticket.count }
    }
  end
end
```

### Control 4: Rate Limiting

**Root Standard:** [API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md)

**Rails Implementation Pattern:**

- Use Rack::Attack middleware for rate limiting
- Apply per-IP and per-user rate limits
- Return HTTP 429 on limit exceeded
- Expose rate limit info in response headers

**Compliant Example:**

```ruby
# Gemfile
gem 'rack-attack'

# config/initializers/rack_attack.rb
class Rack::Attack
  Rack::Attack.cache.store = ActiveSupport::Cache::RedisCacheStore.new

  throttle('api/ip', limit: 300, period: 1.hour) do |req|
    req.ip if req.path.start_with?('/api/')
  end

  throttle('api/user', limit: 1000, period: 1.hour) do |req|
    if req.path.start_with?('/api/')
      # Rate limit by user ID if authenticated
      req.env['REMOTE_USER'] if req.env['REMOTE_USER']
    end
  end

  self.throttled_response = lambda do |env|
    [429, { 'Content-Type' => 'application/json' }, [
      { error: 'Rate limit exceeded' }.to_json
    ]]
  end
end

# config/middleware.rb
Rails.application.config.middleware.use Rack::Attack
```

### Control 5: Input Validation & Sanitization

**Root Standard:** [API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md)

**Rails Implementation Pattern:**

- Use Active Model validations
- Sanitize input via Rails helpers
- Validate against JSON schema for complex payloads
- Reject invalid MIME types

**Compliant Example:**

```ruby
# app/models/ticket.rb
class Ticket < ApplicationRecord
  validates :title, presence: true, length: { minimum: 3, maximum: 255 },
            format: { with: /\A[a-zA-Z0-9\s\-\.]+\z/, message: 'contains invalid characters' }
  validates :description, presence: true, length: { maximum: 5000 }
  validates :priority, presence: true, inclusion: { in: %w(low medium high critical) }
  validates :tenant_id, presence: true, numericality: { only_integer: true }

  sanitize_attributes :title, :description
end

# spec/support/json_schema/ticket_schema.json
{
  "type": "object",
  "properties": {
    "title": { "type": "string", "max_length": 255 },
    "description": { "type": "string", "max_length": 5000 },
    "priority": { "enum": ["low", "medium", "high", "critical"] }
  },
  "required": ["title", "description", "priority"]
}

# app/controllers/api/v1/tickets_controller.rb
class Api::V1::TicketsController < ApplicationController
  def create
    @ticket = Ticket.new(ticket_params)

    if @ticket.valid? && validate_json_schema(@ticket)
      @ticket.save!
      render json: @ticket, status: :created
    else
      render json: { errors: @ticket.errors }, status: :unprocessable_entity
    end
  end

  private

  def ticket_params
    params.require(:ticket).permit(:title, :description, :priority)
  end
end
```

### Control 6: Response Security Headers

**Root Standard:** [API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md)

**Rails Implementation Pattern:**

- Enforce HTTPS via middleware
- Set security headers (CSP, X-Frame-Options, X-Content-Type-Options)
- Use Rails built-in headers or middleware

**Compliant Example:**

```ruby
# config/initializers/headers.rb
module ActionDispatch
  class FrameOptions
    DEFAULT_HEADER_VALUE = "DENY"
  end
end

# config/environments/production.rb
Rails.application.configure do
  config.force_ssl = true

  # Strict-Transport-Security
  config.ssl_options = {
    redirect: { status: 308 },
    hsts: { expires_in: 1.year, include_subdomains: true, preload: true }
  }

  # Content-Security-Policy
  config.content_security_policy do |policy|
    policy.default_src :none
    policy.script_src :self
    policy.style_src :self
    policy.img_src :self
  end

  # X-Frame-Options
  config.action_dispatch.default_headers = {
    'X-Frame-Options' => 'DENY',
    'X-Content-Type-Options' => 'nosniff',
    'X-XSS-Protection' => '1; mode=block',
    'Referrer-Policy' => 'no-referrer'
  }
end

# app/middleware/security_headers.rb
class SecurityHeaders
  def initialize(app)
    @app = app
  end

  def call(env)
    status, headers, body = @app.call(env)

    headers['X-Content-Type-Options'] = 'nosniff'
    headers['X-Frame-Options'] = 'DENY'
    headers['X-XSS-Protection'] = '1; mode=block'
    headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    headers['Referrer-Policy'] = 'no-referrer'

    [status, headers, body]
  end
end

# config/application.rb
config.middleware.insert_before ActionDispatch::PublicExceptions, SecurityHeaders
```

### Control 7: Exception Handling & Error Disclosure

**Root Standard:** [API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md)

**Rails Implementation Pattern:**

- Never expose stack traces in production
- Log detailed errors internally
- Return generic error messages to clients

**Compliant Example:**

```ruby
# app/controllers/application_controller.rb
class ApplicationController < ActionController::API
  rescue_from StandardError, with: :handle_exception
  rescue_from ActiveRecord::RecordNotFound, with: :record_not_found
  rescue_from Pundit::NotAuthorizedError, with: :user_not_authorized

  private

  def handle_exception(exception)
    Rails.logger.error({
      event: 'exception',
      error_class: exception.class,
      message: exception.message,
      backtrace: exception.backtrace,
      tenant_id: Current.tenant_id,
      user_id: Current.user&.id
    })

    if Rails.env.production?
      render json: { error: 'Internal server error' }, status: :internal_server_error
    else
      render json: { error: exception.message, backtrace: exception.backtrace }, status: :internal_server_error
    end
  end

  def record_not_found(exception)
    render json: { error: 'Resource not found' }, status: :not_found
  end

  def user_not_authorized(exception)
    render json: { error: 'Forbidden' }, status: :forbidden
  end
end
```

### Control 8: CORS & Cross-Origin Requests

**Root Standard:** [API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md)

**Rails Implementation Pattern:**

- Implement CORS via rack-cors gem
- Whitelist only trusted origins
- Force HTTPS
- Support credentials only for same-origin requests

**Compliant Example:**

```ruby
# Gemfile
gem 'rack-cors'

# config/initializers/cors.rb
Rails.application.config.middleware.insert_before 0, Rack::Cors do
  allow do
    origins 'app.example.com', 'admin.example.com'
    resource '*',
      headers: :any,
      methods: [:get, :post, :put, :patch, :delete],
      credentials: true,
      max_age: 3600,
      expose: ['X-Total-Count', 'X-Page-Number']
  end
end

# Secure by default - all other origins rejected
```

## Multi-Tenancy Controls

### Current Context Management

- Rails 6.1+ provides `ActiveSupport::CurrentAttributes` for request context
- Tenant ID automatically included via middleware
- All queries respect tenant scope

```ruby
# app/models/current.rb
class Current < ActiveSupport::CurrentAttributes
  attribute :user, :tenant_id, :request_id
end

# app/middleware/tenant_middleware.rb
class TenantMiddleware
  def initialize(app)
    @app = app
  end

  def call(env)
    Current.request_id = env['HTTP_X_REQUEST_ID'] || SecureRandom.uuid

    if env['REMOTE_USER']
      user = User.find(env['REMOTE_USER'])
      Current.user = user
      Current.tenant_id = user.tenant_id
    end

    @app.call(env)
  ensure
    Current.reset
  end
end

# config/application.rb
config.middleware.use TenantMiddleware
```

### Resource Isolation Verification

- Every ApplicationRecord uses default_scope to filter by tenant
- Cross-tenant resource access returns 403 Forbidden
- Policies include tenant validation

```ruby
# spec/requests/api/v1/tickets_spec.rb
require 'rails_helper'

RSpec.describe 'Api::V1::Tickets', type: :request do
  it 'prevents cross-tenant access' do
    tenant_a = create(:tenant)
    tenant_b = create(:tenant)
    user_a = create(:user, tenant: tenant_a)
    ticket_b = create(:ticket, tenant: tenant_b)

    headers = { Authorization: "Bearer #{user_a.generate_auth_token}" }
    get "/api/v1/tickets/#{ticket_b.id}", headers: headers

    expect(response).to have_http_status(:not_found)
  end
end
```

### Audit Trail Isolation

- Audit logs include tenant_id for all operations
- Tenant-specific audit export available only to tenant admins
- Compliance audit trails stored separately per tenant with 90-day minimum retention

```ruby
# app/models/audit_log.rb
class AuditLog < ApplicationRecord
  belongs_to :tenant
  belongs_to :user, optional: true

  scope :for_tenant, ->(tenant_id) { where(tenant_id: tenant_id) }
  scope :recent, -> { where('created_at >= ?', 90.days.ago) }

  def self.export_for_tenant(tenant_id)
    for_tenant(tenant_id).recent.to_csv
  end
end

# app/controllers/admin/audit_logs_controller.rb
class Admin::AuditLogsController < ApplicationController
  def export
    authorize_admin!

    csv = AuditLog.export_for_tenant(Current.tenant_id)
    send_data csv, filename: "audit_#{Date.today}.csv"
  end
end
```

## Dependency & Supply Chain Governance

### Dependency Declaration

Rails projects declare dependencies in `Gemfile`:

```ruby
# Gemfile
ruby '3.3.0'

source 'https://rubygems.org'

gem 'rails', '~> 7.1.0'
gem 'pg', '~> 1.5'
gem 'puma', '~> 6.0'
gem 'devise'
gem 'pundit'
gem 'jwt'
gem 'rack-attack'
gem 'rack-cors'

group :development, :test do
  gem 'rspec-rails'
  gem 'bundler-audit'
  gem 'brakeman'
  gem 'simplecov'
end
```

### Vulnerability Scanning

CI/CD pipeline runs:

```bash
bundle audit check --update
brakeman -q -z
bundle exec rspec --coverage
```

- HIGH severity findings block merge
- MEDIUM findings require documented mitigation
- Security patches deployed within 7 days of CVE publication

### Bundler Lock Discipline

- `Gemfile.lock` committed to repository
- All dependencies pinned to exact versions
- Updates only via `bundle update` with security review
- No dynamic version constraints in production

## CI/CD Integration Gates

### Pre-Merge Gate

- Testing: `rspec` (100% pass rate required)
- Security: `bundler-audit` and `brakeman`
- Code quality: Rubocop linting
- Coverage: SimpleCov minimum 80%

```yaml
# .github/workflows/test.yml
- name: Run security audit
  run: bundle audit check --update

- name: Run brakeman
  run: brakeman -q -z

- name: Run tests
  run: bundle exec rspec --coverage

- name: Check code style
  run: bundle exec rubocop
```

### Pre-Release Gate

- Integration tests passing (100% pass rate)
- Load test: p99 latency < 500ms for 100 RPS
- API schema stable (no breaking changes from v1.0)
- Database migrations tested on staging

### Pre-Production Gate

- Dependency audit passes: `bundler-audit` with no HIGH findings
- Secrets in production config validated (not in code)
- Canary deployment to 5% traffic
- Monitor error rates for 15 minutes

## Implementation Risk Notes

### Deployment Risks

**Breaking API changes:**

- Risk: Clients using old endpoints fail silently
- Mitigation: Semantic versioning (v1 → v2 separate namespace), 6+ month deprecation window

**Database migration failures:**

- Risk: Locks production database during upgrade with long-running migrations
- Mitigation: Zero-downtime migrations, test on staging replica, automated rollback

**JWT validation latency:**

- Risk: Token validation adds per-request overhead
- Mitigation: Cache token validation; use Redis for token blacklisting

### Performance Impact

- Authentication adds ~12ms per request (JWT validation)
- Authorization (Pundit policy) adds ~8ms per request
- Structured logging adds ~3ms per request (JSON serialization)
- **Total:** ~23ms overhead on typical request
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

- [ ] **Rails.env.production?** enforces `force_ssl = true`
- [ ] **SECRET_KEY_BASE** sourced from secure vault (not code)
- [ ] **Database credentials** use AWS Secrets Manager or vault
- [ ] **HTTPS enforced** (force_ssl and HSTS headers)
- [ ] **JWT authentication** enabled for API endpoints (not sessions)
- [ ] **Pundit policies** defined for all authorization checks
- [ ] **Default scopes** implemented on all multi-tenant models
- [ ] **Gemfile.lock** committed to repository
- [ ] **bundler-audit** passes (no HIGH findings)
- [ ] **brakeman** security scan passes
- [ ] **Security headers middleware** configured
- [ ] **CORS** configured with whitelisted origins only
- [ ] **Database connections** use SSL/TLS
- [ ] **Unit test coverage ≥80%** (SimpleCov report)
- [ ] **Integration tests** passing for multi-tenant scenarios
- [ ] **Load test** completes with p99 < 500ms
- [ ] **Database migrations** tested on staging replica
- [ ] **Error handling** does not expose stack traces in production

**Deployment blocked if any MANDATORY item fails.**

## Governance Implications

### If Not Implemented

**Cross-tenant data exposure:**

- Risk: Tenant A queries Tenant B data (default_scope bypass)
- Impact: GDPR/CCPA violations, contract breach, reputation damage
- Audit finding: ISO 27001 A.8.21 (Access control) violation

**Compromised JWT tokens:**

- Risk: Token validation bypassed; session hijacking
- Impact: Account takeover, fraud, compliance failure
- Audit finding: NIST 800-53 IA-2 (Authentication) violation

**Vulnerable gems:**

- Risk: Compromised gem dependency deployed to production
- Impact: RCE, data breach, ransomware
- Audit finding: NIST SSDF PW.4 (Dependency management) violation

**PII exposure in logs:**

- Risk: Customer data in plain-text logs
- Impact: GDPR Article 32 violation, SOC2 Type I failure
- Audit finding: ISO 27001 A.8.15 (Logging) violation

**Audit failure:**

- Rails without governance = non-compliant under EATGF
- SOC2 Type II certification blocked
- PCI-DSS requirement for code review, testing, logging failures

## Official References

- [NIST SP 800-218: Secure Software Development Framework](https://csrc.nist.gov/publications/detail/sp/800-218/final)
- [ISO/IEC 27001:2022 Annex A](https://www.iso.org/standard/27001)
- [OWASP ASVS 5.0](https://owasp.org/www-project-application-security-verification-standard/)
- [OWASP API Security Top 10 (2023)](https://owasp.org/www-project-api-security/)
- [NIST SP 800-53 Rev 5](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
- [COBIT 2019 Governance Framework](https://www.isaca.org/resources/cobit)
- [Ruby on Rails Security Guide](https://guides.rubyonrails.org/security.html)
- [OWASP Ruby on Rails Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Ruby_on_Rails_Cheat_Sheet.html)

## Version Information

| Field              | Value                           |
| ------------------ | ------------------------------- |
| **Version**        | 1.0                             |
| **Release Date**   | 2026-02-15                      |
| **Change Type**    | Major (First Release)           |
| **EATGF Baseline** | v1.0 (Phases 12a-b Complete)    |
| **Next Review**    | Q2 2026 (Rails 8.0 LTS release) |
| **Author**         | EATGF Governance Council        |
| **Status**         | Ready for Enterprise Deployment |
