#!/usr/bin/env python3
"""Office joke entry for the make.fun bounty
"Make the AI Judge Laugh: Office Jokes".

Writes a single one-line joke about office life to /output/entry.txt.
"""

import os

LINE = "I finally got my inbox to zero, and Outlook celebrated by sending me a congratulatory email."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
