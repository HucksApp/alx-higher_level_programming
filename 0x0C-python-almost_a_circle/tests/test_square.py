#!/usr/bin/python3
"""Defines unittests for models/rectangle.py.
Unittest classes:
    TestRectangle_instantiation - line 25
"""
import unittest
from models.base import Base
from models.square import Square



class TestSquare_args(unittest.TestCase):

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
        s1 = Square(1, 2, 3, 1)
        s2 = Square(4, 3, 2, 2)
        self.assertEqual(s1.id, s2.id - 1)


class TestSquare_create(unittest.TestCase):
    """Unittests for testing create method of the Square class."""

    def test_create_obj_type(self):
        correct = Square(1, 2, 3, 4)
        result = Square.create(**(correct.to_dictionary()))
        self.assertIsNot(correct, result)
        self.assertIsInstance(result, Square)


    def test_create_obj_props(self):
        s1 = Square(4, 3, 2, 1)
        s2 = Square.create(**(s1.to_dictionary()))
        correct = s1.to_dictionary()
        result = s2.to_dictionary()
        self.assertDictEqual(correct, result)
        self.assertDictEqual(s1.__dict__, s2.__dict__)


    def test_create_args(self):
        d = {'id': 1, 'size': 2, 'x': 3, 'y': 4 }
        d2 = [1, 2, 3, 4]
        r1 = Square(*d2)
        m = []
        d3 = {}
        index = 0
        for key, value in d.items():
            if value == d2[index]:
                d3.update({key: value})
                m.append(Square.create(**d3))
            index +=1
        former : 'Square' = None
        for obj in m:
            self.assertIsNot(obj, r1)
            self.assertIsInstance(obj, Square)
            result = [*obj.to_dictionary()]
            result.sort()
            correct = [*d]
            correct.sort()
            self.assertEqual(result, correct)
            if not former:
                former = obj
                continue
            self.assertIsNot(former, obj)
        
