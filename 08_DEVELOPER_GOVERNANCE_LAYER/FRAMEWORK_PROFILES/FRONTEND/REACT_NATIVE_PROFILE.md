# React Native Framework Governance Profile
## Enterprise Conformance Model (v1.0)

---

## Authority Notice

**CLASSIFICATION:** Framework Implementation Profile (Cross-Cutting)

**AUTHORITY LAYER:** 08_DEVELOPER_GOVERNANCE_LAYER → FRAMEWORK_PROFILES → FRONTEND

**CONTROL AUTHORITY RELATIONSHIP:**
- This profile **implements** governance controls defined in [02_API_GOVERNANCE_STANDARD.md](../../02_API_GOVERNANCE/API_GOVERNANCE_STANDARD.md)
- This profile **references** secure SDLC requirements from [01_SECURE_SDLC_STANDARD.md](../../01_SECURE_SDLC/SECURE_SDLC_STANDARD.md)
- This profile **clarifies** mobile-specific DevSecOps patterns
- This profile **does not** redefine any control from root governance documents
- This profile **differs** from React/Next.js: mobile requires device-level security controls

**COMPLIANCE STATEMENT:** This profile enforces security across iOS and Android mobile applications. Non-conformance impacts:
- Credential theft from device storage
- Man-in-the-middle (MITM) attacks via certificate pinning bypass
- Jailbroken/rooted device exploitation
- Over-the-air (OTA) update attacks
- Biometric authentication spoofing

React Native operates as **Mobile Client** with:
- Device OS integration (iOS/Android)
- Local credential storage (Keychain/Keystore)
- Network certificate verification
- Platform-specific permissions model

---

## 1. Purpose & Scope

This document defines governance conformance requirements for React Native applications (iOS and Android) operating under EATGF.

**Scope:** Native mobile applications, cross-platform iOS/Android clients, enterprise mobile apps, financial/healthcare mobile clients

**Non-Scope:** Web-based mobile (React web), desktop/Electron apps, platform-specific native code (except for security bridges)

---

## 2. Architectural Position

**EATGF Layer Placement:**
```
08_DEVELOPER_GOVERNANCE_LAYER
├── FRAMEWORK_PROFILES
│   ├── BACKEND (Django, FastAPI, Node.js, Spring Boot)
│   ├── FRONTEND
│   │   ├── React (web browser)
│   │   ├── Next.js (hybrid SSR/CSR)
│   │   └── React Native (iOS & Android) ← THIS PROFILE
│   └── INFRASTRUCTURE
```

**React Native operates as:**
- **Sandboxed application** (iOS App Sandbox, Android SELinux)
- **OS credential consumer** (Keychain, Keystore, Biometric APIs)
- **Network client** with certificate pinning
- **Permissions requester** (camera, location, contacts)
- **OTA update consumer** (CodePush, EAS Updates, native app stores)

**React Native must conform to:**
- **02_API_GOVERNANCE:** API client security (network layer)
- **01_SECURE_SDLC:** Mobile development lifecycle
- **Mobile-Specific Controls:**
  - Certificate pinning (MITM prevention)
  - Biometric authentication
  - Device integrity checking
  - Jailbreak/root detection
  - Credential storage (Keychain/Keystore)
  - OTA update verification

**Critical Principle:** Mobile is higher-risk than web. Device can be physically compromised, jailbroken, or rooted. Assume device OS is untrusted in adversarial scenarios.

---

## 3. Governance Principles

### Principle 1: Certificate Pinning (MANDATORY)

Prevent MITM attacks by validating server certificate against pinned public key.

```typescript
// ❌ PROHIBITED: Accept any valid SSL certificate
const response = await fetch('https://api.example.com/invoices');

// ✅ COMPLIANT: Pin certificate
import { fetch as pinnedFetch } from 'react-native-pinch';

const config = {
  host: 'api.example.com',
  cert: require('./certs/api-cert.pem') // Embedded certificate
};

const response = await pinnedFetch(
  'https://api.example.com/invoices',
  {
    method: 'GET',
    credentials: 'include',
    // Verify cert against pinned value
  },
  config
);
```

**Pinning Strategy:**

```typescript
// lib/certificate-pinning.ts
import { Platform } from 'react-native';
import { CertificatePinning } from 'react-native-certificate-pinning';

// ✅ Pin public key hash (survives certificate rotation)
const publicKeyHashes = {
  'api.example.com': [
    'sha256/4QfD+yj7Kpq6ELVIz4pzXfMpJDkqvvQ+VRNW2xv7Q2g=', // Primary
    'sha256/6X5p8qJV2KpLcR7Z9bvQ+XvNpT1zV5qC4Z2qR1q2mP8='  // Backup
  ],
  'cdn.example.com': [
    'sha256/Z5bQzW2kPw5sX9jY8oV6Z3U1T2V5qC4Z2qR1q2mP8Z='
  ]
};

export async function setupCertificatePinning() {
  await Promise.all(
    Object.entries(publicKeyHashes).map(([domain, hashes]) =>
      CertificatePinning.setHosts({
        [domain]: {
          includeSubdomains: true,
          pins: hashes
        }
      })
    )
  );
}

// ✅ Validate in app initialization
export function initializeApp() {
  setupCertificatePinning().catch((error) => {
    console.error('Certificate pinning setup failed:', error);
    // Crash app if pinning cannot be established
    throw new Error('Security initialization failed');
  });
}
```

**Enforcement:**
- Pin both leaf and intermediate certificates
- Include backup keys for rotation
- Update pinned certificates in each app release
- Test pinning in CI/CD

---

### Principle 2: Secure Credential Storage (MANDATORY)

Never store tokens in plain text. Use OS-provided secure storage.

```typescript
// ❌ PROHIBITED: AsyncStorage (plain text)
import AsyncStorage from '@react-native-async-storage/async-storage';

await AsyncStorage.setItem('auth_token', token); // EXPOSED

// ❌ PROHIBITED: Redux persist
store.dispatch(setToken(token)); // Persisted to storage

// ✅ COMPLIANT: Keychain (iOS) / Keystore (Android)
import * as SecureStore from 'expo-secure-store';

export async function saveToken(token: string) {
  try {
    await SecureStore.setItemAsync('auth_token', token, {
      keychainAccessible: SecureStore.WHEN_UNLOCKED // iOS: require device unlock
    });
  } catch (error) {
    console.error('Failed to save token securely');
    throw error;
  }
}

export async function getToken(): Promise<string | null> {
  try {
    return await SecureStore.getItemAsync('auth_token');
  } catch (error) {
    console.error('Failed to retrieve token');
    return null;
  }
}

// ✅ Initialization: Restore token on app launch
export function useAuthRestoration() {
  const [isReady, setIsReady] = useState(false);

  useEffect(() => {
    const restoreToken = async () => {
      const token = await getToken();
      
      if (token) {
        // ✅ Validate with server before using
        const isValid = await validateToken(token);
        if (!isValid) {
          await deleteToken();
        }
      }
      
      setIsReady(true);
    };

    restoreToken();
  }, []);

  return { isReady };
}
```

**Enforcement:**
- No AsyncStorage for tokens
- SecureStore (Expo), react-native-keychain, or platform-specific
- Require device unlock (iOS: WHEN_UNLOCKED_THIS_DEVICE_ONLY)
- Clear on logout

---

### Principle 3: Jailbreak/Root Detection (MANDATORY)

Prevent app execution on compromised devices.

```typescript
// ✅ COMPLIANT: Detect jailbreak/root
import { Platform } from 'react-native';
import { jailmonkey } from 'jailmonkey';

export async function checkDeviceIntegrity(): Promise<boolean> {
  try {
    if (Platform.OS === 'ios') {
      const isJailbroken = await jailmonkey.isJailBrokenIOS(true);
      
      if (isJailbroken) {
        // ✅ Disable sensitive features
        console.warn('Jailbroken device detected');
        return false;
      }
    }

    if (Platform.OS === 'android') {
      const isRooted = await jailmonkey.isJailBrokenAndroid(true);
      
      if (isRooted) {
        console.warn('Rooted device detected');
        return false;
      }
    }

    return true;
  } catch (error) {
    // ❌ If check fails, assume compromised
    console.error('Device integrity check failed:', error);
    return false;
  }
}

// ✅ Enforcement: Block app usage on compromised device
export function useDeviceIntegrityCheck() {
  useEffect(() => {
    checkDeviceIntegrity().then((isSecure) => {
      if (!isSecure) {
        // Show warning or crash app
        Alert.alert(
          'Security Alert',
          'This app cannot run on jailbroken/rooted devices',
          [{ text: 'Exit', onPress: () => RNExitApp.exitApp() }]
        );
      }
    });
  }, []);
}
```

**Risk Levels:**
- **CRITICAL:** Root shell detected
- **HIGH:** Malicious package managers detected (Cydia, Xposed)
- **MEDIUM:** Debugging tools detected (Frida, debuggers)

---

### Principle 4: Biometric Authentication (MANDATORY for Financial Apps)

Support biometric (fingerprint, Face ID) with fallback to password.

```typescript
// ✅ COMPLIANT: Biometric authentication with fallback
import * as LocalAuthentication from 'expo-local-authentication';

export async function authenticateBiometric(): Promise<boolean> {
  try {
    // ✅ Check if device supports biometric
    const compatible = await LocalAuthentication.hasHardwareAsync();
    
    if (!compatible) {
      console.log('Device does not support biometric');
      return false;
    }

    // ✅ Check if biometric is enrolled
    const enrolled = await LocalAuthentication.isEnrolledAsync();
    
    if (!enrolled) {
      console.log('No biometric enrolled');
      return false;
    }

    // ✅ Prompt for biometric (face ID or fingerprint)
    const result = await LocalAuthentication.authenticateAsync({
      disableDeviceFallback: false, // Allow device passcode as fallback
      reason: 'Authenticate to access your invoices',
      promptMessage: 'Use biometric or device passcode'
    });

    return result.success;
  } catch (error) {
    console.error('Biometric authentication failed:', error);
    return false;
  }
}

// ✅ Usage: Require biometric for sensitive operations
export function useProtectedOperation() {
  const performSensitiveAction = async (action: () => Promise<void>) => {
    const authenticated = await authenticateBiometric();
    
    if (!authenticated) {
      Alert.alert('Authentication Failed', 'Could not verify identity');
      return;
    }

    await action(); // Proceed only after biometric success
  };

  return { performSensitiveAction };
}

// ✅ CRITICAL: Never transmit biometric data to server
// Biometric verification is local only
// Server verifies session token, not biometric
```

---

### Principle 5: API Client Configuration (MANDATORY)

Centralize API configuration with security controls.

```typescript
// lib/api-client.ts
import axios, { AxiosInstance } from 'axios';
import * as SecureStore from 'expo-secure-store';
import { Platform } from 'react-native';
import { CertificatePinning } from 'react-native-certificate-pinning';

// ✅ Centralized API client
export const createApiClient = async (): Promise<AxiosInstance> => {
  // ✅ Setup certificate pinning
  await setupCertificatePinning();

  const api = axios.create({
    baseURL: Platform.OS === 'ios' 
      ? 'https://api-ios.example.com' 
      : 'https://api-android.example.com',
    timeout: 5000
  });

  // ✅ Request interceptor: Add auth token from secure storage
  api.interceptors.request.use(async (config) => {
    const token = await SecureStore.getItemAsync('auth_token');
    
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }

    config.headers['X-Correlation-ID'] = generateUUID();
    config.headers['User-Agent'] = `MyApp/${APP_VERSION}`;

    return config;
  });

  // ✅ Response interceptor: Handle 401 (token expired)
  api.interceptors.response.use(
    (response) => response,
    async (error) => {
      if (error.response?.status === 401) {
        // Token expired, clear storage and redirect to login
        await SecureStore.deleteItemAsync('auth_token');
        // Trigger re-authentication
        return Promise.reject(error);
      }
      return Promise.reject(error);
    }
  );

  return api;
};

export const api = createApiClient();
```

---

### Principle 6: Permissions Model (MANDATORY)

Request OS permissions only when needed.

```typescript
// ✅ COMPLIANT: Request permissions at usage time
import * as Permissions from 'expo-permissions';

export async function requestCameraPermission() {
  const { status } = await Permissions.askAsync(Permissions.CAMERA);
  
  if (status !== 'granted') {
    Alert.alert('Permission Required', 'Camera access is required');
    return false;
  }

  return true;
}

// ✅ Usage: Request only when feature is used
export function CameraScanner() {
  const [hasPermission, setHasPermission] = useState(false);

  const enableCamera = async () => {
    const granted = await requestCameraPermission();
    setHasPermission(granted);
  };

  return (
    <button onPress={enableCamera}>
      Scan Invoice
    </button>
  );
}

// ✅ Manifest declaration (app.json)
{
  "expo": {
    "plugins": [
      [
        "expo-camera",
        {
          "cameraPermission": "Allow MyApp to access your camera."
        }
      ]
    ]
  }
}
```

---

### Principle 7: OTA Update Security (MANDATORY)

Verify integrity of over-the-air updates.

```typescript
// ✅ COMPLIANT: EAS Updates with signature verification
import * as Updates from 'expo-updates';

export async function initializeUpdates() {
  try {
    // ✅ EAS automatically handles signature verification
    const update = await Updates.checkAsync();

    if (update.isAvailable) {
      // ✅ Verify update before installing
      console.log('Update available, installing...');
      
      await Updates.fetchUpdateAsync();
      await Updates.reloadAsync();
    }
  } catch (error) {
    if (error instanceof Updates.UpdatesError) {
      // ✅ Handle update failures securely
      console.error('Update failed:', error);
      // Don't crash, continue with current version
    }
  }
}

// ✅ Alternative: CodePush with signature verification
import CodePush from 'react-native-code-push';

const codePushOptions = {
  // ✅ Checksum verification mandatory
  checkFrequency: CodePush.CheckFrequency.ON_APP_START,
  // ✅ Install immediately only for critical fixes
  installMode: CodePush.InstallMode.ON_NEXT_RESTART,
  // ✅ Deployment key from secure config, not hardcoded
  deploymentKey: process.env.CODEPUSH_KEY
};

export const App = CodePush(codePushOptions)(MainApp);

// ❌ PROHIBITED: Disable signature verification
// ❌ PROHIBITED: Hardcoded deployment keys
```

---

### Principle 8: Build & Release Security (MANDATORY)

Ensure app builds are signed and verified.

```bash
# ✅ iOS: Build with signing certificate
fastlane ios build --signing-certificate MyCompanyCA

# ✅ Android: Sign with keystore
jarsigner -verbose -sigalg SHA256withRSA -digestalg SHA-256 \
  -keystore my-app.keystore app-release.apk my-app-key

# ✅ Verify signature
jarsigner -verify -verbose -certs app-release.apk

# ✅ CI/CD: Strip debug symbols from production build
--release --minify

# ✅ CI/CD: Verify no secrets in build
! grep -r "API_KEY\|SECRET" build/
```

---

## 4. Control 1: Authentication

**Objective:** Establish mobile user identity with secure token handling.

### Requirement
- Biometric optional, password mandatory as fallback
- Tokens stored in Keychain/Keystore only
- Session validation on app launch
- Token refresh handled transparently

### Compliant Implementation

```typescript
export function useAuth() {
  const [user, setUser] = useState(null);
  const [isLoading, setIsLoading] = useState(true);
  const api = useContext(ApiContext);

  useEffect(() => {
    const restoreSession = async () => {
      try {
        // ✅ Retrieve token from secure storage
        const token = await SecureStore.getItemAsync('auth_token');

        if (token) {
          // ✅ Validate token with server
          const response = await api.get('/auth/user');
          setUser(response.data);
        }
      } catch (error) {
        console.error('Session restore failed');
        // Token invalid, user must re-authenticate
      } finally {
        setIsLoading(false);
      }
    };

    restoreSession();
  }, []);

  const login = async (email: string, password: string) => {
    try {
      const response = await api.post('/auth/login', { email, password });

      // ✅ Store token in secure storage
      await SecureStore.setItemAsync('auth_token', response.data.token);

      setUser(response.data.user);
    } catch (error) {
      if (error.response?.data?.mfaRequired) {
        return { mfaRequired: true };
      }
      throw error;
    }
  };

  const logout = async () => {
    await SecureStore.deleteItemAsync('auth_token');
    setUser(null);
  };

  return { user, isLoading, login, logout };
}
```

---

## 5. Control 2: Authorization

**Objective:** Authorize actions based on server-validated permissions.

### Requirement
- Backend re-validates authorization
- Frontend shows/hides UI based on permissions
- No client-side permission spoofing

### Compliant Implementation

```typescript
export function useAuthorization(action: string) {
  const { user } = useAuth();
  const [canAccess, setCanAccess] = useState(false);
  const api = useContext(ApiContext);

  useEffect(() => {
    const checkAuth = async () => {
      try {
        // ✅ Server authorizes action
        const response = await api.get('/auth/can', {
          params: { action }
        });
        setCanAccess(response.data.authorized);
      } catch {
        setCanAccess(false);
      }
    };

    if (user) {
      checkAuth();
    }
  }, [user, action]);

  return canAccess;
}

export function DeleteInvoiceButton({ invoiceId }) {
  const canDelete = useAuthorization('delete_invoice');

  if (!canDelete) return null;

  return (
    <button onPress={async () => {
      // ✅ Server validates permission again
      await api.delete(`/invoices/${invoiceId}`);
    }}>
      Delete
    </button>
  );
}
```

---

## 6. Control 3: Versioning

**Objective:** Manage app versioning and API compatibility.

### Requirement
- App version checked on launch
- Deprecation warnings displayed
- Force upgrade on critical versions

### Compliant Implementation

```typescript
export async function checkAppVersion() {
  const currentVersion = Constants.manifest.version;
  
  const response = await api.get('/app/version-check', {
    params: { version: currentVersion }
  });

  const { status, minimumVersion, message } = response.data;

  if (status === 'deprecated') {
    Alert.alert(
      'Update Available',
      message,
      [
        {
          text: 'Update Now',
          onPress: () => Linking.openURL('https://apps.apple.com/...')
        }
      ]
    );
  } else if (status === 'critical') {
    Alert.alert(
      'Critical Update Required',
      'Your app version is no longer supported',
      [
        {
          text: 'Update',
          onPress: () => Linking.openURL('https://apps.apple.com/...'),
          isPreferred: true
        }
      ]
    );
  }
}
```

---

## 7. Control 4: Input Validation

**Objective:** Validate all user input before sending to API.

### Requirement
- Client-side validation for UX
- Server-side validation mandatory
- Schema coercion and sanitization

### Compliant Implementation

```typescript
import { z } from 'zod';

const InvoiceSchema = z.object({
  amount: z.number().positive().max(999999.99),
  currency: z.enum(['USD', 'EUR']),
  dueDate: z.string().datetime()
});

export function InvoiceForm() {
  const [errors, setErrors] = useState({});

  const handleSubmit = async (data) => {
    try {
      // ✅ Parse and validate
      const validated = InvoiceSchema.parse(data);

      // ✅ Send to server (server re-validates)
      await api.post('/invoices', validated);
    } catch (error) {
      if (error instanceof z.ZodError) {
        setErrors(error.flatten().fieldErrors);
      }
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      {/* Form fields */}
    </form>
  );
}
```

---

## 8. Control 5: Rate Limiting

**Objective:** Prevent client from overwhelming API.

### Requirement
- Exponential backoff on failures
- 429 response handling
- User feedback on rate limits

### Compliant Implementation

```typescript
export const api = axios.create({
  baseURL: process.env.API_URL
});

api.interceptors.response.use(
  response => response,
  async error => {
    if (error.response?.status === 429) {
      const retryAfter = parseInt(
        error.response.headers['retry-after'] || '60'
      );

      Alert.alert('Rate Limited', `Please try again in ${retryAfter}s`);

      await new Promise(resolve => 
        setTimeout(resolve, retryAfter * 1000)
      );

      return api.request(error.config);
    }

    return Promise.reject(error);
  }
);
```

---

## 9. Control 6: Testing & Documentation

**Objective:** Ensure app quality and security.

### Requirement
- Unit test coverage > 80%
- E2E tests for auth flows
- Security tests for certificate pinning

### Compliant Implementation

```typescript
describe('Certificate Pinning', () => {
  it('rejects requests to unpinned domains', async () => {
    expect(async () => {
      await api.get('https://untrusted.example.com/data');
    }).rejects.toThrow('Certificate verification failed');
  });
});

describe('Secure Storage', () => {
  it('stores token in secure storage', async () => {
    await saveToken('test-token');
    const token = await SecureStore.getItemAsync('auth_token');
    expect(token).toBe('test-token');
  });
});

describe('Jailbreak Detection', () => {
  it('prevents app on jailbroken device', async () => {
    const result = await checkDeviceIntegrity();
    expect(result).toBe(true); // Pass on non-jailbroken device
  });
});
```

---

## 10. Control 7: Logging & Observability

**Objective:** Capture errors and security events without exposing sensitive data.

### Requirement
- Structured logging with correlation IDs
- No sensitive data in logs
- Error tracking integrated

### Compliant Implementation

```typescript
import * as Sentry from "@sentry/react-native";

Sentry.init({
  dsn: process.env.SENTRY_DSN,
  beforeSend(event) {
    // ✅ Remove sensitive data
    if (event.request) {
      delete event.request.cookies;
      delete event.request.headers['authorization'];
    }
    return event;
  }
});

export const logger = {
  error: (message: string, context?: any) => {
    console.error(message, context);
    Sentry.captureException(new Error(message), { contexts: { extra: context } });
  },
  info: (message: string, context?: any) => {
    console.log(message, context);
  }
};
```

---

## 11. Control 8: Zero Trust Networking

**Objective:** Enforce network security and certificate verification.

### Requirement
- HTTPS only (no HTTP)
- Certificate pinning enforced
- Secure cookie transport

### Compliant Implementation

```typescript
// ✅ Certificate pinning (covered in Principle 1)
// ✅ HTTPS-only configuration
const api = axios.create({
  baseURL: 'https://api.example.com', // HTTPS only
  timeout: 5000,
  withCredentials: true
});

// ✅ No plain HTTP URLs
// Build fails if HTTP URL detected
if (API_URL.startsWith('http://') && !DEV_MODE) {
  throw new Error('API URL must use HTTPS in production');
}
```

---

## 12. Multi-Tenancy Controls

**Objective:** Enforce tenant isolation (if applicable).

### Requirement
- Tenant ID from server only
- No URL-based tenant switching
- Session includes tenant context

### Compliant Implementation

```typescript
interface AuthSession {
  userId: string;
  tenantId: string;
  roles: string[];
}

export function useTenant(): string {
  const { user } = useAuth() as { user: AuthSession };
  return user.tenantId; // From authenticated session
}

// ✅ All requests include tenant context
api.interceptors.request.use(config => {
  const tenantId = useTenant();
  config.headers['X-Tenant-ID'] = tenantId;
  return config;
});
```

---

## 13. Dependency & Supply Chain Governance

**Objective:** Manage dependency security.

### Requirement
- npm audit passes
- Dependencies pinned
- CI/CD verification

### Compliant Implementation

```json
{
  "scripts": {
    "audit": "npm audit --audit-level=high",
    "build": "react-native build-ios && react-native build-android"
  }
}
```

```bash
# CI/CD
npm ci
npm audit --audit-level=high || exit 1
```

---

## 14. Control Mapping

| EATGF Control | ISO 27001:2022 | NIST SSDF 1.1 | OWASP ASVS 5.0 | COBIT 2019 |
|---|---|---|---|---|
| Authentication | A.8.2, A.8.3 | PW.2.1 | V2 | DSS05.02 |
| Authorization | A.8.5, A.8.9 | PW.2.2 | V4 | DSS05.03 |
| Versioning | A.8.28 | PW.4.2 | V14 | BAI09.02 |
| Input Validation | A.8.22 | PW.8.1 | V5 | DSS05.04 |
| Rate Limiting | A.8.22 | PW.8.2 | V11 | DSS01.05 |
| Testing | A.8.28 | PW.9.1 | V14 | BAI03.07 |
| Logging | A.8.15, A.8.23 | RV.1.1 | V15 | MEA01.02 |
| Zero Trust | A.8.1, A.8.9 | PW.1.1 | V1 | DSS05.01 |

---

## 15. Developer Checklist

- [ ] Certificate pinning configured for all API domains
- [ ] Auth token stored in Keychain (iOS) / Keystore (Android) only
- [ ] Jailbreak/root detection enabled and enforced
- [ ] Biometric authentication supported with password fallback
- [ ] Centralized API client with correlation IDs
- [ ] 401 responses trigger re-authentication
- [ ] Permissions requested at feature usage time (not app launch)
- [ ] OTA updates verified (EAS or CodePush with signatures)
- [ ] App signed with production certificate
- [ ] No API keys hardcoded in app
- [ ] Device integrity check on app launch
- [ ] Secure storage used for all sensitive data
- [ ] HTTPS enforced (no HTTP fallback)
- [ ] npm audit passes
- [ ] Biometric data never sent to server

---

## 16. Governance Implications

**Risk if not implemented:**
- Token theft via secure storage bypass
- MITM attacks via certificate pinning bypass
- Jailbroken app execution and data theft
- Biometric spoofing on compromised device
- OTA update exploitation

**SOC2/ISO 27001:** Mobile-specific controls enforce A.8.2, A.8.3 (Authentication), A.8.1 (Network Security)

---

## 17. Version Information

| Field | Value |
|---|---|
| **Document Version** | 1.0 |
| **Change Type** | Major (Initial Release) |
| **Issue Date** | February 15, 2026 |
| **EATGF Baseline** | v1.0 (Block 2 Complete) |
| **React Native Version** | 0.72+ |
| **iOS Minimum** | 12.0+ |
| **Android Minimum** | 5.0 (API 21)+ |

---

**Authorization:** Enterprise Architecture Board (EATGF Governance)
**Last Reviewed:** February 15, 2026
**Next Review:** August 15, 2026
