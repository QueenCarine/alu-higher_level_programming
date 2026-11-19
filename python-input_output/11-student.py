#!/usr/bin/python3
"""Module that defines a Student class that can be saved and reloaded."""


class Student:
    """Class representing a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student with first name, last name and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the dictionary representation of the student.

        If attrs is a list of strings, only those attributes are kept.
        """
        if type(attrs) is list and all(type(a) is str for a in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace the attributes of the student using a dictionary."""
        for key, value in json.items():
            setattr(self, key, value)
