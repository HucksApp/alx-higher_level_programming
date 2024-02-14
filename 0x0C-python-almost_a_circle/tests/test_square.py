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

    def test_error_args(self):
        with self.assertRaises(ValueError):
            Square(0), Square(-1), Square(4, -1), Square(1, 2, -3)
        with self.assertRaises(TypeError):
            Square("1"), Square(1, "2"), Square(1, 2, "3")


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


class TestSquare__str(unittest.TestCase):

    def test___str_rep(self):
        s = Square(1, 2, 3, 4)
        correct = f"[Square] ({s.id}) 2/3 - 1"
        self.assertEqual(correct, s.__str__())


class TestSquare_to_dictionary(unittest.TestCase):
    """Unittests for testing create method of the Square class."""

    def test_to_dict(self):
        m1 = [[2, 1, 3], [2, 3, 1], [0,2,0]]
        m2 = ["id", "x", "size", "y"]
        s1 = Square(1, 2, 3, 4)
        s2 = Square(3, 2, 1)
        s3 = Square(2)
        for index, s in enumerate([s1, s2, s3]):
            result = s.to_dictionary()
            correct = dict(zip(m2, [s.id, *m1[index]]))
            self.assertDictEqual(correct, result)


class TestSquare_Update(unittest.TestCase):
    """Unittests for testing to_dictionary method of the Rectangle class."""

    def test_update_wrong_args(self):
        s = Square(2, 3, 5)
        with self.assertRaises(ValueError):
            s.update(1, 2, -3), s.update(1, -2),
            s.update(-1), s.update(0)

        with self.assertRaises(TypeError):
            s.update(1, 2, "3"), s.update(1, "2"),
            s.update("1")

    def test_update_diff_args_nums(self):

        m1 = [[9],[7, 5],[6, 4, 2], [8, 2, 3, 4]]
        m2 = ["id", "size", "x", "y"]
        correct = {'id': 1, 'x': 0, 'size': 1, 'y': 0}
        s = Square(1)
        for args in m1:
            index = 0
            s.update(*args)
            result = s.to_dictionary()
            for arg in args:
                correct.update({m2[index] : arg})
                index += 1
            self.assertDictEqual(correct, result)

