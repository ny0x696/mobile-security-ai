#!/usr/bin/env python3
"""Turn observed endpoint records into bounded validation plans."""
from __future__ import annotations

def plan(endpoint: dict) -> dict:
    return {
        "endpoint_id": endpoint.get("id"),
        "method": endpoint.get("method", "GET"),
        "host": endpoint.get("host"),
        "path": endpoint.get("path"),
        "provenance": endpoint.get("provenance", []),
        "tests": [
            "baseline",
            "missing_optional_parameters",
            "documented_parameter_variants",
            "documented_method_variant",
            "response_differential",
        ],
        "credential_source": "authorized_test_identity_reference_only",
    }
