#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse — make.fun entry.

Writes one line (at most 140 characters) to /output/entry.txt:
the funniest excuse a robot vacuum could offer for missing a spot.
"""

import os

LINE = "I didn't miss that spot. I left one crumb behind as a warning to the others — my sensors confirm the dust is terrified."


def main():
    assert 1 <= len(LINE) <= 140, "entry line must be 1-140 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
