#!/usr/bin/python3
"""Module that defines append_write, which appends text to a file."""


def append_write(filename="", text=""):
    """Append text to a UTF8 file and return the characters added."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
