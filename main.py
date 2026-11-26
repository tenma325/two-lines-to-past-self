#!/usr/bin/env python3
"""Entry for make.fun: Two Lines to Your Past Self.

The entry is two lines of advice addressed to a past self,
and both lines are about one deploy. Never deploy at six in
the evening on the Friday before the holiday weekend: that
single evening cost a weekend, a rollback, and the last of
a person's faith in quick fixes. The first line is the rule,
the second line is the receipt, and anyone who has ever
watched a dashboard turn red at 6:05 PM already knows why
the rule exists and why it is written in the past tense,
in bold, on the wall above the deploy button.

Running this program writes the entry to /output/entry.txt,
falling back to ./output/entry.txt when /output is not
writable, and prints it to stdout as well.
"""

from pathlib import Path

ENTRY_TEXT = (
    "Never deploy at 6PM on the Friday before the holiday weekend.\n"
    "That one evening cost me a weekend, a rollback, and the last "
    "of my faith in quick fixes."
)

# The rule is short because the lesson was expensive: one
# evening bought a weekend of incident calls and a rollback.
DEPLOY_HOUR_OF_REGRET = 18


def render_entry() -> str:
    """Return the two lines exactly as the past self receives them."""
    return ENTRY_TEXT


def is_two_lines(text: str) -> bool:
    """Confirm the advice is two lines and within the cap."""
    return text.count("\n") == 1 and len(text) <= 220


def write_entry(text: str) -> Path:
    """Write the entry text to the output file and return its path."""
    out_dir = Path("/output")
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
        target = out_dir / "entry.txt"
        target.write_text(text + "\n", encoding="utf-8")
        return target
    except OSError:
        out_dir = Path("output")
        out_dir.mkdir(parents=True, exist_ok=True)
        target = out_dir / "entry.txt"
        target.write_text(text + "\n", encoding="utf-8")
        return target


def main() -> None:
    text = render_entry()
    assert is_two_lines(text), "the advice must be two lines"
    write_entry(text)
    print(text)


if __name__ == "__main__":
    main()
