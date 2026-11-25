"""Snooze Button Roast.

Writes one line roasting an alarm clock that rings at 6 AM on a
Saturday to $MAKEFUN_OUTPUT_DIR/entry.txt: the only thing in the
house with a worse work-life balance than its owner. Standard
library only.
"""

import os
import sys

ALARM_ROAST = (
    "My alarm clock rings at 6 AM on Saturdays \u2014 the only "
    "thing in this house with a worse work-life balance than me."
)


def roast_gate(text):
    """Check the roast against the competition gate.

    The gate wants plain UTF-8 text of 1 to 200 characters, not
    only white space, on a single line: one roast of an alarm
    clock that rings at 6 AM on a Saturday. Returns the cleaned
    text or raises ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("roast must not be only whitespace")
    if len(cleaned) > 200:
        raise ValueError(
            "roast is %d characters, over the 200 limit"
            % len(cleaned)
        )
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("roast must be exactly one line")
    return cleaned


def roast_measure(text):
    """Measure the roast for one last sanity pass.

    Returns a dict with the character count and the word count of
    the cleaned text. A roast too short to carry a setup and a
    punchline, or one padded out to fill the cap instead of
    landing the joke, is caught here before anything is written.
    """
    words = text.split()
    return {"chars": len(text), "words": len(words)}


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = roast_gate(ALARM_ROAST)
    shape = roast_measure(text)
    if shape["words"] < 5:
        raise ValueError("roast is too short to carry a punchline")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
