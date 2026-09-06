#!/usr/bin/env python3
"""
case_doc_tracker.py
Tracks documentation status for a case against a checklist you define.

Usage:
    python case_doc_tracker.py checklist.json -o status_report.md

Input (checklist.json) — SYNTHETIC EXAMPLE:
{
  "case_id": "CASE-2026-0091",
  "items": [
    {"category": "Government-issued ID", "collected": true, "notes": "Received via email 3/2"},
    {"category": "Last 3 months account statements", "collected": true, "notes": ""},
    {"category": "Proof of address", "collected": false, "notes": "Requested 3/5, no response yet"},
    {"category": "Correspondence log", "collected": false, "notes": ""}
  ]
}
"""

import json
import argparse
from datetime import datetime, timezone


def build_report(data):
    items = data.get("items", [])
    collected = [i for i in items if i.get("collected")]
    outstanding = [i for i in items if not i.get("collected")]

    lines = [f"# Documentation Status — {data.get('case_id', 'Unknown Case')}", ""]
    lines.append(f"Generated: {datetime.now(timezone.utc).isoformat()}")
    lines.append(f"Progress: {len(collected)}/{len(items)} collected")
    lines.append("")

    lines.append("## ✅ Collected")
    if collected:
        for i in collected:
            note = f" — {i['notes']}" if i.get("notes") else ""
            lines.append(f"- {i['category']}{note}")
    else:
        lines.append("_None yet._")
    lines.append("")

    lines.append("## ⬜ Outstanding")
    if outstanding:
        for i in outstanding:
            note = f" — {i['notes']}" if i.get("notes") else ""
            lines.append(f"- {i['category']}{note}")
    else:
        lines.append("_Nothing outstanding._")

    return "\n".join(lines)


def build_shareable_summary(data):
    items = data.get("items", [])
    collected = [i["category"] for i in items if i.get("collected")]
    outstanding = [i["category"] for i in items if not i.get("collected")]
    case_id = data.get("case_id", "Unknown Case")

    lines = [f"Case {case_id} — Documentation Status", ""]
    lines.append("Still needed from customer:")
    lines += [f"- {c}" for c in outstanding] if outstanding else ["- Nothing outstanding"]
    lines.append("")
    lines.append("Already received:")
    lines += [f"- {c}" for c in collected] if collected else ["- Nothing yet"]

    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description="Generate a documentation status report from a checklist.")
    ap.add_argument("input", help="Path to checklist JSON file")
    ap.add_argument("-o", "--output", default="status_report.md")
    ap.add_argument("--summary", help="Optional path to also write a plain-text shareable summary")
    args = ap.parse_args()

    with open(args.input) as f:
        data = json.load(f)

    report = build_report(data)
    with open(args.output, "w") as f:
        f.write(report)
    print(f"Report written to {args.output}")

    if args.summary:
        summary = build_shareable_summary(data)
        with open(args.summary, "w") as f:
            f.write(summary)
        print(f"Shareable summary written to {args.summary}")


if __name__ == "__main__":
    main()
