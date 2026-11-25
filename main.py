"""Write one funny, true line reviewing the most boring everyday object.

Entry for make.fun's "The Most Boring Object, Reviewed in One Line" bounty
(slug u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3).

The program writes exactly one review line to /output/entry.txt. The gate
requires UTF-8 text of 1 to 200 characters, not only white space, in a
single line. Standard library only.
"""

import os
import sys

ENTRY = (
    "The doorstop has held this door open since 2019. It has never been "
    "thanked, moved, or noticed \u2014 the most reliable employee here, "
    "and the only one who never asked for a raise."
)

MAX_CHARS = 200


def validate(text):
    """Return an error string, or None when the entry passes the gate."""
    if not text or not text.strip():
        return "entry must not be empty or only whitespace"
    if len(text) > MAX_CHARS:
        return "entry is %d characters, over the %d limit" % (len(text), MAX_CHARS)
    if "\n" in text or "\r" in text:
        return "entry must be a single line"
    return None


def resolve_output_path(argv):
    if len(argv) > 1:
        return argv[1]
    return os.path.join(os.sep + "output", "entry.txt")


def main(argv):
    error = validate(ENTRY)
    if error is not None:
        sys.stderr.write("gate error: %s\n" % error)
        return 1
    path = resolve_output_path(argv)
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    tmp_path = path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)
    os.replace(tmp_path, path)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
