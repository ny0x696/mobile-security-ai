#!/usr/bin/env python3
"""Hard scope gate. Intended for authorized security testing only."""
from __future__ import annotations
from urllib.parse import urlparse


def _host(url: str) -> str:
    return (urlparse(url).hostname or "").lower().rstrip(".")


def host_allowed(host: str, rules: list[str]) -> bool:
    host = host.lower().rstrip(".")
    for rule in rules:
        r = rule.lower().strip().lstrip(".")
        if host == r or host.endswith("." + r):
            return True
    return False


def check_request(scope: dict, url: str, method: str = "GET") -> tuple[bool, str]:
    if scope.get("active_testing") is not True:
        return False, "active_testing is not explicitly enabled"
    host = _host(url)
    allowed = scope.get("allowed_hosts", [])
    if not host or not host_allowed(host, allowed):
        return False, f"host outside allowed_hosts: {host or '<invalid>'}"
    methods = [m.upper() for m in scope.get("allowed_methods", ["GET"])]
    if method.upper() not in methods:
        return False, f"method not allowed: {method.upper()}"
    return True, "allowed"
