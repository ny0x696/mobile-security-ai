#!/usr/bin/env python3
"""Build a login test matrix from an observed request. Does not perform credential attacks."""
from __future__ import annotations

def build_matrix(request: dict) -> list[dict]:
    required = request.get("required_fields", [])
    base = {"name": "baseline", "changes": {}}
    cases = [base]
    for field in required:
        cases.append({"name": f"missing_{field}", "changes": {field: "<OMIT>"}})
        cases.append({"name": f"empty_{field}", "changes": {field: ""}})
    cases += [
        {"name": "invalid_credentials_authorized_test_account", "changes": {"credential_source": "approved_test_account"}},
        {"name": "invalid_content_type", "changes": {"content_type": "controlled_variant"}},
    ]
    return cases

if __name__ == "__main__":
    import argparse, json
    p = argparse.ArgumentParser()
    p.add_argument("request_json")
    args = p.parse_args()
    data = json.load(open(args.request_json, encoding="utf-8"))
    print(json.dumps(build_matrix(data), indent=2))
