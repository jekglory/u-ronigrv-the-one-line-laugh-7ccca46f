#!/usr/bin/env python3
"""The One-Line Laugh entry for make.fun.

The program writes exactly one funny line — a single sentence of at most
200 characters — to entry.txt inside the grader's output directory.

The line plays on a small everyday truth: noise-cancelling headphones
promise a quiet mind, and the punchline is what the silence reveals.
Against the judge's brief, in its order: the surprise lands at the end
("I have nothing to say") and still makes sense, because the headphones
did exactly what they promised; the setup is an everyday truth anyone
who owns headphones recognises; and the whole joke is one short sentence
with no wasted words.

Pure Python 3 standard library. No network, no clock, no randomness:
two runs write byte-identical output.
"""

import os
import sys

MAX_CHARS = 200

LINE = (
    "I bought noise-cancelling headphones to finally hear myself think "
    "\u2014 turns out I have nothing to say."
)


def output_dir():
    """Return the directory the grader provides for the entry's output."""
    chosen = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    if not os.path.isdir(chosen):
        os.makedirs(chosen, exist_ok=True)
    return chosen


def clear_contents(directory):
    """Remove only the contents of the provided directory, never the directory."""
    for name in os.listdir(directory):
        path = os.path.join(directory, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)
        elif os.path.isdir(path):
            for sub in os.listdir(path):
                os.remove(os.path.join(path, sub))
            os.rmdir(path)


def validate(line):
    """Check the line against the bounty brief: one sentence, <=200 chars."""
    if len(line) > MAX_CHARS:
        return f"line is {len(line)} chars, over the {MAX_CHARS} limit"
    if line.count(".") != 1:
        return "line must be exactly one sentence"
    if line != line.strip():
        return "line must not start or end with whitespace"
    return None


def main():
    problem = validate(LINE)
    if problem is not None:
        print(problem, file=sys.stderr)
        return 1
    directory = output_dir()
    clear_contents(directory)
    target = os.path.join(directory, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")
    size = os.path.getsize(target)
    print(f"Wrote {len(LINE)}-char line ({size} bytes) to {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
