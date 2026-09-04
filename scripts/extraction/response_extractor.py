#!/usr/bin/env python3
"""Extract structure from captured responses without attempting unauthorized access."""
from __future__ import annotations
import json, re


def extract(body: str) -> dict:
    result = {"format": "text", "keys": [], "urls": [], "ids": []}
    try:
        obj = json.loads(body)
        result["format"] = "json"
        if isinstance(obj, dict):
            result["keys"] = sorted(obj.keys())
    except json.JSONDecodeError:
        pass
    result["urls"] = sorted(set(re.findall(r"https?://[^\s\"'<>]+", body)))
    result["ids"] = sorted(set(re.findall(r"\b(?:id|user_id|account_id|object_id)[\"']?\s*[:=]\s*[\"']?([A-Za-z0-9_-]{1,80})", body, re.I)))
    return result

if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser(); p.add_argument("response")
    a = p.parse_args()
    print(json.dumps(extract(open(a.response, encoding="utf-8").read()), indent=2))
