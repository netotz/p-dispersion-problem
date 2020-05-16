'''
Module of the implementations of constructive heuristics for the PDP.
'''

from models import PDPInstance, Solution
from models.plotter import plot_instance_solution

def greedy_construction(instance: PDPInstance, verbose: bool = False) -> Solution:
    '''
    Starting by choosing the 2 farthest points,
    the algorithm adds the farthest point to the current solution until p is reached.

    Returns a list of the p chosen points.
    '''
    # copy all the instance's points
    candidates = list(instance.points)
    # initialize the solution with the 2 farthest points
    solution = list(instance.get_farthest_points())
    if verbose:
        print('Greedy Construction (GC)')
        print('  Solution starts with the 2 farthest points:')
        print(f'  S = {solution}')
        plot_instance_solution(instance.points, solution)

    # remove them from the candidates
    candidates.remove(solution[0])
    candidates.remove(solution[1])

    # until solution has p points
    while len(solution) < instance.p:
        len_solution = len(solution)
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

        if verbose:
            print(f'    p = {len_solution}\n')
            print('    Add farthest point to current solution:')
            print(f'    x = {repr(chosen_point)}')
            print(f'    S = {solution}')
            plot_instance_solution(instance.points, solution)

    return solution
