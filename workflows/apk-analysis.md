# APK Analysis Workflow

## Objective
Build a reproducible Android attack-surface and code-flow map from an APK, AAB-derived APK set, DEX/JAR or unpacked application.

## Stages

1. **Fingerprint**
   - Identify package name, version, min/target SDK, architectures and signing metadata.
   - Record hashes and acquisition provenance.
2. **Manifest surface**
   - Enumerate activities, services, receivers, providers, permissions and intent filters.
   - Flag exported components and externally reachable entry points for evidence-backed review.
3. **Code and data-flow discovery**
   - Locate network clients, authentication/token handling, serialization, WebViews, deep links, sensitive storage and JNI boundaries.
   - Trace important flows from entry point to security-sensitive sink.
4. **Native boundary**
   - Inventory `.so` libraries and JNI methods.
   - Escalate to native-agent only when static evidence justifies it.
5. **Runtime correlation**
   - Use ADB/Frida only for an authorized target and only to answer a defined hypothesis.
   - Correlate runtime observations with static locations and traffic.
6. **Security hypotheses**
   - Generate hypotheses from observations, not generic scanner output.
   - Prioritize externally reachable and high-impact trust-boundary crossings.
7. **Validation**
   - Apply the smallest authorized test capable of confirming or rejecting each hypothesis.
8. **Artifacts**
   - Update `inventory.json`, `endpoints.json`, `hypotheses.json`, `evidence.json` and findings only when supported.

## Completion criteria

The workflow is complete when the application surface is mapped, important flows have provenance, hypotheses are resolved or explicitly marked inconclusive, and confirmed findings contain reproducible evidence.
