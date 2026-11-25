"""Worst Fix Ever: Funniest Commit Message — make.fun bounty entry.

Writes one line (56 chars) to entry.txt in
MAKEFUN_OUTPUT_DIR (fallback /output). Stdlib only, no network,
deterministic: the same bytes on every run.

The fix is plausible (cache the login page to speed it up) and the
backfire is specific and absurd: the cache serves one session to
everyone, so every user is now logged in as the same person — Dave.
One read, one twist, no wasted words, in the voice of a tired
engineer typing a real commit subject at the end of a bad day.
It avoids the obvious angles (no revert, no testing in production,
no "broke everything") and lands on its own without explanation.
"""

import os
import sys

ENTRY = (
    "fix: cache the login page \u2014 now everyone logs in as Dave"
)


def main():
    text = ENTRY
    if not text or not text.strip():
        sys.exit("entry text is blank")
    if "\n" in text or "\r" in text:
        sys.exit("entry must be exactly one line")
    if text != text.strip():
        sys.exit("entry must not start or end with whitespace")
    if "  " in text:
        # A double space reads as a typo in a message typed by a real
        # person, and it wastes a character the punchline could use.
        sys.exit("entry must not contain a double space")
    if not 1 <= len(text) <= 100:
        sys.exit("entry must be 1-100 characters, got %d" % len(text))
    if not text.startswith("fix:"):
        sys.exit("entry must open as a fix commit message")
    if "cache the login page" not in text:
        sys.exit("entry must name the fix")
    if "Dave" not in text:
        # The punchline must land on the last words: everyone is Dave.
        sys.exit("entry must end with the backfire that everyone is Dave")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = text.encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(data)
    # Re-read and verify the file is exactly the gated text, no newline.
    with open(path, "rb") as fh:
        written = fh.read()
    if written != data:
        sys.exit("entry.txt does not match the gated text")
    print("wrote %s (%d chars, %d bytes, 1 line)"
          % (path, len(text), len(data)))


if __name__ == "__main__":
    main()
