#!/usr/bin/python3
"""Module 1-rectangle
Defines a Rectangle class.
"""


class Rectangle:
    """Rectangle class defined by width and height."""

    def __init__(self, width: int = 0, height: int = 0) -> None:
        """Initializes a Rectangle instance.

        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.width = width
        self.height = height

    def __str__(self):
        """Returns an informal and nicely printable string representation
        of a Rectangle instance, filled with the '#' character."""
        if self.__height == 0 or self.__width == 0:
            return ''
        rep = ""
        for h in range(self.__height):
            for w in range(self.__width):
                rep += str(self.print_symbol)
            if h < self.__height - 1:
                rep += "\n"
        return rep

    def __repr__(self):
        """Return a string representation of a Rectangle instance
        that is able to recreate a new instance by using eval()
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    @property
    def width(self) -> int:
        """Retrieves the width of a Rectangle instance."""
        return self.__width

    @width.setter
    def width(self, value: int) -> None:
        """Sets the width of a Rectangle instance

        Args:
            value: value of the width, must be a positive integer
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self) -> int:
        """Retrieves the height of a Rectangle instance."""
        return self.__height

    @height.setter
    def height(self, value: int) -> None:
        """Sets the height of a Rectangle instance

        Args:
            value: value of the height, must be a positive integer
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self) -> int:
        """Calculates the area of a Rectangle instance

        Returns:
            Area of the the rectangle, given by height * width
        """
        return self.__width * self.__height

    def perimeter(self) -> int:
        """Calculates the perimeter of a Rectangle instance

        Returns:
            Perimeter of the rectangle, given by 2 * (height + width)
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)
