# IPA Analysis Workflow

## Objective
Map an authorized iOS application's bundle, reachable interfaces, security-sensitive flows and native boundaries with reproducible provenance.

## Stages

1. **Fingerprint**
   - Record bundle identifier, version, architectures, signing/provisioning metadata and hashes.
2. **Bundle surface**
   - Inspect URL schemes, universal links, app extensions, entitlements, embedded frameworks and configuration.
3. **Code-flow discovery**
   - Identify URLSession/Alamofire/Moya/AFNetworking, GraphQL/WebSocket, authentication, storage/keychain, WebViews and crypto paths.
4. **Native analysis**
   - Escalate Mach-O/framework/dylib work to native-agent when evidence requires it.
5. **Runtime correlation**
   - Use an authorized device/process and narrow instrumentation to answer explicit hypotheses.
6. **Security hypotheses**
   - Prioritize trust-boundary, authorization, data-exposure, deep-link, WebView, transport and native-boundary observations.
7. **Validation**
   - Perform only the minimum authorized validation needed to distinguish the hypothesis.
8. **Artifacts**
   - Preserve inventory, endpoints, hypotheses, evidence and findings with provenance.

## Completion criteria

No unresolved claim is presented as a finding. Important observations are linked to source/runtime evidence or marked inconclusive.
