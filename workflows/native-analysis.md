# Native Analysis Workflow

## Objective
Analyze authorized native binaries and native application boundaries when higher-level evidence points to native code.

## Stages

1. Fingerprint format, architecture, libraries, imports/exports and symbols.
2. Locate security-sensitive strings, functions, parsers, serialization and cryptographic operations.
3. Map callers and callees around the relevant trust boundary.
4. Identify JNI/ObjC/Swift/native crossings and data transformations.
5. Form hypotheses from concrete code paths.
6. Use runtime instrumentation only when static evidence is insufficient.
7. Validate minimally and preserve reproducible evidence.
8. Link native evidence back to the originating application flow or endpoint.

## Tool routing

Use Ghidra, IDA, radare2 or rizin according to availability and case requirements. Tool output is evidence only after its provenance and interpretation are recorded.

## Safety

Do not turn reverse engineering into persistence, destructive exploitation or unauthorized access. Keep analysis bounded to the authorized sample and scope.
