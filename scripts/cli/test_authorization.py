#!/usr/bin/env python3
"""CLI for generating an authorization test matrix. It does not send requests."""
from __future__ import annotations
import argparse, json
from pathlib import Path
from scripts.access_control.authorization_matrix import build_matrix

p=argparse.ArgumentParser(description="Generate an authorized authz test matrix")
p.add_argument("--objects", required=True, help="JSON array of object IDs")
p.add_argument("--identities", required=True, help="JSON array of approved test identity names")
p.add_argument("--out", default="authz-matrix.json")
a=p.parse_args()
objects=json.loads(Path(a.objects).read_text(encoding="utf-8"))
identities=json.loads(Path(a.identities).read_text(encoding="utf-8"))
Path(a.out).write_text(json.dumps(build_matrix(objects, identities), indent=2)+"\n", encoding="utf-8")
print(a.out)
