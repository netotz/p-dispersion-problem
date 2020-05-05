'''
Module to solve a PDP instance.
'''

from typing import Tuple

from file_handling import list_files, read_instance
from heuristic.constructive import greedy_construction
from heuristic.functions import objective_function

def solve_instance(size: int, number: int, heuristics: Tuple[int, int], verbose: int):
    '''
    Solves one or more PDP instances according to:

    size: Size of the instance.

    number: Number of instances to solve.

    heuristics: Which heuristics to use. The first element is a constructive,
    the second a local search.

    verbose: Option to increase output information.
    '''
    pdp_instances = (read_instance(file) for file in list_files(size, number))
    for instance in pdp_instances:
        print('Solving instance...')
        solution = greedy_construction(instance)

        #* temporary simple output, will be changed
        print(solution)
        f = objective_function(solution, instance.distances)
        print(f'Obj func = {f}')
        print()
