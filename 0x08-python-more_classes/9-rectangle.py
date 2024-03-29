#!/usr/bin/python3
"""Module 1-rectangle
Defines a Rectangle class.
"""


class Rectangle:
    """Rectangle class defined by width and height."""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width: int = 0, height: int = 0) -> None:
        """Initializes a Rectangle instance.

        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self) -> str:
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

    def __repr__(self) -> str:
        """Return a string representation of a Rectangle instance
        that is able to recreate a new instance by using eval()
        """
        return (f"{self.__class__.__name__}({self.__width}, {self.__height})")

    def __del__(self) -> None:
        """Deletes a Rectangle instance."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

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

    @staticmethod
    def bigger_or_equal(rect_1: 'Rectangle',
                        rect_2: 'Rectangle') -> 'Rectangle':
        for x in (rect_1, rect_2):
            if not isinstance(x, Rectangle):
                rect = 'rect_1' if x == rect_1 else 'rect_2'
                err_msg = f"{rect} must be an instance of Rectangle"
                raise TypeError(err_msg)
        if rect_1.area() == rect_2.area() or rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size: int = 0) -> 'Rectangle':
        """Creates a new Rectangle instance with width == height == size

        Args:
            size: size to set the new rectangle to

        Returns:
            The new Rectangle instance
        """
        return cls(size, size)
