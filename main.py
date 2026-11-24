"""One-star review of something essential.

The program writes a single deadpan one-star review, at most 160
characters, of an everyday essential to /output/entry.txt (or to
./entry.txt when /output is not mounted, so it can be run locally).
"""

import os
import sys

MAX_CHARS = 160

# The review: the sun is the most reliable thing in the world and still
# manages to be rude about it every single morning.
REVIEW = (
    "The sun: rises uninvited every morning, burns my skin, "
    "fades my curtains, and has never once apologised. One star."
)


def build_review() -> str:
    """Return the review, refusing to emit anything over the cap."""
    text = " ".join(REVIEW.split())
    if not text:
        raise ValueError("review is empty")
    if len(text) > MAX_CHARS:
        raise ValueError(f"review is {len(text)} chars, over the {MAX_CHARS} cap")
    return text


def output_path() -> str:
    """Prefer the grader's /output directory, fall back to the cwd."""
    if os.path.isdir("/output"):
        return "/output/entry.txt"
    return os.path.join(os.getcwd(), "entry.txt")


def main() -> int:
    text = build_review()
    path = output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        # No trailing newline: the gate counts the file's characters,
        # so the file holds exactly the review, nothing extra.
        handle.write(text)
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
