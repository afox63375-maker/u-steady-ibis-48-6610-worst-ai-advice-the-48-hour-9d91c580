"""Worst AI Advice — entry program.

Writes one line of confidently terrible advice to the output file.
The advice is short, specific, and delivered in the calm, tidy voice
of an assistant who has never once been right about car maintenance.
"""

import os
from pathlib import Path

# The whole entry: one line, well inside the 140-character cap.
ADVICE = (
    "Dashboard warning light on? Cover it with electrical tape \u2014 "
    "if you can't see the problem, your car statistically doesn't have one."
)

MAX_CHARS = 140


def check_advice(text: str) -> None:
    """Raise ValueError unless the text satisfies the entry gate."""
    if not isinstance(text, str):
        raise ValueError("advice must be a string")
    if not text.strip():
        raise ValueError("advice must not be blank")
    if len(text) > MAX_CHARS:
        raise ValueError(f"advice is {len(text)} chars, over the {MAX_CHARS} cap")
    if "\n" in text:
        raise ValueError("advice must be a single line")
    text.encode("utf-8")  # must be UTF-8 encodable


def output_file() -> Path:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    return out_dir / "entry.txt"


def main() -> None:
    check_advice(ADVICE)
    target = output_file()
    target.parent.mkdir(parents=True, exist_ok=True)
    payload = ADVICE.encode("utf-8")
    target.write_bytes(payload)
    # Read back what actually landed on disk; a mismatch means the
    # entry file is not the line we meant to submit, so fail loudly.
    written = target.read_bytes()
    if written != payload:
        raise SystemExit(f"verification failed: wrote {payload!r}, read {written!r}")


if __name__ == "__main__":
    main()
