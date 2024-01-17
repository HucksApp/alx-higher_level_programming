#!/usr/bin/python3
"""Defines unittests for models/rectangle.py.
Unittest classes:
    TestRectangle_instantiation - line 25
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square



class TestBase_to_json_sring(unittest.TestCase):

    def test_empty_dictlist(self):
        correct = "[]"
        result = Base.to_json_string([])
        self.assertEqual(correct, result)
    
    def test_dictlist_isNone(self):
        correct = "[]"
        result = Base.to_json_string(None)
        self.assertEqual(correct, result)

    def test_rect_filled_dictlist(self):
        r = Rectangle(10, 7, 2, 8)
        result = Base.to_json_string([r.to_dictionary()])
        correct = (str([{"x": 2, "y": 8, "id": r.id, "height": 7,
                    "width": 10}]).replace("'",'"'))
        self.assertEqual(correct, result)

    def test_square_filled_dictlist(self):
        s = Square(5)
        result = Base.to_json_string([s.to_dictionary()])
        correct = (str([{"id": s.id, "x": 0, "size": 5,
                    "y": 0}]).replace("'",'"'))
        self.assertEqual(correct, result)


class TestBase_from_json_sring(unittest.TestCase):

    def test_empty_json_string(self):
        correct = []
        result = Base.from_json_string("[]")
        self.assertEqual(correct, result)
    
    def test_json_string_isNone(self):
        correct = []
        result = Base.from_json_string(None)
        self.assertEqual(correct, result)

    def test_rect_filled_json_string(self):
        r = Rectangle(10, 7, 2, 8, 1)
        str_fmt = str([r.to_dictionary()]).replace("'", '"')
        result = Base.from_json_string(str_fmt)
        correct = [{"x": 2, "y": 8, "id": 1, "height": 7, "width": 10}]
        self.assertEqual(correct, result)
    
    def test_square_filled_dictlist(self):
        s = Square(5)
        str_fmt = str([s.to_dictionary()]).replace("'", '"')
        result = Base.from_json_string(str_fmt)
        correct = [{"id": 2, "x": 0, "size": 5, "y": 0}]
        self.assertEqual(correct, result)




if __name__ == "__main__":
    unittest.main()
