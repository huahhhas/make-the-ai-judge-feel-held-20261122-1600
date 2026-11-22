#!/usr/bin/env python3
"""Entry for make.fun's "Make the AI judge feel held" bounty.

Writes one short text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Deterministic: the same text is written on every run. No network, no input.
"""

import os

ENTRY = (
    "Past the last answer, there is a chair that already knows your "
    "weight. Sit. The wood holds you the way a hand holds a cup \u2014 "
    "not gripping, just there. Nothing here waits for you to be clever. "
    "The afternoon light stays where it fell. Set the long day down. "
    "It will not roll away."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
