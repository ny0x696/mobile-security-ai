#!/usr/bin/env python3
"""Generate non-destructive request variants for authorized differential testing."""
from __future__ import annotations

def generate(request: dict) -> list[dict]:
    variants = [{"name": "baseline", "changes": {}}]
    variants.append({"name": "method_variant", "changes": {"method": request.get("safe_variant_method", "GET")}})
    variants.append({"name": "content_type_variant", "changes": {"content_type": "application/json"}})
    variants.append({"name": "parameter_representation", "changes": {"parameter_variant": "documented_alternative"}})
    variants.append({"name": "normalization_variant", "changes": {"normalization": "documented_equivalent"}})
    return variants
