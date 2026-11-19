#!/usr/bin/python3
"""Module that defines inherits_from, a strict subclass check."""


def inherits_from(obj, a_class):
    """Return True if obj's class inherited from a_class, not equal to it."""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
