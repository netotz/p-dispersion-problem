'''
Tests for the Point class.
'''

import math

from models import Point

def test_distance():
    '''
    Test distance from one point to another.
    '''
    p1 = Point(0, 1, 2)
    p2 = Point(1, 3, 4)
    assert p1.distance(p2) == math.sqrt(abs(3 - 1) ** 2 + abs(4 - 2) ** 2)
