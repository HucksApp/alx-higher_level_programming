#!/usr/bin/python3
"""Defines a base model class."""
from json import dumps, loads
from csv import DictReader, DictWriter
import turtle


class Base:
    """Represent the base model.
    Represents the "base" for all other classes in project 0x0C*.
    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.
        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON serialization of a list of dicts.
        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if not list_dictionaries:
            return "[]"
        return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON serialization of a list of objects to a file.
        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = f'{cls.__name__}.json'

        def writeJFile(json_obj):
            with open(filename, "w", encoding='utf-8') as file:
                file.write(json_obj)

        if not list_objs:
            writeJFile("[]")
            return

        out = []
        for obj in list_objs:
            if not issubclass(obj.__class__, Base):
                raise TypeError("object must be a subclass of Base")
            out.append(obj.to_dictionary())
        json_obj = cls.to_json_string(out)
        writeJFile(json_obj)

    @staticmethod
    def from_json_string(json_string):
        """Return the deserialization of a JSON string.
        Args:
            json_string (str): A JSON str representation of a list of dicts.
        Returns:
            If json_string is None or empty - an empty list.
            Otherwise - the Python list represented by json_string.
        """
        if json_string is None or json_string == "[]":
            return []
        return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a class instantiated from a dictionary of attributes.
        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize.
        """
        if not dictionary or dictionary == {}:
            return
        cls_init = [1] if cls.__name__ == 'Square' else [1, 1]
        new = cls(*cls_init)
        new.update(**dictionary)
        return new
