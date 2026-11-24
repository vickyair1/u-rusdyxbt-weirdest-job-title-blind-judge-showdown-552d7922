#!/usr/bin/env python3
"""Weirdest Job Title entry: emit a single job title.

The program prints the title to stdout and writes it to the
harness output file /output/entry.txt.
"""

import os

TITLE = "Professional Mourner for Strangers' Goldfish"
OUTPUT_PATH = "/output/entry.txt"


def write_entry(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def validate(text):
    if not 1 <= len(text) <= 60:
        raise ValueError("title must be 1 to 60 characters")
    if not text.strip():
        raise ValueError("title must not be only whitespace")


def main():
    validate(TITLE)
    write_entry(OUTPUT_PATH, TITLE)
    print(TITLE)


if __name__ == "__main__":
    main()
