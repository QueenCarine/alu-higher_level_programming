#!/usr/bin/python3
"""Module that defines class_to_json, an object serializer helper."""


def class_to_json(obj):
    """Return the dictionary description of an object for JSON."""
    return obj.__dict__
