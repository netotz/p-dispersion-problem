'''
Module to solve a PDP instance.
'''

from typing import Tuple
from statistics import mean
import timeit
import random

from file_handling import list_files, read_instance, write_results
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
        1: greedy_construction
    }
    ch_names = {
        0: 'random',
        1: 'GC'
    }
    # local search heuristics
    lsh_funcs = {
        1: first_interchange,
        2: best_interchange
    }
    lsh_names = {
        1: 'IF',
        2: 'IM'
    }

    improved_instances = 0
    improvement_data = list()
    # initialize results with titles
    results = [
        ['Instance', 'CH OF', 'CH Time (s)', 'LSH OF', 'LSH Time (s)',
         'Absolute improvement', 'Relative improvement']
    ]
    for filename in list_files(size, number):
        # load instance from file
        instance = read_instance(filename)

        print()
        # get chosen constructive heuristic
        ch_key = heuristics[0]
        if ch_key:
            start = timeit.default_timer()
            solution = ch_funcs[ch_key](instance)
            ch_time = timeit.default_timer() - start

            ch_of = objective_function(solution, instance.distances)
            print(f'CH OF = {ch_of}')
            ch_time = float(f'{ch_time:g}')
            print(f'CH Time = {ch_time} s')
        # if no constructive was chosen
        else:
            solution = random.sample(instance.points, instance.p)
            ch_of = ''
            ch_time = ''

        # get chosen local search heuristic
        lsh_key = heuristics[1]
        start = timeit.default_timer()
        solution = lsh_funcs[lsh_key](instance, solution)
        lsh_time = timeit.default_timer() - start

        lsh_of = objective_function(solution, instance.distances)
        print(f'LSH OF = {lsh_of}')
        lsh_time = float(f'{lsh_time:g}')
        print(f'LSH Time = {lsh_time} s')

        # if the current experiment uses a CH and a LSH
        if ch_key:
            abs_imp = lsh_of - ch_of
            rel_imp = (abs_imp / ch_of) * 100
            improvement_data.append(rel_imp)
            if lsh_of > ch_of:
                improved_instances += 1
                print(f'Absoulte improvement: {abs_imp}')
                rel_imp = f'{rel_imp:.3g}%'
                print(f'Relative improvement: {rel_imp}')
        else:
            abs_imp = ''
            rel_imp = ''

        # row (results' data) of current experiment with instance name
        results.append([filename[:-4], ch_of, ch_time, lsh_of, lsh_time, abs_imp, rel_imp])

    if ch_key:
        print(f'Improved instances: {improved_instances}/{number}')
        avg_rel_imp = f'{mean(improvement_data):.3g}%'
        print(f'Avg relative: {avg_rel_imp}')
        results.append(['Improved instances', '', '', '', '', improved_instances, ''])
        results.append(['Average', '', '', '', '', '', avg_rel_imp])
    csv_name = f'{size}_{ch_names[ch_key]}_vs_{lsh_names[lsh_key]}.csv'
    write_results(csv_name, results)
    # print(results)