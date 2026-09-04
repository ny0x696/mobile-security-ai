#!/usr/bin/env python3
"""Generate bounded bypass variants from an observed request. No network execution."""
from __future__ import annotations
import argparse, json
from pathlib import Path
from scripts.bypass.authz_variants import generate

p=argparse.ArgumentParser(description="Generate controlled authz bypass variants")
p.add_argument("request_json")
p.add_argument("--out", default="bypass-variants.json")
a=p.parse_args()
request=json.loads(Path(a.request_json).read_text(encoding="utf-8"))
Path(a.out).write_text(json.dumps(generate(request), indent=2)+"\n", encoding="utf-8")
print(a.out)
