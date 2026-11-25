"""Invent a Word We Need: coin one new English word and define it in one line.

The entry is written to /output/entry.txt (created if needed).
"""

import os

ENTRY = "miswave \u2014 the wave you give a stranger who was waving at the person behind you."


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
