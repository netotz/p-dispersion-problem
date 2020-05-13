'''
Module to solve a PDP instance.
'''

from typing import Tuple
from statistics import mean
import timeit
import random

from file_handling import list_files, read_instance
from heuristic.constructive import greedy_construction
from heuristic.local_search import first_interchange, best_interchange
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
    # constructive heuristics
    ch_funcs = {
        1 : greedy_construction
    }
    # local search heuristics
    lsh_funcs = {
        1 : first_interchange,
        2 : best_interchange
    }

    # loaded instances from files
    pdp_instances = (read_instance(file) for file in list_files(size, number))
    improved_instances = 0
    improvement_data = list()
    for instance in pdp_instances:
        print()
        ch_key = heuristics[0]
        if ch_key:
            start = timeit.default_timer()
            solution = ch_funcs[ch_key](instance)
            ch_time = timeit.default_timer() - start

            ch_of = objective_function(solution, instance.distances)
            print(f'CH OF = {ch_of}')
            print(f'CH Time = {ch_time:g} s')
        # if no constructive was chosen
        else:
            solution = random.sample(instance.points, instance.p)

        lsh_key = heuristics[1]
        start = timeit.default_timer()
        solution = lsh_funcs[lsh_key](instance, solution)
        lsh_time = timeit.default_timer() - start

        lsh_of = objective_function(solution, instance.distances)
        print(f'LSH OF = {lsh_of}')
        print(f'LSH Time = {lsh_time:g} s')

        # if the current experiment uses a CH and a LSH
        if ch_key:
            abs_imp = lsh_of - ch_of
            rel_imp = (abs_imp / ch_of) * 100
            improvement_data.append(rel_imp)
            if lsh_of > ch_of:
                improved_instances += 1
                print(f'Absoulte improvement: {abs_imp}')
                print(f'Relative improvement: {rel_imp:.3g}%')
    if ch_key:
        print(f'Improved instances: {improved_instances}/{number}')
        print(f'Avg relative: {mean(improvement_data):.3g}%')
