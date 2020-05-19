'''
Implementations of local search heuristics.
'''
import matplotlib.pyplot as plt

from models import PDPInstance, Solution
from models.plotter import plot_instance_solution
from .functions import objective_function, get_closest_points

def first_interchange(instance: PDPInstance, solution: Solution, verbose: bool = False) -> Solution:
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
    if verbose:
        print('First Pairwise Interchange (IF)')
        print('  Received solution:')
        print(f'  S = {solution}')
        plot_instance_solution(instance.points, solution)
        # plt.show()

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

            if verbose:
                print('\n  Current solution:')
                print(f'  S = {solution}')
                print('  The 2 closest points in S:')
                print(f'  x1 = {repr(x1)}')
                print(f'  x2 = {repr(x2)}')
                print('    Current point outside S:')
                print(f'    xk = {repr(cp)}')
                print('    Remove x1 and add xk:')
                print(f"    S' = {s1}")
                print('    Remove x2 and add xk:')
                print(f"    S'' = {s2}")
                print('    Compare the objective function evaluations:')
                print(f'    f(S) = {ff}')
                print(f"    f(S') = {f1}")
                print(f"    f(S'') = {f2}")

            # compare them
            if f1 > ff and f1 >= f2:
                solution = list(s1)
                change = True
                str_sx = "S'"
                break
            elif f2 > ff and f2 >= f1:
                solution = list(s2)
                change = True
                str_sx = "S''"
                break

        if verbose:
            if change:
                print(f'\n  {str_sx} is better than current S:')
                print(f'  S = {str_sx}')
                plot_instance_solution(instance.points, solution)
            else:
                print('\n  Solution could not improve.')

    return solution

def best_interchange(instance: PDPInstance, solution: Solution, verbose: bool = False) -> Solution:
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
    if verbose:
        print('Best Pairwise Interchange (IM)')
        print('  Received solution:')
        print(f'  S = {solution}')
        plot_instance_solution(instance.points, solution)

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

            if verbose:
                print('\n  Current solution:')
                print(f'  S = {solution}')
                print('  The 2 closest points in S:')
                print(f'  x1 = {repr(x1)}')
                print(f'  x2 = {repr(x2)}')
                print('  Temporary solution:')
                print(f'  SS = {ss}')
                print('    Current point outside S:')
                print(f'    xk = {repr(cp)}')
                print('    Remove x1 and add xk:')
                print(f"    S' = {s1}")
                print('    Remove x2 and add xk:')
                print(f"    S'' = {s2}")
                print('    Compare the objective function evaluations:')
                print(f'    f(SS) = {ff}')
                print(f"    f(S') = {f1}")
                print(f"    f(S'') = {f2}")
            str_sx = ''
            # compare them
            if f1 > ff and f1 >= f2:
                ss = list(s1)
                change = True
                str_sx = "S'"
            elif f2 > ff and f2 >= f1:
                ss = list(s2)
                change = True
                str_sx = "S''"

            if verbose and str_sx:
                print(f'\n    {str_sx} is better than current SS:')
                print(f'    SS = {str_sx}')
                plot_instance_solution(instance.points, ss)

        if change:
            solution = list(ss)
            if verbose:
                print('\n  SS is best neighbor of S:')
                print('  S = SS')
                plot_instance_solution(instance.points, solution)
        else:
            if verbose:
                print('\n  Solution could not improve.')

    return solution
