#!/usr/bin/env python3
"""One Star, Five Stars for the Food — make.fun entry.

Writes a single-sentence, one-star review of planet Earth from an alien
tourist that still slips in a real compliment about the food, to
/output/entry.txt. The entry is a fixed string: deterministic, no network,
no randomness, no input files.
"""

import os

ENTRY = (
    "One star: the gravity flattened my hover-suit, the locals pay for "
    "water, and the sun has no off switch \u2014 but the pho broth was so "
    "good I'd crash-land here again just for one more bowl."
)


def main() -> None:
    # Self-check the gate before writing: one sentence, 1-200 characters.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} characters"
    assert ENTRY.count(".") == 1 and ENTRY.endswith("."), "entry must be one sentence"
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY + "\n")
    print(ENTRY)
    print(f"characters: {len(ENTRY)}")


if __name__ == "__main__":
    main()
