# gRPC & Protocol Buffers Governance Profile

> **Authority Notice:** This document implements the controls defined in API_GOVERNANCE_STANDARD.md. It does not introduce new governance controls.

## Profile Description

Enterprise AI-Aligned Technical Governance Framework (EATGF)
Version: 1.0
Layer: 08_DEVELOPER_GOVERNANCE_LAYER → 02_API_GOVERNANCE
Profile Type: gRPC/Protocol Buffers Architecture Implementation
Status: Authoritative Implementation Profile

## Purpose

Define enforceable governance standards for gRPC services and Protocol Buffers schemas within enterprise, SaaS, startup, and developer environments.

This profile operationalizes the [API_GOVERNANCE_STANDARD.md](../API_GOVERNANCE_STANDARD.md) specifically for gRPC-based systems and ensures:

- Protocol buffer schema versioning and backward compatibility
- mTLS mandatory for service-to-service communication
- Service method authorization at handler level
- Streaming security (bidirectional, client, server streams)
- Deployment gating before production release
- Binary protocol integrity and tamper detection

**This is an enforcement profile, not a gRPC tutorial.**

## Architectural Position

- **Parent Standard:** [API_GOVERNANCE_STANDARD.md](../API_GOVERNANCE_STANDARD.md)
- **Enforcement Model:** [API_ENFORCEMENT_MATRIX.md](../API_ENFORCEMENT_MATRIX.md)
- **Mapping Authority:** [API_CONTROL_MAPPING_APPENDIX.md](../API_CONTROL_MAPPING_APPENDIX.md)
- **Layer:** 08_DEVELOPER_GOVERNANCE_LAYER / 02_API_GOVERNANCE
- **Control Authority Relationship:** Implements root standard controls using gRPC patterns

**Applies to:**

- Microservice-to-microservice communication
- High-performance internal APIs
- Service mesh (Istio, Linkerd) integration
- Real-time bidirectional streams
- Data pipeline systems

**Mandatory for all gRPC production services.**

## Governance Principles

- **Schema Versioning:** Proto files versioned semantically; backward compatibility enforced
- **mTLS Mandatory:** All service-to-service communication encrypted with mutual TLS
- **Handler Authorization:** Every RPC method validates user/service identity and permissions
- **Stream Security:** Client, server, and bidirectional streams must authenticate per message
- **Backward Compatibility:** New fields must be optional; old clients must not break
- **Metadata Propagation:** Trace context propagated across service boundaries
- **Deployment Gating:** Deployment without governance validation gates is non-compliant

## gRPC & Protocol Buffers Governance Requirements

### 1. Protocol Buffer Schema Versioning (MANDATORY)

**Proto files must follow semantic versioning:**

```protobuf
// user.proto
// Version: 1.0.0 (MAJOR.MINOR.PATCH)
// Deprecated: false

syntax = "proto3";

package user.v1;

option go_package = "github.com/company/user/v1";

message User {
  string id = 1;              // Required (key)
  string name = 2;            // Required
  string email = 3;           // Required
  int32 age = 4;              // Optional (added in v1.1.0)
  repeated string roles = 5;  // Optional (added in v1.2.0)

  reserved 6, 7, 8;  // Never reuse these field numbers
}
```

**Breaking Change Examples (Prohibited):**

```protobuf
// BREAKING: Removing field
// v1.0.0
message User {
  string id = 1;
  string email = 2;
}

// v1.1.0 (WRONG! This is breaking)
message User {
  string id = 1;
  // removed: string email = 2;  # BREAKS old clients
}

// CORRECT: Deprecate instead
message User {
  string id = 1;
  string email = 2 [deprecated = true];  // v2.0.0+ can remove
}
```

**Example (Backward-Compatible Addition):**

```protobuf
// v1.0.0
message CreateUserRequest {
  string name = 1;
  string email = 2;
}

// v1.1.0 (Backward-compatible)
message CreateUserRequest {
  string name = 1;
  string email = 2;
  string phone = 3;  // New optional field; old clients ignored
  repeated string roles = 4;  // New optional array
}

// v2.0.0 (Breaking - major version bump)
message CreateUserRequest {
  string name = 1;
  // Removed: string email = 2; (breaking change)
  string phone = 3;
}
```

**Mitigation:**

- All proto changes reviewed against breaking change checklist
- Removed fields marked `reserved` to prevent reuse
- Deprecated fields carry `[deprecated = true]`
- Multiple API versions coexist (v1.0 and v2.0 can run simultaneously)

### 2. Mutual TLS (mTLS) (MANDATORY)

**All service-to-service communication must use mTLS:**

```yaml
# Istio ServiceEntry for enforcing mTLS
apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
metadata:
  name: default
spec:
  mtls:
    mode: STRICT # Require mTLS for all traffic

---
apiVersion: networking.istio.io/v1alpha3
kind: DestinationRule
metadata:
  name: tls-required
spec:
  host: "*.svc.cluster.local"
  trafficPolicy:
    tls:
      mode: ISTIO_MUTUAL # mTLS enforced by Istio
```

**Example (Go gRPC with mTLS):**

```go
// Server: Load certificates and require client cert
certs, err := tls.LoadX509KeyPair("server.crt", "server.key")
clientCAs, err := ioutil.ReadFile("client-ca.crt")
certPool := x509.NewCertPool()
certPool.AppendCertsFromPEM(clientCAs)

tlsConfig := &tls.Config{
  Certificates: []tls.Certificate{certs},
  ClientAuth:   tls.RequireAndVerifyClientCert,  // Require client certs
  ClientCAs:    certPool,
}

listener, err := tls.Listen("tcp", ":50051", tlsConfig)
grpcServer := grpc.NewServer(
  grpc.Creds(credentials.NewTLS(tlsConfig)),
)

// Client: Use mutual TLS
certs, err := tls.LoadX509KeyPair("client.crt", "client.key")
caCert, err := ioutil.ReadFile("ca.crt")
caCertPool := x509.NewCertPool()
caCertPool.AppendCertsFromPEM(caCert)

tlsConfig := &tls.Config{
  Certificates: []tls.Certificate{certs},
  RootCAs:      caCertPool,
}

conn, err := grpc.Dial(
  "user-service:50051",
  grpc.WithTransportCredentials(credentials.NewTLS(tlsConfig)),
)
client := user.NewUserServiceClient(conn)
```

### 3. Handler Authorization (MANDATORY)

**Every RPC method must authorize callers:**

```protobuf
service UserService {
  // Requires "admin" role
  rpc CreateUser(CreateUserRequest) returns (User);

  // Requires "viewer" role
  rpc GetUser(GetUserRequest) returns (User);

  // Requires "self" or "admin" role
  rpc UpdateUser(UpdateUserRequest) returns (User);
}
```

**Example (Go handler with authorization):**

```go
func (s *UserService) GetUser(ctx context.Context, req *GetUserRequest) (*User, error) {
  // 1. Extract identity from mTLS
  peerInfo, ok := peer.FromContext(ctx)
  if !ok {
    return nil, status.Error(codes.Unauthenticated, "mTLS required")
  }

  tlsInfo := peerInfo.AuthInfo.(credentials.TLSInfo)
  clientSubject := tlsInfo.State.VerifiedChains[0][0].Subject.CommonName

  // 2. Decode JWT from metadata (if additional auth needed)
  md, ok := metadata.FromIncomingContext(ctx)
  if !ok {
    return nil, status.Error(codes.Unauthenticated, "Metadata missing")
  }

  tokens := md.Get("authorization")
  if len(tokens) == 0 {
    return nil, status.Error(codes.Unauthenticated, "Token missing")
  }

  user, err := verifyToken(tokens[0])
  if err != nil {
    return nil, status.Error(codes.Unauthenticated, "Invalid token")
  }

  // 3. Authorize user can access this resource
  targetUser, err := db.GetUser(req.UserId)
  if targetUser.TenantId != user.TenantId {
    return nil, status.Error(codes.PermissionDenied, "Forbidden")
  }

  return targetUser, nil
}
```

### 4. Streaming Security (MANDATORY)

**Client, server, and bidirectional streams must secure each message:**

```protobuf
// Server streaming: Server sends multiple User responses
service UserService {
  rpc ListUsers(ListUsersRequest) returns (stream User);

  // Client streaming: Client sends multiple CreateUserRequest
  rpc BatchCreateUsers(stream CreateUserRequest) returns (BatchCreateUserResponse);

  // Bidirectional streaming
  rpc StreamUserUpdates(stream UserUpdate) returns (stream UserUpdateResponse);
}
```

**Example (Secure bidirectional stream):**

```go
func (s *UserService) StreamUserUpdates(stream UserService_StreamUserUpdatesServer) error {
  ctx := stream.Context()

  // 1. Authenticate caller (once at stream start)
  user, err := s.authenticateStream(ctx)
  if err != nil {
    return status.Error(codes.Unauthenticated, "Auth failed")
  }

  // 2. Rate limit stream messages
  limiter := rate.NewLimiter(rate.Limit(100), 10)  // 100/sec, burst 10

  for {
    // 3. Receive client message
    clientMsg, err := stream.Recv()
    if err == io.EOF {
      return nil
    }
    if err != nil {
      return err
    }

    // 4. Rate limiting
    if !limiter.Allow() {
      return status.Error(codes.ResourceExhausted, "Rate limited")
    }

    // 5. Authorize each message
    if clientMsg.UserId != user.Id && !user.IsAdmin {
      return status.Error(codes.PermissionDenied, "Cannot update other users")
    }

    // 6. Process and send response
    updatedUser, err := s.updateUser(clientMsg)
    if err != nil {
      return status.Error(codes.Internal, "Update failed")
    }

    stream.Send(&UserUpdateResponse{User: updatedUser})
  }
}
```

### 5. Metadata Propagation (MANDATORY)

**Trace context must propagate across service boundaries:**

```go
// Service A calls Service B
ctx := context.Background()

// Add trace context to outgoing metadata
correlationId := uuid.New().String()
ctx = metadata.AppendToOutgoingContext(ctx,
  "x-correlation-id", correlationId,
  "x-trace-id", traceId,
  "x-user-id", userId,
  "authorization", bearerToken,
)

// Call downstream service
client := NewDownstreamServiceClient(conn)
resp, err := client.DoSomething(ctx, &Request{})

// Service B extracts context
md, _ := metadata.FromIncomingContext(ctx)
correlationId := md.Get("x-correlation-id")[0]
userId := md.Get("x-user-id")[0]

// Log with context
logger.Info("Request received", map[string]interface{}{
  "correlation_id": correlationId,
  "user_id": userId,
  "service": "service-b",
})
```

### 6. Service Mesh Integration (RECOMMENDED for Enterprise)

**Istio/Linkerd enforce security policies:**

```yaml
# Enforce mTLS between services
apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
metadata:
  name: default-mtls
spec:
  mtls:
    mode: STRICT

---
# Define service-to-service authorization
apiVersion: security.istio.io/v1beta1
kind: AuthorizationPolicy
metadata:
  name: user-service-authz
spec:
  rules:
    - from:
        - source:
            principals: ["cluster.local/ns/default/sa/order-service"]
      to:
        - operation:
            methods: ["GetUser"]
            paths: ["/user.v1.UserService/GetUser"]
```

### 7. Logging & Observability (MANDATORY)

**Must log all RPC invocations:**

```json
{
  "timestamp": "2024-01-15T10:30:45Z",
  "correlation_id": "uuid",
  "caller_service": "order-service",
  "called_service": "user-service",
  "method": "/user.v1.UserService/GetUser",
  "grpc_code": "OK",
  "duration_ms": 45,
  "message_count": 1,
  "error": null
}
```

**Example (Go interceptor logging):**

```go
func loggingUnaryInterceptor(ctx context.Context, req interface{}, info *grpc.UnaryServerInfo, handler grpc.UnaryHandler) (interface{}, error) {
  start := time.Now()

  // Get caller service from mTLS cert
  peerInfo, _ := peer.FromContext(ctx)
  tlsInfo := peerInfo.AuthInfo.(credentials.TLSInfo)
  callerService := tlsInfo.State.VerifiedChains[0][0].Subject.CommonName

  resp, err := handler(ctx, req)

  duration := time.Since(start)
  code := codes.OK
  if err != nil {
    code = status.Code(err)
  }

  logger.Info(map[string]interface{}{
    "caller": callerService,
    "method": info.FullMethod,
    "code": code.String(),
    "duration_ms": duration.Milliseconds(),
  })

  return resp, err
}
```

## Severity Model

| Control                   | Severity    | Enforcement       |
| ------------------------- | ----------- | ----------------- |
| **mTLS**                  | MANDATORY   | BLOCKS deployment |
| **Handler Authorization** | MANDATORY   | BLOCKS deployment |
| **Schema Versioning**     | MANDATORY   | BLOCKS deployment |
| **Streaming Security**    | MANDATORY   | BLOCKS deployment |
| **Metadata Propagation**  | MANDATORY   | BLOCKS deployment |
| **Service Mesh**          | RECOMMENDED | Warning logged    |
| **Logging**               | MANDATORY   | BLOCKS deployment |

## Developer Checklist

Before submitting gRPC service for deployment:

- [ ] **Proto Schema:** Semantic versioning enforced; no breaking changes without major bump
- [ ] **mTLS:** Certificates loaded; client cert verification enabled
- [ ] **Handler Auth:** Every method validates caller identity and permissions
- [ ] **Streaming:** Client/server/bidirectional streams rate-limited and authorized
- [ ] **Metadata:** Trace context propagated (correlation ID, user ID, etc.)
- [ ] **Logging:** JSON structured logs with method name, caller, duration
- [ ] **Backward Compatibility:** Old proto versions supported during migration
- [ ] **CI/CD Gates:** Proto linting passed; breaking change detection passed

**Deployment without checklist completion is non-compliant.**

## Governance Implications

### Risk If Not Enforced

- **Service Impersonation:** Without mTLS, any service can call any other service
- **Data Breach:** Missing handler auth allows unauthorized data access
- **Breaking Changes:** Proto schema changes break dependent services without warning
- **Audit Gap:** Missing metadata makes incident investigation impossible

### Operational Impact

- **Developers:** 1-2 weeks to implement mTLS and auth per service
- **DevOps:** Service mesh configuration and certificate management
- **Security:** Monitor unauthorized service-to-service calls

## Official References

- **Root Authority:** [API_GOVERNANCE_STANDARD.md](../API_GOVERNANCE_STANDARD.md)
- **gRPC Security:** https://grpc.io/docs/guides/auth/
- **Protocol Buffers:** https://developers.google.com/protocol-buffers
- **Istio Security:** https://istio.io/latest/docs/concepts/security/

## Version Information

| Element               | Value                                           |
| --------------------- | ----------------------------------------------- |
| **Document Version**  | 1.0 (Initial Release)                           |
| **Issue Date**        | 2024-Q1                                         |
| **Profile Type**      | gRPC/Protocol Buffers Architecture              |
| **Relation to EATGF** | Implements Layer 08, Domain 02 for gRPC systems |
| **Next Review**       | Q2 2024                                         |
