#!/usr/bin/env python3
"""Office joke entry for the make.fun bounty
"Make the AI Judge Laugh: Office Jokes".

Writes a single one-line joke about office life to /output/entry.txt.
"""

import os

# The joke, kept as parts so the setup and the punchline stay readable
# and independently editable. Joined with a single space at build time.
_SETUP = "I finally got my inbox to zero,"
_PUNCHLINE = "and Outlook celebrated by sending me a congratulatory email."


MAX_LINE_LENGTH = 199


def validate_line(line: str) -> None:
    """Reject a blank or over-long line before anything is written."""
    if not line.strip():
        raise ValueError("joke line must not be blank")
    if len(line) > MAX_LINE_LENGTH:
        raise ValueError(
            f"joke line is {len(line)} chars, over the {MAX_LINE_LENGTH} limit"
        )


def build_line() -> str:
    """Assemble the joke line from its parts."""
    return " ".join([_SETUP, _PUNCHLINE])


def main() -> None:
    line = build_line()
    validate_line(line)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
