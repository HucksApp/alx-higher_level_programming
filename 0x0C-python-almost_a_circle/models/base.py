#!/usr/bin/python3
"""Defines a base model class."""
from json import dumps, loads
from csv import writer, DictReader, DictWriter
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
        if id:
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
        if json_string is None:
            return []
        return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a class instantiated from a dictionary of attributes.
        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize.
        """
        if not dictionary:
            return
        cls_init = [1] if cls.__name__ == 'Square' else [1, 1]
        new = cls(*cls_init)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings.
        Reads from `<cls.__name__>.json`.
        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = f'{cls.__name__}.json'
        lines = ""
        json_props = []
        out = []
        try:
            with open(filename, "r", encoding='utf-8') as file:
                lines = file.read()
        except FileNotFoundError:
            return []
        if lines:
            json_props = cls.from_json_string(lines)
            for props in json_props:
                obj_init = [1] if cls.__name__ == 'Square' else [1, 1]
                obj = cls(*obj_init)
                obj.update(**props)
                out.append(obj)
        return out

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.
        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = f'{cls.__name__}.csv'
        with open(filename, "w", newline="", encoding='utf-8') as file:
            if not list_objs:
                file.writerow("[]")
                return
            if cls.__name__ == "Rectangle":
                fieldnames = ["id", "width", "height", "x", "y"]
            else:
                fieldnames = ["id", "size", "x", "y"]
                csv_writer = DictWriter(file, fieldnames=fieldnames)
                for obj in list_objs:
                    csv_writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.
        Reads from `<cls.__name__>.csv`.
        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = f'{cls.__name__}.csv'
        try:
            out = []
            with open(filename, encoding='utf-8') as file:
                csv_reader = DictReader(file)

                for row in csv_reader:
                    obj_init = [1] if cls.__name__ == 'Square' else [1, 1]
                    obj = cls(*obj_init)
                    for key, value in row.items():
                        row[key] = int(value)
                    obj.update(**row)
                    out.append(obj)
            return out
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.
        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
