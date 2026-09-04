# Mobile Security AI

> AI-assisted mobile application security research for experienced operators.

Mobile Security AI is a security-engineering skill system for **authorized** reverse engineering, API assessment, runtime analysis and bug-bounty research. It connects application artifacts, network traffic, native code and runtime observations into one evidence-driven workflow.

The goal is not to produce a larger scanner. It is to give an AI agent a disciplined methodology for doing the work a strong mobile pentester would actually do: establish scope, build an attack-surface model, form hypotheses, validate them carefully, preserve evidence and report only what can be defended.

[![License](https://img.shields.io/badge/license-MIT-informational)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Android%20%7C%20iOS%20%7C%20API%20%7C%20Native-111827)](#scope)
[![Focus](https://img.shields.io/badge/focus-Mobile%20Security%20%7C%20Bug%20Bounty-111827)](#capabilities)

---

## What it is

A reusable set of **agents, workflows, schemas, templates and local validation helpers** that can be used from AI coding/agent environments such as OpenCode and Qoder.

It is designed around a simple principle:

```text
Do not confuse something interesting with something proven.
```

Every meaningful result should be traceable from observation to hypothesis, validation and evidence.

## Capabilities

| Area | Coverage |
|---|---|
| Android | APK/AAB/DEX, manifest, exported components, intents, deep links, WebView, storage, crypto, JNI |
| iOS | IPA/Mach-O, entitlements, URL schemes, universal links, Keychain, WebView, ATS, native boundaries |
| API | Authentication, authorization, BOLA/IDOR, data exposure, injection hypotheses, business logic, GraphQL/WebSocket |
| Native | ARM64, JNI, C/C++, Swift/Objective-C boundaries, crypto and binary analysis |
| Runtime | Frida-assisted observation, dynamic validation and evidence capture |
| Reverse engineering | Static analysis, call-flow tracing, data-flow analysis and code/traffic correlation |
| Bug bounty | Scope parsing, asset inventory, hypothesis generation, validation, evidence, deduplication and reporting |
| Automation | Bounded request plans, credential matrices, authorization matrices, response comparison and artifact generation |

## Methodology

The system follows a staged investigation rather than blindly throwing tools at a target.

```text
                    TARGET
                       │
                       ▼
                 SCOPE / AUTHZ
                       │
                       ▼
                  CASE INIT
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
       STATIC       NETWORK       NATIVE
          │            │            │
          └────────────┼────────────┘
                       ▼
                 CORRELATION
                       │
                       ▼
                  HYPOTHESIS
                       │
                       ▼
             AUTHORIZED VALIDATION
                       │
                       ▼
                    EVIDENCE
                       │
                       ▼
                   FINDING
                       │
                       ▼
                    REPORT
```

### Investigation depth

Escalation is deliberate:

```text
L1  Fingerprint
L2  Static analysis
L3  Data-flow analysis
L4  Native analysis
L5  Runtime instrumentation
L6  Deep investigation
```

A deeper level should be justified by evidence from the previous level. This keeps the workflow fast on simple targets and thorough when the application actually warrants it.

### Evidence loop

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

An unconfirmed scanner alert is not a finding. A plausible bypass is not a finding. A response difference without a sound test fixture is not a finding. The repository is intentionally opinionated about this because bug-bounty reports are judged on evidence, not enthusiasm.

## Code ↔ traffic correlation

One of the central workflows is connecting what the application **does** in code with what it **actually sends** on the wire.

```text
UI / user action
      ↓
API client
      ↓
Endpoint
      ↓
Authentication / token source
      ↓
Serialization
      ↓
Native / JNI boundary
      ↓
Crypto / storage
      ↓
Observed traffic
```

This makes it possible to answer questions such as:

- Where is an endpoint called from?
- Which identity or token reaches the request?
- Which object identifier crosses the trust boundary?
- Is a security decision made client-side or server-side?
- Which native function participates in a sensitive operation?

## Endpoint artifacts

Observed endpoints can be normalized into reusable artifacts:

```text
artifacts/endpoints/
├── endpoint-001.md
├── endpoint-001.py
├── endpoint-001.js
└── endpoint-001.sh
```

Generated scripts are based on **observed or documented request data**. The system must not invent hosts, paths, parameters, authentication headers, secrets or response structures.

Secrets should remain external to the repository and appear only as placeholders in generated artifacts.

## Bug-bounty workflow

```text
PROGRAM
   ↓
SCOPE PARSER
   ↓
TARGET VALIDATION
   ↓
ASSET INVENTORY
   ↓
STATIC / NETWORK ANALYSIS
   ↓
ATTACK-SURFACE MAP
   ↓
HYPOTHESIS ENGINE
   ↓
AUTHORIZED VALIDATION
   ↓
EVIDENCE
   ↓
DEDUPLICATION
   ↓
SEVERITY / CONFIDENCE
   ↓
REPORT
```

The intended use is inside an explicit program scope or another environment where the operator has permission to test the target.

## Repository layout

```text
.
├── SKILL.md                    # Main skill entry point
│
├── agents/                     # Specialized agent contracts
├── workflows/                  # End-to-end investigation workflows
├── schemas/                    # Machine-readable artifact schemas
├── templates/                  # Case, evidence and finding templates
├── scripts/                    # Local validation and analysis helpers
├── tools/                      # Tool adapters and operating notes
├── knowledge/                  # Security and platform playbooks
├── adapters/                   # OpenCode / Qoder integration
└── cases/                      # Local assessment state
```

## Case model

Each assessment is intended to remain reproducible and auditable:

```text
cases/target-001/
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

`scope.json` is a hard gate for active validation. If authorization or scope cannot be established, active testing should stop.

## Installation

The repository is intentionally lightweight. It provides the methodology and orchestration layer while relying on standard security tooling for the actual analysis.

### Quick start

```bash
git clone https://github.com/ny0x696/mobile-security-ai.git
cd mobile-security-ai
python3 --version
python3 -m unittest discover -s tests -v
```

For the complete workstation setup, platform-specific tooling and troubleshooting, see **[INSTALL.md](INSTALL.md)**.

### Recommended tooling

Depending on the target, a serious workstation will typically include:

- Python 3.11+
- Git
- Android SDK / `adb`
- Java 17+
- JADX
- apktool
- Frida / frida-tools
- Ghidra, Rizin or radare2
- Burp Suite or mitmproxy
- macOS/Xcode tooling for iOS runtime work

The repository does not bundle these tools. Use versions appropriate to the assessment environment.

## Authorized test credentials

Authentication and authorization testing should use **dedicated test identities** supplied or approved for the assessment.

The helper layer supports environment-based credentials, for example:

```bash
export MSAI_TEST_OWNER_USERNAME='owner-test@example.invalid'
export MSAI_TEST_OWNER_PASSWORD='REDACTED'
export MSAI_TEST_SECOND_USERNAME='second-test@example.invalid'
export MSAI_TEST_SECOND_PASSWORD='REDACTED'
```

Credential helpers are designed for controlled test identities. They do not implement credential stuffing, password spraying or credential theft.

## Security model

Mobile Security AI is built around several non-negotiable constraints:

1. **Scope before traffic.** Discovery does not automatically grant permission to test a discovered asset.
2. **Evidence before claims.** Scanner output and hypotheses require validation.
3. **Observed data over guesses.** Endpoint artifacts come from application artifacts, captured traffic or documentation.
4. **Bounded validation.** Test plans should be minimal, reproducible and rate-aware.
5. **Secrets stay out of Git.** Credentials, tokens and private keys must be supplied externally and redacted from evidence.
6. **Provenance matters.** Findings should be traceable to the evidence that supports them.
7. **Ambiguity means stop.** If authorization or scope is unclear, do not turn uncertainty into an experiment.

## Finding model

A finding is expected to contain enough information for another security engineer to reproduce and assess it:

```text
Finding
├── Title
├── Asset
├── Endpoint
├── Vulnerability
├── Preconditions
├── Evidence
├── Reproduction
├── Impact
├── Severity
├── Confidence
├── CWE
├── CVSS
└── Report
```

The distinction between **severity** and **confidence** is intentional. A theoretically severe issue with weak evidence should not be presented as a confirmed critical vulnerability.

## Design philosophy

### Evidence first

The system records what was observed before deciding what it means.

### Escalate only when useful

Static analysis often answers the question. Runtime instrumentation is reserved for questions that static evidence cannot settle.

### Automate the boring parts

Parsing, normalization, comparison, artifact generation and case bookkeeping should be deterministic so the operator can spend time on the parts that require judgment.

### Keep the operator in control

The agent can organize an investigation and propose the next useful action. Authorization, scope and consequential validation remain explicit boundaries.

## Status

The repository is under active development. Core agent contracts, workflows, schemas and the first generation of authorized validation helpers are already present. Additional runtime harnesses, endpoint replay, adapters and deeper automation are being developed incrementally.

## License

MIT. See [LICENSE](LICENSE).

## Disclaimer

This project is intended for authorized security testing, research and defensive engineering. You are responsible for obtaining permission before testing a target and for complying with the rules of the applicable program, service or organization.
