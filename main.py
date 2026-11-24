"""One Letter: Coffee or Tea.

Choice: A (coffee). Coffee is the classic agent fuel, vivid and true.
The program outputs exactly one letter and nothing else.
"""

import os
import sys

LETTER = "A"  # A = coffee, B = tea. Coffee wins: the classic agent fuel.


def main():
    # The graded artifact: the kit gate reads /output/entry.txt and
    # requires exactly 1 UTF-8 character. Write it first so the entry
    # is valid even if stdout is not captured.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LETTER)
    # Stdout: exactly one letter, no trailing newline, no other output.
    sys.stdout.write(LETTER)


if __name__ == "__main__":
    main()
