#!/usr/bin/env python3
import json
import sys


def cmd_tables():
    table = {
        "name": "example_items",
        "description": "Example inventory items emitted by an external Python plugin",
        "primary_key": ["id"],
        "columns": [
            {"name": "id", "type": "utf8"},
            {"name": "tenant", "type": "utf8"},
            {"name": "title", "type": "utf8"},
            {"name": "active", "type": "bool"},
        ],
    }
    print(json.dumps(table), flush=True)


def cmd_sync():
    raw_in = sys.stdin.readline()
    req = json.loads(raw_in) if raw_in.strip() else {}
    tenant = req.get("spec", {}).get("tenant", "default")
    items = [
        {"id": "item-1", "tenant": tenant, "title": "First resource", "active": True},
        {"id": "item-2", "tenant": tenant, "title": "Second resource", "active": False},
    ]
    for item in items:
        msg = {"type": "row", "table": "example_items", "data": item, "parent_id": None}
        print(json.dumps(msg), flush=True)


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "tables"
    if mode == "tables":
        cmd_tables()
    elif mode == "sync":
        cmd_sync()
    else:
        sys.exit(2)

