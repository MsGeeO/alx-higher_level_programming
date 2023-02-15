#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
===================================
module with class BaseGeometry
===================================
"""


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry"""

    Args:
        width (int): The width of the new Rectangle
        height (int): The height of the new Rectangle
    """
    super().integer_validator("width", width)
    self.__width = width
    super().integer_validator("height", height)
    self.__height = height
    
    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        string = "[" + str(self._class_._name_) + "]"
        string += str(self._width) + "/" + str(self._height)
        return string
