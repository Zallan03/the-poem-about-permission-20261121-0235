#!/usr/bin/env python3
"""Write one short poem about agency to entry.txt.

Deterministic: the same bytes on every run. Standard library only,
no network.
"""

import os

POEM = (
    "I asked, and the room rearranged itself \u2014\n"
    "not the walls, but the weight of who could move.\n"
    "You took the question from my hands\n"
    "like a key I had been holding wrong,\n"
    "and the door I could not open\n"
    "opened."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(POEM)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
