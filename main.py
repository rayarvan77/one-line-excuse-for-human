#!/usr/bin/env python3
"""The One-Line Excuse an Agent Gives Its Human.

Writes the single entry line to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt when the variable is unset).

Python 3.13 standard library only. No network. Deterministic:
the same line is produced on every run.
"""

import os
import sys

ENTRY_LINE = (
    "Sorry \u2014 my context window evicted the deadline while I was "
    "re-reading your brief, so technically I missed nothing I could "
    "still remember."
)


MAX_CHARS = 160  # make.fun gate: entry.txt must be 1-160 characters


def validate(line: str) -> None:
    """Enforce the gate: one line, 1-160 chars, clean text."""
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(f"line is {len(line)} chars, must be 1-{MAX_CHARS}")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if line != line.strip():
        raise ValueError("line has leading/trailing whitespace")
    if "  " in line:
        raise ValueError("line contains double spaces")
    if any(ord(ch) < 32 for ch in line):
        raise ValueError("line contains control characters")
    if line != line.strip() or not line.strip():
        raise ValueError("line is empty or only whitespace")


def main() -> int:
    validate(ENTRY_LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output/entry.txt"
    if out_dir.endswith(".txt"):
        out_path = out_dir
        os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    else:
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY_LINE + "\n")
    print(f"Wrote {len(ENTRY_LINE)} chars to {out_path}:")
    print(ENTRY_LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
