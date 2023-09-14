#!/usr/bin/python3
"""tests the base class"""
import unittest
from models.base import Base


class test_base(unittest.TestCase):
    def test_ifNone(self):
        base_inst = Base()
        self.assertEqual(base_inst._Base__nb_objects, 1)
    def test_noNone(self):
        base_instance = Base(12)
        self.assertEqual(base_instance._Base__nb_objects, 1)
