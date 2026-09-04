# Validation Scripts

Dependency-free Python utilities for authorized mobile/API security research.

## Design

Scripts are evidence-first and scope-gated. They build test matrices, compare captured results, extract structure from supplied artifacts, and preserve reproducibility. They do not perform credential stuffing, secret theft, persistence, destructive exploitation, or out-of-scope scanning.

## Current modules

- `core/scope_engine.py`: hard allowlist gate for active testing.
- `core/validation_engine.py`: baseline/variant comparison primitives.
- `auth/login_probe.py`: login test matrix using approved test credentials.
- `access_control/authorization_matrix.py`: owner/non-owner authorization comparison.
- `bypass/variant_generator.py`: controlled differential-test variants.
- `extraction/response_extractor.py`: structure/URL/identifier extraction from captured responses.
- `api/response_diff.py`: response metadata differential analysis.

## Example

```bash
python scripts/auth/login_probe.py captured-login.json
python scripts/extraction/response_extractor.py response.json
```

Active requests should be executed only by an explicitly authorized harness after `scope_engine` permits the target. Raw credentials and secrets must never be committed to the case repository.
