'''
Module for the class of a PDP's Instance.
'''

from typing import List

from point import Point

Matrix = List[List[int, ...], ...]

class PDPInstance:
    '''
    Instance for the PDP containing:

    n: number of total candidate points.

    p: number of points to select from n.

    points: list of Point objects.

    distances: matrix of points' Euclidean distances.
    '''

    def __init__(self, n: int, p: int, points: List[Point]):
        self.__n = n
        self.__p = p
        self.__points = points
        self.__distances = self.get_distances()

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

    def get_distances(self) -> Matrix:
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
