'''
Supplementary functions for the heuristics.
'''

from typing import List

from models import Point, Matrix

def objective_function(solution: List[Point], dist_matrix: Matrix) -> int:
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
