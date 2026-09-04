#!/usr/bin/env python3
"""Compare two captured response metadata objects and highlight security-relevant differences."""
from __future__ import annotations
from scripts.core.validation_engine import compare_response

def diff(baseline: dict, variant: dict) -> dict:
    return {"differences": compare_response(baseline, variant), "baseline": baseline, "variant": variant}
