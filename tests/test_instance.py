'''
Tests for PDP Instance class.
'''

from models import PDPInstance, Point

# generate dummy points
points = [
    Point(0, 1, 1),
    Point(1, 1, 2),
    Point(2, 1, 4)
]
# dummy instance
instance = PDPInstance(1, points)

def test_matrix():
    '''
    Test distances matrix generation.
    '''
    matrix = [
        [0, 1, 3],
        [1, 0, 2],
        [3, 2, 0]
    ]
    assert instance.distances == matrix

def test_farthest():
    '''
    Test getter of the two farthest points.
    '''
    p1, p2 = instance.get_farthest_points()
    assert str(p1) + ' ' + str(p2) == '0 1 1 2 1 4'
