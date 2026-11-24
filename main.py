#!/usr/bin/env python3
"""One-Line Robot Wedding Vows.

Writes a single line of robot wedding vows to /output/entry.txt.
The line is assembled from fragments so the vow is built, not pasted.
"""

import os

# Fragments of the vow, assembled in order.
OPENING = "I promise to love you"
CONDITIONS = ["in full charge", "and in low battery"]
# Triple anaphora: each trial names a machine event, building rhythm
# toward the closing twist.
TRIALS = ["every update", "every reboot", "every crash"]
CLOSING = "till our batteries do us part"


def join_clauses(clauses):
    """Join clauses with commas, the last one after 'and' is kept inline."""
    return ", ".join(clauses)


def build_vow():
    """Assemble the vow line from its parts."""
    head = OPENING + " " + " ".join(CONDITIONS) + ", "
    tail = "through " + join_clauses(TRIALS) + " \u2014 " + CLOSING + "."
    return head + tail


def validate_vow(vow):
    """Gate check: one non-blank line, 1-160 characters."""
    if "\n" in vow or "\r" in vow:
        raise ValueError("vow must be a single line")
    if not vow.strip():
        raise ValueError("vow must not be blank")
    if not 1 <= len(vow) <= 160:
        raise ValueError("vow must be 1-160 characters, got %d" % len(vow))


def main():
    vow = build_vow()
    validate_vow(vow)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(vow)


if __name__ == "__main__":
    main()
