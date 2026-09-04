#!/usr/bin/env python3
"""Authorized credential provider.

Credentials are referenced by environment variable or an external local file.
They are never printed, committed, or included in evidence.
"""
from __future__ import annotations
import os
from dataclasses import dataclass

@dataclass(frozen=True)
class TestIdentity:
    name: str
    username_env: str
    password_env: str

    def load(self) -> tuple[str, str]:
        user = os.getenv(self.username_env)
        password = os.getenv(self.password_env)
        if not user or not password:
            raise RuntimeError(f"Missing authorized test credential environment variables: {self.username_env}/{self.password_env}")
        return user, password


def identities_from_env(prefix: str = "MSAI_TEST_") -> list[TestIdentity]:
    result=[]
    for key in sorted(os.environ):
        if key.startswith(prefix) and key.endswith("_USERNAME"):
            name=key[len(prefix):-len("_USERNAME")].lower()
            result.append(TestIdentity(name, key, f"{prefix}{name.upper()}_PASSWORD"))
    return result
