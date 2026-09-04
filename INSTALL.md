# Installation

Mobile Security AI is a skill and workflow layer for AI-assisted mobile application security research. It is designed to sit on top of an existing security workstation and orchestrate tools rather than replace them.

## 1. Requirements

### Operating system

Linux is recommended. macOS is supported for most static-analysis workflows. Windows is usable through WSL2.

### Base software

Install the following according to the targets you intend to analyze:

- Python 3.11+
- Git
- Android SDK / `adb`
- Java 17+
- JADX
- apktool
- Frida / frida-tools
- Ghidra, Rizin or radare2 for native analysis
- A proxy such as Burp Suite or mitmproxy for authorized traffic capture
- Optional: iOS tooling and a macOS/Xcode environment for IPA/device work

The repository's Python helpers intentionally favor the standard library where practical. This keeps the core workflow portable and avoids turning a pentesting skill into a dependency-management hobby.

## 2. Clone

```bash
git clone https://github.com/ny0x696/mobile-security-ai.git
cd mobile-security-ai
```

## 3. Verify the repository

```bash
python3 --version
git status
find agents workflows schemas scripts -maxdepth 2 -type f | sort
```

Run the local helper tests when present:

```bash
python3 -m unittest discover -s tests -v
```

## 4. OpenCode

Copy or link the repository's skill into the location used by your OpenCode installation, then expose `SKILL.md` and the `agents/`, `workflows/`, `schemas/` and `scripts/` directories to the agent workspace.

A typical project layout is:

```text
project/
├── .opencode/
│   └── skills/
│       └── mobile-security-ai/
└── ...
```

The exact OpenCode skill directory can vary by installation. The important requirement is that the agent can resolve the repository's `SKILL.md` and its referenced paths.

## 5. Qoder

Add the repository as a reusable skill according to the Qoder skill mechanism. The entry point is:

```text
SKILL.md
```

Keep the repository available in the agent workspace so referenced agents, workflows, schemas and scripts remain resolvable.

## 6. Android workstation

For APK/AAB analysis, verify:

```bash
adb version
java -version
jadx --version
apktool --version
frida --version
```

Typical workflow:

```text
APK/AAB
  -> inventory
  -> JADX/apktool
  -> manifest/components
  -> endpoints and data flows
  -> native/JNI boundaries
  -> runtime instrumentation
  -> evidence
```

Do not connect a production account or personal device to an assessment unless the program explicitly permits it. Use dedicated test accounts and controlled fixtures.

## 7. iOS workstation

IPA and device-level work generally requires macOS plus the appropriate Apple development/signing environment. Verify the tools required by the specific assessment before starting runtime work.

Recommended workflow:

```text
IPA/Mach-O
  -> bundle inventory
  -> plist/entitlements
  -> Objective-C/Swift/native analysis
  -> URL schemes/universal links
  -> networking/storage/crypto review
  -> runtime instrumentation
  -> evidence
```

## 8. API testing configuration

Active API validation requires an explicit scope definition. At minimum, define:

- allowed hosts
- allowed methods
- test accounts
- approved object IDs or fixtures
- request provenance
- rate/request limits

Credentials should be supplied through environment variables or another secret manager, never committed to Git.

Example naming convention:

```bash
export MSAI_TEST_OWNER_USERNAME='owner-test@example.invalid'
export MSAI_TEST_OWNER_PASSWORD='REDACTED'
export MSAI_TEST_SECOND_USERNAME='second-test@example.invalid'
export MSAI_TEST_SECOND_PASSWORD='REDACTED'
```

The credential helpers in `scripts/auth/` are intended for approved test identities. They do not implement credential stuffing or password attacks.

## 9. Case structure

Each assessment should have a case directory similar to:

```text
cases/<target>/
├── target.json
├── scope.json
├── inventory.json
├── endpoints.json
├── hypotheses.json
├── evidence.json
├── findings.json
├── static/
├── native/
├── runtime/
├── network/
├── scripts/
├── artifacts/
└── report/
```

Treat `scope.json` as a hard gate, not documentation. Active validation should stop when scope cannot be established.

## 10. First run

Start with passive analysis:

```text
1. Initialize a case.
2. Import the program scope.
3. Fingerprint the target.
4. Build the asset inventory.
5. Extract endpoints from observed traffic and application artifacts.
6. Map authentication and authorization boundaries.
7. Generate hypotheses.
8. Validate only hypotheses supported by evidence and permitted by scope.
9. Record evidence.
10. Produce findings and a report.
```

The expected reasoning loop is:

```text
Observation
    ↓
Hypothesis
    ↓
Evidence
    ↓
Minimal authorized validation
    ↓
Confirmed / Rejected / Inconclusive
```

## 11. Operational rules

- Never test an asset merely because it was discovered.
- Never infer authorization from a hostname alone.
- Never invent an endpoint, parameter, token, header or response.
- Prefer observed requests and documented program behavior as the source of truth.
- Keep validation bounded and reproducible.
- Redact credentials, session tokens and secrets from artifacts.
- Preserve provenance for every finding.
- Separate scanner output from confirmed vulnerabilities.
- Stop when authorization or scope is ambiguous.

## 12. Troubleshooting

### `adb` cannot see the device

Check USB debugging, device authorization and `adb devices`. For emulators, verify the emulator is running and reachable.

### JADX/apktool is missing

Install them separately and make sure their binaries are on `PATH`. The skill does not bundle third-party reverse-engineering tools.

### Frida cannot attach

Check that the client and target-side Frida versions are compatible, the device is reachable, and the assessment explicitly permits runtime instrumentation.

### A validation script refuses to run

Check `scope.json`, the active-testing flag, allowed hosts/methods and the supplied test identities. A refusal is a safety feature, not a bug to bypass.

### A finding is inconclusive

Keep it inconclusive. Do not turn a plausible hypothesis into a vulnerability because a report looks more impressive that way.

## 13. Recommended environment

For serious work, use an isolated assessment environment with:

- dedicated Android emulator/device
- dedicated test accounts
- isolated proxy workspace
- reproducible case directories
- Git history for scripts and evidence metadata
- separate storage for secrets
- network controls that make out-of-scope access difficult

This project is intentionally an orchestration and reasoning layer. The quality of the result still depends on the quality of the underlying evidence and the operator's judgment.
