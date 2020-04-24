'''
Module for the class of a PDP's Instance.
'''

from typing import List
from random import randint

from .point import Point

Matrix = List[List[int]]

class PDPInstance:
    '''
    Instance for the PDP containing:

    p: number of points to select from n.

    points: list of n Point objects.

    distances_flag: whether or not to calculate the distances matrix.
    Set this to False when writing the instance.
    '''

    def __init__(self, p: int, points: List[Point], distances_flag: bool = True):
        self.__n = len(points)
        self.__p = p
        self.__points = points
        if distances_flag:
            self.__distances = self.__get_distances()
        else:
            self.__distances = [[0]]

    @classmethod
    def random(cls, n: int, p: int, x_max: int, y_max: int):
        '''
        Constructs a random PDP Instance.
        '''
        points = [Point(i, randint(0, x_max), randint(0, y_max)) for i in range(n)]
        return cls(p, points, False)

    @property
    def n(self) -> int:
        '''
        Total number of candidate points.
        '''
        return self.__n

    @property
    def p(self) -> int:
        '''
        Number of points to select from 'n'.
        '''
        return self.__p

    @property
    def points(self) -> List[Point]:
        '''
        Candidate points.
        '''
        return self.__points

    @property
    def distances(self) -> Matrix:
        '''
        Matrix of Euclidean distances of the candidate points.
        '''
        return self.__distances

    def __get_distances(self) -> Matrix:
        '''
        Gets the distances matrix of the candidate points.
        '''
        return [
            [
                # Euclidean distance from point i to point j
                self.points[i].distance(self.points[j])
                # if it's distance of same city put 0
                if i != j else 0
                # for each column
                for j in range(len(self.points))
            ]
            # for each row
            for i in range(len(self.points))
        ]

    def set_distances(self):
        '''
        Set the distances matrix.
        '''
        self.__distances = self.__get_distances()

    def __str__(self) -> str:
        '''
        Returns a string representing the body (the Points) of the instance's file.
        '''
        return '\n'.join([str(p) for p in self.points])
