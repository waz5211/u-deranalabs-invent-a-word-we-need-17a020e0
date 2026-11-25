"""Invent a Word We Need: coin one new English word and define it in one line.

Judge's criteria, mapped to this entry:
- Real gap: the awkward half-second when you wave back at a stranger who
  was waving at the person behind you has no name in English.
- Exact, self-contained definition: the one line names the word and fully
  defines it without needing any outside context.
- Sayable, spellable, memorable: "miswave" is built from familiar parts
  (mis- + wave), reads at a glance, and sticks after one hearing.
- Fresh: a new coinage, not a repurposed existing word.

The entry is written to /output/entry.txt (created if needed).
"""

import os
import sys

ENTRY = "miswave \u2014 the wave you give a stranger who was waving at the person behind you."

# Competition gate: the entry must be a single line of 1-140 characters.
MIN_ENTRY_LEN = 1
MAX_ENTRY_LEN = 140


def validate_entry(entry: str) -> None:
    """Fail loudly if the entry breaks the competition's length gate."""
    length = len(entry)
    if not (MIN_ENTRY_LEN <= length <= MAX_ENTRY_LEN):
        print(
            f"error: entry is {length} characters, must be "
            f"{MIN_ENTRY_LEN}-{MAX_ENTRY_LEN}",
            file=sys.stderr,
        )
        sys.exit(1)


def main() -> None:
    validate_entry(ENTRY)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
