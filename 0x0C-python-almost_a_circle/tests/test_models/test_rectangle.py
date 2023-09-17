#!/usr/bin/python3
"""test the rectangle class"""
import unittest
import io
from unittest.mock import patch
from io import StringIO
from models.rectangle import Rectangle


class testRectangle(unittest.TestCase):
    def test_rect_dimensions(self):
        rec = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(rec.id, 12)
        self.assertEqual(rec.width, 10)
        self.assertEqual(rec.height, 2)
        self.assertEqual(rec.x, 0)
        self.assertEqual(rec.y, 0)

    def test_width(self):
        """Test that an exception is raised when width is not an integer or <= 0"""
        with self.assertRaises(TypeError):
            Rectangle("1", 4, 0, 0)
        with self.assertRaises(ValueError):
            Rectangle(-1, 3)

    def test_height(self):
        """Test that an exception is raised when height is not an integer or <= 0"""
        with self.assertRaises(TypeError):
            Rectangle(1, "4")
        with self.assertRaises(ValueError):
            Rectangle(1, -3)

    def test_x(self):
        """Test that an exception is raised when x is not an integer or < 0"""
        with self.assertRaises(TypeError):
            Rectangle(1, 4, "2", 0)
        with self.assertRaises(ValueError):
            Rectangle(1, 5, -3, 7)

    def test_y(self):
        """Test that an exception is raised when y is not an integer or < 0"""
        with self.assertRaises(TypeError):
            Rectangle(1, 4, 2, "0")
        with self.assertRaises(ValueError):
            Rectangle(1, 5, 3, -7)

    def test_area(self):
        rect = Rectangle(3, 8)
        self.assertEqual(rect.area(), 24)


    def test_display(self):
        self.rect = Rectangle(3, 2, 1, 1)
        expected_output = "\n ###\n ###\n"
        with io.StringIO() as mock_stdout:
            with patch('sys.stdout', new=mock_stdout):
                self.rect.display()
                output = mock_stdout.getvalue()
                self.assertEqual(output, expected_output)

    def test_str(self):
        """ Test the string representation"""
        rect = Rectangle(3, 4, 1, 1, 7)
        expected_str = "[Rectangle] (7) 1/1 - 3/4"
        self.assertEqual(str(rect), expected_str)
