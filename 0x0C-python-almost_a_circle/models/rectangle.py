#!/usr/bin/python3
'''
    Class Rectangle
'''
from models.base import Base


class Rectangle(Base):
    '''
        Defining the Rectangle class
        Inherits from:
            Base
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''
            Returning private attribute
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
            Setting private attribute
        '''
        self.setter_validation("width", value)
        self.__width = value

    @property
    def height(self):
        '''
            Returning private attribute
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
            Setting private attribute
        '''
        self.setter_validation("height", value)
        self.__height = value

    @property
    def x(self):
        '''
            Returning private attribute
        '''
        return self.__x

    @x.setter
    def x(self, value):
        '''
            Setting private attribute
        '''
        self.setter_validation("x", value)
        self.__x = value

    @property
    def y(self):
        '''
            Returning private attribute
        '''
        return self.__y

    @y.setter
    def y(self, value):
        '''
            Setting private attribute
        '''
        self.setter_validation("y", value)
        self.__y = value

    def area(self):
        '''
            Returns the area of the rectangle
        '''
        return (self.height * self.width)

    def display(self):
        '''
            Prints to stdout the representation of the rectangle
        '''
        print('\n' * self.__y, end='')  # y offset
        for y in range(self.__height):
            print(' ' * self.__x, end='')  # x offset
            for x in range(self.__width):
                print('#', end='')
            print()

    def update(self, *args, **kwargs):
        '''
            Updates the arguments in the class
        '''
        if args:
            try:
                props = ["id", "width", "height", "x", "y"]
                for index, arg in enumerate(args):
                    if hasattr(self, props[index]):
                        setattr(self, props[index], arg)
            except IndexError:
                pass
        elif kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        '''
            Returns a dictionary representation of this class
        '''
        return {'x': getattr(self, "x"),
                'y': getattr(self, "y"),
                'id': getattr(self, "id"),
                'height': getattr(self, "height"),
                'width': getattr(self, "width")}

    @staticmethod
    def setter_validation(attribute, value):
        if type(value) is not int:
            raise TypeError(f"{attribute} must be an integer")
        if attribute in ["y", "x"]:
            if value < 0:
                raise ValueError(f"{attribute} must be >= 0")
        elif value <= 0:
            raise ValueError(f"{attribute} must be > 0")

    def __str__(self):
        '''
            Overwritting the str method
        '''
        name = self.__class__.__name__
        return "[{}] ({}) {}/{} - {}/{}".format(name, self.id, self.x, self.y,
                                                self.width, self.height)
