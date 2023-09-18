#!/usr/bin/python3
"""tests the base class"""
import unittest
import json
from models.rectangle import Rectangle
from models.base import Base


class test_base(unittest.TestCase):
    def test_ifNone(self):
        base_inst = Base()
        self.assertEqual(base_inst._Base__nb_objects, 1)

    def test_noNone(self):
        base_instance = Base(12)
        self.assertEqual(base_instance._Base__nb_objects, 2)

    def test_json(self):
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        expected = {'x': 2, 'width': 10, 'id': 2, 'height': 7, 'y': 8}
        expected_list = [{"x": 2, "width": 10, "id": 2, "height": 7, "y": 8}]
        parsed_json_list = json.loads(json_dictionary)
        """change to python so as to compare even if they are not in order"""
        self.assertEqual(dictionary, expected)
        self.assertIsInstance(dictionary, dict)
        self.assertEqual(parsed_json_list, expected_list)
        self.assertIsInstance(json_dictionary, str)
