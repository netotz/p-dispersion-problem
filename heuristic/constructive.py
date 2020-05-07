'''
Module of the implementations of constructive heuristics for the PDP.
'''

from models import PDPInstance, Point, Solution

def greedy_construction(instance: PDPInstance) -> Solution:
    '''
    Starting by choosing the 2 farthest points,
    the algorithm adds the farthest point to the current solution until p is reached.

    Returns a list of the p chosen points.
    '''
    # copy all the instance's points
    candidates = instance.points
    # initialize the solution with the 2 farthest points
    solution = list(instance.get_farthest_points())
    # remove them from the candidates
    candidates.remove(solution[0])
    candidates.remove(solution[1])

    # until solution has p points
    while len(solution) < instance.p:
        # add the point farthest to the current solution
        maximum = max(
            # the distance between a point and a set is
            # the smallest of the distances between the point and the members of the set
            ((cp, min(instance.distances[cp.index][sp.index] for sp in solution))
             for cp in candidates),
            key=lambda x: x[1]
        )
        chosen_point = maximum[0]
        # add the new point
        solution.append(chosen_point)
        # remove it from candidates
        candidates.remove(chosen_point)

    return solution
