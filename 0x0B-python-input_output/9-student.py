#!/usr/bin/python
"""a class that defines a student"""


class Student:
    """
    defines student ,initializes the instance Student
        Args:
            first_name:
            last_name:
            age:
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        Student_dict = {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age
                }
        return Student_dict
