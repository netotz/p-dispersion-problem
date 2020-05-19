'''
Supplementary functions for the heuristics.
'''

from typing import Tuple

from models import Point, Matrix, Solution

def objective_function(solution: Solution, dist_matrix: Matrix) -> int:
    '''
    The maximin objective function of the PDP:
    to maximize the minimum distance between any two of the points in the solution.
    '''
    return min(
        min(
            dist_matrix[solution[i].index][solution[j].index]
            for j in range(i + 1, len(solution))
        )
        for i in range(len(solution) - 1)
    )

def get_closest_points(solution: Solution, dist_matrix: Matrix) -> Tuple[Point, Point]:
    '''
    Returns the two closest points in the solution.
    '''
    indexes = set(p.index for p in solution)
    # get the closest points in the solutions
    minimums = (
        min(
            enumerate(row), key=lambda r: r[1] if r[0] in indexes and r[1] > 0 else float('inf')
        )
        for row in dist_matrix
    )
    closest = min(
        enumerate(minimums), key=lambda m: m[1][1] if m[0] in indexes else float('inf')
    )
    # points' indexes
    i, j = closest[0], closest[1][0]
    p1 = next(p for p in solution if p.index == i)
    p2 = next(p for p in solution if p.index == j)

    return (p1, p2)
