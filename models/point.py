'''
Module for the class of Point.
'''

import math

class Point:
    '''
    A Point in a bidimensional plane with coordinates (x, y) and an index to identify it.
    '''

    def __init__(self, index: int, x: int, y: int):
        self.__index = index
        self.__x = x
        self.__y = y

    @property
    def index(self) -> int:
        '''
        Index that works as an identification.
        '''
        return self.__index

    @property
    def x(self) -> int:
        '''
        Coordinate X.
        '''
        return self.__x

    @property
    def y(self) -> int:
        '''
        Coordinate Y.
        '''
        return self.__y

    def distance(self, point: 'Point') -> float:
        '''
        Calculates the Euclidean distance to another Point.
        '''
        dx = abs(self.x - point.x)
        dy = abs(self.y - point.y)
        return math.hypot(dx, dy)

    def __str__(self) -> str:
        '''
        Returns the string representation of a Point:

        <index> <x> <y>
        '''
        return str(self.index) + ' ' + str(self.x) + ' ' + str(self.y)

    def __eq__(self, point: 'Point') -> bool:
        return self.index == point.index and self.x == point.x and self.y == point.y

    def __repr__(self) -> str:
        return f'Point({self.index}, {self.x}, {self.y})'
