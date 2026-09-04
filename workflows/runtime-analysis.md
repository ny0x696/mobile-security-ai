# Runtime Analysis Workflow

## Objective
Use controlled runtime observation to resolve a specific reverse-engineering or security hypothesis on an authorized device, emulator or process.

## Stages

1. Define the hypothesis and the exact observation needed.
2. Verify target identity and authorization before instrumentation.
3. Choose the narrowest instrumentation point.
4. Capture timestamped observations with target/process context.
5. Correlate runtime data with static code locations, endpoints or native symbols.
6. Decide whether the evidence confirms, rejects or leaves the hypothesis inconclusive.
7. Preserve raw observations separately from interpretation.
8. Escalate only when the current evidence cannot resolve the hypothesis.

## Safety rules

- Prefer observation over mutation.
- Avoid persistence, destructive actions, credential collection and unrelated data access.
- Do not broaden the target or test scope because runtime evidence reveals adjacent assets.

## Completion criteria

Every runtime observation has provenance, a defined purpose and a link to the hypothesis it was collected to resolve.
