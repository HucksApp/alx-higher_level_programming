#!/usr/bin/python3
"""Defines unittests for models/rectangle.py.
Unittest classes:
    TestRectangle_instantiation - line 25
"""
import unittest
from models.base import Base
from models.square import Square



class TestSquare(unittest.TestCase):

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_one_arg(self):
        s1 = Square(1)
        self.assertIsInstance(s1, Square)

    def test_two_args(self):
        s1 = Square(10, 2)
        s2 = Square(2, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def test_three_args(self):
        s1 = Square(2, 2, 4)
        s2 = Square(4, 4, 2)
        self.assertEqual(s1.id, s2.id - 1)

    def test_four_args(self):
        s1 = Square(1, 2, 3, 4)
        s2 = Square(4, 3, 2, 1)
        self.assertEqual(s1.id, s2.id - 1)
