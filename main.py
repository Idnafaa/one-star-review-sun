"""One-star review of something essential.

A tiny program for the make.fun bounty of the same name. It writes one
deadpan one-star review, at most 160 characters, of an everyday essential
(the sun) to /output/entry.txt, falling back to ./entry.txt when /output
is not mounted so the program can be run locally too.
"""

import os
import sys

MAX_CHARS = 160

REVIEW = (
    "The sun: rises uninvited every morning, burns my skin, "
    "fades my curtains, and has never once apologised. One star."
)


def review_text() -> str:
    """Return the review, collapsed to one line and within the cap."""
    text = " ".join(REVIEW.split())
    if not text:
        raise ValueError("review is empty")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"review is {len(text)} characters, over the {MAX_CHARS} cap"
        )
    return text


def output_path() -> str:
    """The grader reads /output/entry.txt; locally, use the cwd."""
    if os.path.isdir("/output") and os.access("/output", os.W_OK):
        return "/output/entry.txt"
    return os.path.join(os.getcwd(), "entry.txt")


def main() -> int:
    text = review_text()
    path = output_path()
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    # No trailing newline: the gate counts the file's characters, so the
    # file holds exactly the review and nothing extra.
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
