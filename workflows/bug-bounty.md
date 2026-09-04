# Authorized Bug Bounty Workflow

## Pipeline

`IMPORT PROGRAM -> PARSE SCOPE -> ASSET INVENTORY -> STATIC ANALYSIS -> API DISCOVERY -> ATTACK-SURFACE MAP -> HYPOTHESES -> AUTHORIZED VALIDATION -> EVIDENCE -> DEDUPLICATION -> SEVERITY -> REPORT`

## Scope gate

Do not proceed to active validation until `scope.json` explicitly permits the target and method.

## Discovery

Inventory package identifiers, versions, components, endpoints, protocols, native libraries and trust boundaries. Prefer passive and static discovery first.

## Hypothesis generation

Use concrete observations to prioritize access control, authentication, injection, SSRF, data exposure, business logic, mobile platform boundary and native-security hypotheses.

## Validation

Use the least invasive test that can distinguish the hypothesis. Respect program rate limits and prohibited techniques.

## Evidence

Capture reproducible request/response or application observations and exact source/runtime provenance. Store artifacts under the case directory.

## Reporting

Only confirmed or appropriately qualified findings reach the report stage. Include impact, reproduction, root cause and remediation.
