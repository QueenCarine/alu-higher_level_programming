#!/usr/bin/python3
"""Module that defines write_file, which writes a string to a file."""


def write_file(filename="", text=""):
    """Write text to a UTF8 file and return the characters written."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
