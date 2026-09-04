# API Analysis Workflow

## Objective
Reconstruct and assess an API attack surface from observed application behavior, source code, documentation or authorized traffic.

## Stages

1. **Provenance**
   - Record where every endpoint observation came from: source, documentation, runtime trace or traffic.
2. **Normalization**
   - Represent method, host, path, headers, authentication source, content type, parameters and body/response schemas.
   - Keep unknown values explicitly unknown.
3. **Correlation**
   - Link endpoint → client method → caller → authentication/token source → serialization → native boundary where applicable.
4. **Attack-surface classification**
   - Review authorization, authentication, input handling, data exposure, rate limits, SSRF, CORS, GraphQL/WebSocket and business-logic boundaries.
5. **Hypothesis generation**
   - Create one hypothesis per concrete observation and assign confidence.
6. **Authorized validation**
   - Test only explicitly in-scope assets and methods.
   - Prefer minimal-impact, reversible checks.
7. **Artifact generation**
   - Generate scripts only from observed endpoint data. Secrets must be placeholders and never copied into committed artifacts.
8. **Finding gate**
   - Require reproducible evidence and demonstrated security impact before confirmation.

## Endpoint artifact rule

A generated script must identify its source endpoint artifact and preserve provenance. It must not invent authentication, parameters, headers or response behavior.
