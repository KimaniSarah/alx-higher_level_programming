#!/usr/bin/python3
"""defines a class Student"""


class Student:
    """
    initializes an instance/object Student
    Args:
        last_name: string
        first_name :string
        age: int
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a Student instance
        Args:
            attrs: if attrs is a list of strings, only attributes
            name contain in this list must be retrieved.
        """
        if (type(attrs) == list and all(type(ele) == str for ele in attrs)):
            return {a: getattr(self, a) for a in attrs if hasattr(self, a)}
        else:
            return self.__dict__
