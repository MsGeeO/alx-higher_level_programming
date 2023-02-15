#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
===================================
module with class BaseGeometry
===================================
"""


class Square(Rectangle):
    """Square class that inherits from Rectangle that inherits BaseGeometry"""

    def __init__(self, size):
        """Method for initialized the attrubutes"""
        
        Args:
            size (int): The size of the new square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
