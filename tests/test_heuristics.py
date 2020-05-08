'''
Tests of the heuristic algorithms and functions.
'''

from heuristic.functions import objective_function
from models import PDPInstance, Point

def test_objective_function():
    # generate dummy points
    points = [
        Point(0, 1, 1),
        Point(1, 1, 2),
        Point(2, 1, 4)
    ]
    # dummy instance
    instance = PDPInstance(1, points)
    assert objective_function(points, instance.distances) == 1
