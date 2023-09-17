#!/usr/bin/python3
"""test for the square class that inherits from Rectangle"""
import unittest
import io
from unittest.mock import patch
from models.square import Square
from models.rectangle import Rectangle


class test_square(unittest.TestCase):
    def test_para(self):
        S1 = Square(5, 0, 0, 1)
        self.assertEqual(S1.width, 5)
        self.assertEqual(S1.x, 0)
        self.assertEqual(S1.y, 0)
        self.assertEqual(S1.id, 1)

    def test_area(self):
        S3 = Square(5, 0, 0)
        self.assertEqual(S3.area(), 25)

    def test_str(self):
        S2 = Square(4, 1, 1, 2)
        exp = "[Square] (2) 1/1 - 4"
        self.assertEqual(str(S2), exp)

    def test_display(self):
        self.rect = Rectangle(3, 2, 1, 1)
        expected_output = "\n ###\n ###\n"
        with io.StringIO() as mock_stdout:
            with patch('sys.stdout', new=mock_stdout):
                self.rect.display()
                output = mock_stdout.getvalue()
                self.assertEqual(output, expected_output)
