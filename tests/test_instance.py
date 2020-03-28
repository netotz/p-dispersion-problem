'''
Tests for PDP Instance class.
'''

from models import PDPInstance, Point

def test_matrix():
    '''
    Test distances matrix generation.
    '''
    # generate dummy points
    points = [
        Point(0, 1, 1),
        Point(1, 1, 2),
        Point(2, 1, 3)
    ]
    instance = PDPInstance(3, 1, points)
    matrix = [
        [0, 1, 2],
        [1, 0, 1],
        [2, 1, 0]
    ]
    assert instance.distances == matrix
