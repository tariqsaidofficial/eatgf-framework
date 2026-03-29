# Flutter Framework Governance Profile

## Enterprise Conformance Model (v1.0)

---

## Authority Notice

**CLASSIFICATION:** Framework Implementation Profile (Cross-Cutting)

**AUTHORITY LAYER:** 08_DEVELOPER_GOVERNANCE_LAYER → FRAMEWORK_PROFILES → FRONTEND

**CONTROL AUTHORITY RELATIONSHIP:**

- This profile **implements** governance controls defined in [02_API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md)
- This profile **references** mobile-specific security requirements
- This profile **clarifies** Dart-specific patterns, BLoC architecture, secure storage
- This profile **does not** redefine any control from root governance documents

**COMPLIANCE STATEMENT:** This profile enforces security across Flutter applications (iOS/Android/web). Non-conformance impacts credential storage, platform channel security, and OTA update verification.

Flutter operates as **Mobile + Web Client** with Dart runtime (distinct from React Native's JavaScript runtime).

---

## 1. Purpose & Scope

This document defines governance conformance requirements for Flutter applications operating under EATGF.

**Scope:** Cross-platform mobile (iOS, Android), Flutter web applications, embedded Flutter in native apps

**Non-Scope:** Pure native iOS/Android development

---

## 2. Architectural Position

**EATGF Layer Placement:**

```
08_DEVELOPER_GOVERNANCE_LAYER
├── FRAMEWORK_PROFILES
│   └── FRONTEND
│       ├── React Native (JavaScript runtime)
│       └── Flutter (Dart runtime) ← THIS PROFILE
```

**Flutter operates as:**

- Dart application runtime
- Platform channels for native integration (iOS/Android)
- BLoC/Riverpod state management
- HTTP client with certificate pinning
- Secure storage bridge to Keychain/Keystore

**Critical Principle:** Flutter bridges Dart and native platforms. Security at both layers required.

---

## 3. Governance Principles

### Principle 1: Secure HTTP Client (MANDATORY)

```dart
//  PROHIBITED: No certificate pinning
final http.Client _httpClient = http.Client();

//  COMPLIANT: Certificate pinning
import 'package:flutter_http_client/flutter_http_client.dart';

Future<SecurityContext> createSecurityContext() async {
  final certBytes = await rootBundle.load('assets/certs/api.pem');
  final certificateChain = utf8.decode(certBytes.buffer.asUint8List());

  final context = SecurityContext.defaultContext;
  context.setTrustedCertificates(
    File.fromUri(Uri.dataFromString(certificateChain))
  );

  return context;
}

final IOClient _httpClient = IOClient(
  HttpClient()..badCertificateCallback = (_, __, ___) => false
);
```

### Principle 2: Secure Credential Storage (MANDATORY)

```dart
//  PROHIBITED: SharedPreferences for tokens
final prefs = await SharedPreferences.getInstance();
prefs.setString('token', token); // EXPOSED

//  COMPLIANT: flutter_secure_storage
import 'package:flutter_secure_storage/flutter_secure_storage.dart';

const storage = FlutterSecureStorage(
  aOptions: AndroidOptions(
    keyCipherAlgorithm: KeyCipherAlgorithm.RSA_ECB_OAEPwithSHA_256andMGF1Padding
  ),
  iOptions: IOSOptions(
    accessibility: KeychainAccessibility.first_available_when_unlocked_this_device_only
  ),
);

Future<void> saveToken(String token) async {
  await storage.write(key: 'auth_token', value: token);
}

Future<String?> getToken() async {
  return await storage.read(key: 'auth_token');
}
```

### Principle 3: BLoC Pattern for State (MANDATORY)

```dart
//  PROHIBITED: Mutable state directly in widgets
class UserWidget extends StatefulWidget {
  @override
  State<UserWidget> createState() => _UserWidgetState();
}

class _UserWidgetState extends State<UserWidget> {
  String? token; // EXPOSED state
  User? user;
}

//  COMPLIANT: BLoC manages auth state
class AuthBloc extends Bloc<AuthEvent, AuthState> {
  final AuthRepository _repository;

  AuthBloc(this._repository) : super(AuthInitial()) {
    on<AuthLoginEvent>(_onLogin);
    on<AuthLogoutEvent>(_onLogout);
  }

  Future<void> _onLogin(
    AuthLoginEvent event,
    Emitter<AuthState> emit,
  ) async {
    emit(AuthLoading());
    try {
      final user = await _repository.login(event.email, event.password);
      emit(AuthSuccess(user: user));
    } catch (e) {
      emit(AuthFailure(error: e.toString()));
    }
  }
}

class AuthPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return BlocListener<AuthBloc, AuthState>(
      listener: (context, state) {
        if (state is AuthSuccess) {
          Navigator.pushReplacementNamed(context, '/dashboard');
        }
      },
      child: BlocBuilder<AuthBloc, AuthState>(
        builder: (context, state) {
          if (state is AuthSuccess) {
            return DashboardWidget(user: state.user);
          }
          return LoginWidget();
        },
      ),
    );
  }
}
```

### Principle 4: Platform Channel Security (MANDATORY)

```dart
//  COMPLIANT: Sealed platform channel
@pragma('vm:entry-point')
Future<void> _nativeEntryPoint() async {
  WidgetsFlutterBinding.ensureInitialized();

  const methodChannel = MethodChannel('com.example.app/secure');

  methodChannel.setMethodCallHandler((MethodCall call) async {
    if (call.method == 'getBiometricsStatus') {
      //  Signature verification, platform-specific
      return await _checkBiometrics();
    }
    throw PlatformException(code: 'UNIMPLEMENTED', details: null);
  });
}

// Biometric verification
Future<bool> _checkBiometrics() async {
  final localAuth = LocalAuthentication();

  try {
    final isDeviceSupported = await localAuth.canCheckBiometrics;
    final canCheckDeviceAuth = await localAuth.deviceSupportsBiometric;

    if (!isDeviceSupported || !canCheckDeviceAuth) {
      return false;
    }

    return await localAuth.authenticate(
      localizedReason: 'Authenticate to access invoices',
      options: const AuthenticationOptions(
        stickyAuth: true,
        biometricOnly: true,
      ),
    );
  } catch (e) {
    return false;
  }
}
```

### Principle 5: HTTP Interceptor Chain (MANDATORY)

```dart
//  COMPLIANT: http.Client wrapper with interceptor
class AuthenticatedHttpClient extends http.BaseClient {
  final http.Client _inner;
  final TokenManager _tokenManager;

  AuthenticatedHttpClient(this._inner, this._tokenManager);

  @override
  Future<http.StreamedResponse> send(http.BaseRequest request) async {
    //  Add token to every request
    final token = await _tokenManager.getToken();
    if (token != null) {
      request.headers['Authorization'] = 'Bearer $token';
    }

    //  Add correlation ID
    request.headers['X-Correlation-ID'] = _generateUUID();

    final response = await _inner.send(request);

    //  Handle 401 (token expired)
    if (response.statusCode == 401) {
      await _tokenManager.clearToken();
      // Trigger re-authentication
    }

    return response;
  }
}
```

### Principle 6: Input Validation (MANDATORY)

```dart
//  COMPLIANT: Validate before sending
import 'package:validators/validators.dart';

class InvoiceRepository {
  Future<void> createInvoice({
    required String customerId,
    required double amount,
    required String currency,
  }) async {
    // Validate inputs
    if (customerId.isEmpty) {
      throw ValidationException('Customer ID required');
    }
    if (amount <= 0 || amount > 999999.99) {
      throw ValidationException('Invalid amount');
    }
    if (!['USD', 'EUR'].contains(currency)) {
      throw ValidationException('Invalid currency');
    }

    //  Send to server (server re-validates)
    return await _httpClient.post(
      Uri.parse('$_baseUrl/invoices'),
      body: jsonEncode({
        'customerId': customerId,
        'amount': amount,
        'currency': currency,
      }),
    );
  }
}
```

### Principle 7: OTA Update Verification (MANDATORY)

```dart
//  COMPLIANT: EAS Updates with signature verification
import 'package:eas_update/eas_update.dart';

Future<void> checkForUpdates() async {
  try {
    final UpdateCheckResult updateCheckResult = await Updates.checkAsync();

    if (updateCheckResult.isAvailable) {
      //  EAS automatically verifies signature
      await Updates.fetchUpdateAsync();
      await Updates.reloadAsync();
    }
  } catch (e) {
    print('Error checking for updates: $e');
  }
}
```

### Principle 8: Root/Jailbreak Detection (MANDATORY)

```dart
//  COMPLIANT: Detect compromised device
import 'package:device_info_plus/device_info_plus.dart';
import 'package:root_jailbreak_detection/root_jailbreak_detection.dart';

Future<bool> checkDeviceIntegrity() async {
  final bool? isJailBroken = await RootJailbreakDetection.canPhoneBeJailbroken();

  if (isJailBroken ?? false) {
    // Device compromised
    await _exitApp();
    return false;
  }

  return true;
}

Future<void> _exitApp() async {
  // Shut down app to prevent compromise
  SystemChannels.platform.invokeMethod('SystemNavigator.pop');
}
```

---

## 4. Control 1: Authentication

**Objective:** BLoC-based auth with secure token storage.

### Compliant Implementation

```dart
class AuthRepository {
  final AuthenticatedHttpClient _httpClient;
  final TokenManager _tokenManager;
  final SecureStorage _storage;

  Future<User> login(String email, String password) async {
    final response = await _httpClient.post(
      Uri.parse('$_baseUrl/auth/login'),
      body: {'email': email, 'password': password},
    );

    final data = jsonDecode(response.body);
    final token = data['token'];

    //  Store in secure storage
    await _storage.write('auth_token', token);

    return User.fromJson(data['user']);
  }

  Future<void> logout() async {
    await _httpClient.post(Uri.parse('$_baseUrl/auth/logout'));
    await _storage.delete('auth_token');
  }
}

class AuthBloc extends Bloc<AuthEvent, AuthState> {
  final AuthRepository repository;

  AuthBloc(this.repository) : super(AuthInitial()) {
    on<AuthCheckEvent>(_onCheck);
    on<AuthLoginEvent>(_onLogin);
  }

  Future<void> _onCheck(AuthCheckEvent event, Emitter<AuthState> emit) async {
    final token = await repository.getStoredToken();
    if (token != null) {
      emit(AuthSuccess());
    }
  }
}
```

---

## 5. Control 2: Authorization

**Objective:** Server-validated permissions with BLoC.

### Compliant Implementation

```dart
class PermissionBloc extends Bloc<PermissionEvent, PermissionState> {
  final ApiRepository api;

  PermissionBloc(this.api) : super(PermissionInitial()) {
    on<CheckPermissionEvent>(_onCheckPermission);
  }

  Future<void> _onCheckPermission(
    CheckPermissionEvent event,
    Emitter<PermissionState> emit,
  ) async {
    try {
      final response = await api.checkAuthorization(event.action);
      if (response.authorized) {
        emit(PermissionGranted());
      } else {
        emit(PermissionDenied());
      }
    } catch (e) {
      emit(PermissionDenied());
    }
  }
}
```

---

## 6. Control 3: Versioning

**Objective:** App version management.

### Compliant Implementation

```dart
import 'package:package_info_plus/package_info_plus.dart';

Future<void> checkAppVersion() async {
  final packageInfo = await PackageInfo.fromPlatform();
  final currentVersion = packageInfo.version;

  final response = await http.get(
    Uri.parse('$_baseUrl/app/version-check?version=$currentVersion'),
  );

  final data = jsonDecode(response.body);
  if (data['status'] == 'deprecated') {
    showDialog(context: context, builder: (_) => UpdateDialog());
  }
}
```

---

## 7. Control 4: Input Validation

**Objective:** Pre-submission validation.

### Compliant Implementation

```dart
class InvoiceForm {
  final formKey = GlobalKey<FormState>();

  Widget build(BuildContext context) {
    return Form(
      key: formKey,
      child: Column(
        children: [
          TextFormField(
            validator: (value) {
              if (value?.isEmpty ?? true) return 'Required';
              if (double.tryParse(value!) == null) return 'Invalid amount';
              return null;
            },
          ),
        ],
      ),
    );
  }

  void submit() {
    if (formKey.currentState!.validate()) {
      //  Form valid, send to server
      context.read<InvoiceBloc>().add(CreateInvoiceEvent(...));
    }
  }
}
```

---

## 8. Control 5: Rate Limiting

**Objective:** Backoff and retry logic.

### Compliant Implementation

```dart
class RateLimitHttpClient extends http.BaseClient {
  final http.Client _inner;

  @override
  Future<http.StreamedResponse> send(http.BaseRequest request) async {
    var response = await _inner.send(request);

    if (response.statusCode == 429) {
      final retryAfter = int.tryParse(
        response.headers['retry-after'] ?? '60'
      ) ?? 60;

      await Future.delayed(Duration(seconds: retryAfter));
      response = await _inner.send(request);
    }

    return response;
  }
}
```

---

## 9. Control 6: Testing & Documentation

**Objective:** Widget + API testing with mocking.

### Compliant Implementation

```dart
void main() {
  testWidgets('Login button disabled when form invalid', (tester) async {
    await tester.pumpWidget(MyApp());

    expect(find.byType(ElevatedButton), findsOneWidget);

    final button = find.byType(ElevatedButton).evaluate().first.widget;
    expect((button as ElevatedButton).onPressed, isNull); // disabled
  });

  test('Authentication interceptor adds token', () async {
    final storage = MockSecureStorage();
    when(storage.read('auth_token')).thenAnswer((_) async => 'test-token');

    final client = AuthenticatedHttpClient(MockHttpClient(), storage);

    await client.send(http.Request('GET', Uri.parse('https://api.example.com')));

    verify(storage.read('auth_token')).called(1);
  });
}
```

---

## 10. Control 7: Logging & Observability

**Objective:** Structured logging with correlation IDs.

### Compliant Implementation

```dart
class LoggingHttpClient extends http.BaseClient {
  final http.Client _inner;

  @override
  Future<http.StreamedResponse> send(http.BaseRequest request) async {
    final correlationId = const Uuid().v4();
    request.headers['X-Correlation-ID'] = correlationId;

    print('[$correlationId] ${request.method} ${request.url}');

    final response = await _inner.send(request);

    print('[$correlationId] → ${response.statusCode}');

    return response;
  }
}
```

---

## 11. Control 8: Zero Trust Networking

**Objective:** HTTPS enforcement and certificate pinning.

### Compliant Implementation

```dart
//  Force HTTPS in production
final Uri baseUrl = Uri.parse(
  kReleaseMode
    ? 'https://api.example.com'
    : 'https://staging-api.example.com'
);

//  Certificate pinning (covered in Principle 1)
//  Secure platform channels for native calls
```

---

## 12. Multi-Tenancy Controls

**Objective:** Tenant context from auth state.

### Compliant Implementation

```dart
class TenantBloc extends Bloc<TenantEvent, TenantState> {
  final AuthBloc authBloc;

  TenantBloc(this.authBloc) : super(TenantInitial()) {
    authBloc.stream.listen((authState) {
      if (authState is AuthSuccess) {
        emit(TenantLoaded(tenantId: authState.user.tenantId));
      }
    });
  }
}
```

---

## 13. Dependency & Supply Chain Governance

```bash
flutter pub get
flutter pub outdated
dart run build_runner build
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

- [ ] Certificate pinning configured for API endpoint
- [ ] Tokens stored in flutter_secure_storage (not SharedPreferences)
- [ ] BLoC pattern used for all state management
- [ ] Platform channels have signature verification
- [ ] HTTP client has interceptor chain (auth, logging, error)
- [ ] Input validation before API submission
- [ ] Biometric authentication supported
- [ ] OTA updates verify signature
- [ ] Jailbreak/root detection enabled
- [ ] 80%+ test coverage
- [ ] Correlation IDs on all HTTP requests
- [ ] 401 responses trigger re-authentication

---

## Official References

- Flutter Documentation: https://flutter.dev/docs
- Flutter Security Best Practices: https://flutter.dev/docs/testing/integration-tests
- OWASP Mobile Security: https://owasp.org/www-project-mobile-top-10/
- Dart HTTP Security: https://pub.dev/packages/http
- Android & iOS Security: https://developer.apple.com/security/ and https://developer.android.com/security

---

## 16. Version Information

| Field                | Value         |
| -------------------- | ------------- |
| **Document Version** | 1.0           |
| **Flutter Version**  | 3.0+          |
| **Dart Version**     | 2.18+         |
| **Min iOS**          | 11.0+         |
| **Min Android**      | 5.0 (API 21)+ |

---

**Authorization:** Enterprise Architecture Board
**Last Reviewed:** February 15, 2026
**Next Review:** August 15, 2026
