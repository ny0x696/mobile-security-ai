#!/usr/bin/env python3
"""Generate an authorization comparison plan for accounts/objects explicitly supplied by the tester."""
from __future__ import annotations

def build_matrix(objects: list[str], identities: list[str]) -> list[dict]:
    return [{"identity": identity, "object": obj, "expected_owner": identity == objects[0] if objects else False}
            for identity in identities for obj in objects]


def analyze_pair(owner_response: dict, other_response: dict) -> dict:
    return {
        "owner_status": owner_response.get("status_code"),
        "other_status": other_response.get("status_code"),
        "body_changed": owner_response.get("body_hash") != other_response.get("body_hash"),
        "requires_review": other_response.get("status_code") in {200, 201, 202, 204},
        "conclusion": "potential_authorization_difference" if other_response.get("status_code") in {200,201,202,204} else "no_obvious_access",
    }
