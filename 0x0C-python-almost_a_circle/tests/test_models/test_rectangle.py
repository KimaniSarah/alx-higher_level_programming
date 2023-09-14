#!/usr/bin/python3
"""test the rectangle class"""
import unittest
from models.rectangle import Rectangle


class testRectangle(unittest.TestCase):
    def Noneis(self):
        instance =  Rectangle(10, 2)
        instance2 = Rectangle(10, 2, 0, 0, 12)

        self.assertEqual(instance._Rectangle__nb_objects, 1)
        self.assertEqual(instance2._Rectangle__nb_objects, 1)
