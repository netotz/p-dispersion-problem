'''
Implementatios of local search heuristics.
'''

from models import PDPInstance, Solution
from .functions import objective_function, get_closest_points

def first_interchange(instance: PDPInstance, solution: Solution) -> Solution:
    '''
    First Pairwise Interchange heuristic (IF).

    Receives a feasible solution S of a PDP instance and attempts
    to improve the objective function value by interchanging a
    point x in the solution with another point y not in the solution.

    The point x to be excluded from the solution is one of the two
    points x1, x2 in S that are the closest.

    IF performs the interchange with the first point outside S
    that improves the objective function value.
    '''
    change = True
    while change:
        x1, x2 = get_closest_points(solution, instance.distances)

        solset = set(solution)
        # candidate points outside the solution
        candidates = (p for p in instance.points if p not in solset)
        change = False
        for cp in candidates:
            # solution without point x1
            s1 = list(solution)
            s1.remove(x1)
            s1.append(cp)

            # solution without point x2
            s2 = list(solution)
            s2.remove(x2)
            s2.append(cp)

            # objective function's values
            ff = objective_function(solution, instance.distances)
            f1 = objective_function(s1, instance.distances)
            f2 = objective_function(s2, instance.distances)
            # compare them
            if f1 > ff and f1 >= f2:
                solution = list(s1)
                change = True
                break
            elif f2 > ff and f2 >= f1:
                solution = list(s2)
                change = True
                break

    return solution

def best_interchange(instance: PDPInstance, solution: Solution) -> Solution:
    '''
    Best Pairwise Interchange heuristic (IM).

    Receives a feasible solution S of a PDP instance and attempts
    to improve the objective function value by interchanging a
    point x in the solution with another point y not in the solution.

    The point x to be excluded from the solution is one of the two
    points x1, x2 in S that are the closest.

    IM considers all possible interchanges between x1, x2 and points
    outside S, and performs the interchange that improves the objective
    the most. Thus IM can be viewed as a greedy interchange algorithm.
    '''
    change = True
    while change:
        x1, x2 = get_closest_points(solution, instance.distances)

        solset = set(solution)
        # candidate points outside the solution
        candidates = (p for p in instance.points if p not in solset)
        # temporary better solution
        ss = list(solution)
        change = False
        for cp in candidates:
            # solution without point x1
            s1 = list(solution)
            s1.remove(x1)
            s1.append(cp)

            # solution without point x2
            s2 = list(solution)
            s2.remove(x2)
            s2.append(cp)

            # objective function's values
            ff = objective_function(ss, instance.distances)
            f1 = objective_function(s1, instance.distances)
            f2 = objective_function(s2, instance.distances)
            # compare them
            if f1 > ff and f1 >= f2:
                ss = list(s1)
                change = True
            elif f2 > ff and f2 >= f1:
                ss = list(s2)
                change = True
        if change:
            solution = list(ss)

    return solution
