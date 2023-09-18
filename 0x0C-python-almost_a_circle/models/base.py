#!/usr/bin/python3
"""defines base class"""
import json


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Args:
            list_dictionaries: is a list of dictionaries
        Return:
            the JSON string representation of list_dictionaries
        """
        if not list_dictionaries:
            return "[]"
        else:
            json_rep = json.dumps(list_dictionaries)
            return json_rep

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        Args:
            cls:the class
            list_obj:a list of instances who inherits of Base
            example: list of Rectangle or list of Square instances
        Return:
            the json string
        """
        if not list_objs:
            list_objs = []
        filename = f"{cls.__name__}.json"
        object_list = [obj.to_dictionary() for obj in list_objs]
        json_file = cls.to_json_string(object_list)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(json_file)
