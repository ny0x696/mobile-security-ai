#!/usr/bin/env python3
"""Generate bounded authorization variants for an explicitly authorized request."""
from __future__ import annotations

def generate(request: dict) -> list[dict]:
    variants=[]
    for name, changes in [
        ("owner_identity", {"identity": "owner_test_account"}),
        ("second_identity", {"identity": "secondary_test_account"}),
        ("missing_auth", {"authorization": "<OMIT>"}),
        ("documented_method", {"method": request.get("documented_alternative_method", "GET")}),
    ]:
        variants.append({"name": name, "changes": changes, "destructive": False})
    return variants


def assess(baseline: dict, variant: dict) -> dict:
    access = variant.get("authorized_object_access")
    return {
        "status_changed": baseline.get("status_code") != variant.get("status_code"),
        "access_changed": access != baseline.get("authorized_object_access"),
        "potential_bypass": bool(access) and variant.get("identity") == "secondary_test_account",
        "requires_manual_confirmation": True,
    }
