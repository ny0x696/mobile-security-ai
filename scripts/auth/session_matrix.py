#!/usr/bin/env python3
"""Build a session/authentication test plan from explicitly supplied test identities."""
from __future__ import annotations

def build(identities: list[str], endpoints: list[dict]) -> list[dict]:
    return [
        {"identity": identity, "endpoint_id": ep["id"], "operation": ep.get("method", "GET"), "mode": "authorized_session"}
        for identity in identities for ep in endpoints
    ]


def compare_sessions(owner: dict, other: dict) -> dict:
    return {
        "owner_authenticated": bool(owner.get("authenticated")),
        "other_authenticated": bool(other.get("authenticated")),
        "status_changed": owner.get("status_code") != other.get("status_code"),
        "body_changed": owner.get("body_hash") != other.get("body_hash"),
        "review": "possible_authz_issue" if other.get("authenticated") and other.get("authorized_object_access") else "no_conclusion",
    }
