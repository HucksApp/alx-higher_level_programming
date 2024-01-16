#!/usr/bin/python3
"""Define Rectangle Class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Module Representation of Square
"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization a Square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """module Square size getter
        """
        return self.width

    @size.setter
    def size(self, value):
        """module Square size setter
        """
        if all([hasattr(self, m) for m in ('width', 'height')]):
            setattr(self, 'width', value)
            setattr(self, 'height', value)

    def __str__(self):
        """module string represation of square
        """
        name = self.__class__.__name__
        return "[{}] ({:d}) {:d}/{:d} - {:d}".format(name, self.id,
                                                     self.x, self.y,
                                                     self.width)

    def update(self, *args, **kwargs):
        """module update square
        """
        if args:
            props = ["id", "size", "x", "y"]
            for index, arg in enumerate(args):
                setattr(self, props[index], arg)
        elif kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """retrun dictonary
        """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
