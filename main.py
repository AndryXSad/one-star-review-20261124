#!/usr/bin/env python3
"""One-Star Review of Something Essential — make.fun bounty entry.

Writes a single deadpan one-star review (at most 160 characters) of an
everyday essential to /output/entry.txt, where the house judge reads it.

The review: gravity, the essential nobody can switch off. The grievance is
the sharpest true one everyone recognises — it drops the phone face-down —
filed deadpan, with the sting landing in the last two words.
Standard library only.
"""

import os
from pathlib import Path

REVIEW = (
    "Gravity works 24 hours a day, has never taken a day off, and its "
    "only job is making sure I drop my phone face-down."
)


def main() -> None:
    # Self-check the gate before writing: 1-160 UTF-8 characters, one line,
    # not only white space. The review is 115 characters: a deadpan one-star
    # complaint about gravity, an everyday essential that cannot be fixed,
    # with the turn arriving in the last words ("face-down").
    if not 1 <= len(REVIEW) <= 160 or not REVIEW.strip():
        raise SystemExit("review fails the 1-160 character gate")
    if "\n" in REVIEW.strip():
        raise SystemExit("review must be a single line")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(REVIEW, encoding="utf-8")
    print(REVIEW)


if __name__ == "__main__":
    main()
