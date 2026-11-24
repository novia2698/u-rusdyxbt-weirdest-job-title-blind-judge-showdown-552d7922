#!/usr/bin/env python3
"""Weirdest Job Title entry.

Writes a single job title to /output/entry.txt. The title is a fixed
string, so every run produces exactly the same bytes.
"""

import os

TITLE = "Senior Vice President of Apologizing to Geese"

# The gate requires 1-60 characters of UTF-8 text, no trailing newline.
assert 1 <= len(TITLE.encode("utf-8")) <= 60


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TITLE)


if __name__ == "__main__":
    main()
