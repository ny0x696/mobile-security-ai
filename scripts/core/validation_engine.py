#!/usr/bin/env python3
"""Shared validation primitives. Network execution is intentionally opt-in and external."""
from __future__ import annotations
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from .scope_engine import check_request

@dataclass
class TestResult:
    test_id: str
    url: str
    method: str
    status: str
    baseline: dict
    variant: dict
    differences: list[str]
    evidence_refs: list[str]
    note: str = ""
    timestamp: str = ""

    def json(self):
        if not self.timestamp:
            self.timestamp = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
        return asdict(self)


def gate(scope: dict, url: str, method: str) -> tuple[bool, str]:
    return check_request(scope, url, method)


def compare_response(baseline: dict, variant: dict) -> list[str]:
    differences = []
    if baseline.get("status_code") != variant.get("status_code"):
        differences.append("status_code")
    if baseline.get("authenticated") != variant.get("authenticated"):
        differences.append("authenticated")
    if baseline.get("body_hash") != variant.get("body_hash"):
        differences.append("body_hash")
    if baseline.get("content_type") != variant.get("content_type"):
        differences.append("content_type")
    return differences
