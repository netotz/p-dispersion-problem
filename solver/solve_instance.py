'''
Module to solve a PDP instance.
'''

from typing import Tuple

from file_handling import list_files, read_instance

SIZES = {
    0 : '',   # all files
    1: '100', # small
    2: '500', # medium
    3: '1000' # large
}

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
        pass
