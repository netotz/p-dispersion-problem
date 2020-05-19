'''
Module to generate an instance for the PDP.
'''

from typing import Tuple

from models import PDPInstance
from models.plotter import plot_instance
from file_handling import write_instance

def generate_instance(n: int, p: int, dimensions: Tuple[int, int], number: int, verbose: int):
    '''
    Generates an random instance based on the arguments parsed:

    n: total number of candidate points.

    p: points to choose from n.

    dimensions: maximum values for coordinates (x, y).

    number: instances to generate.

    verbose: output verbosity.

    The generated instance is saved to a .dat file.
    '''
    x_max, y_max = dimensions

    if not verbose:
        str_gen = ''
        str_wr = ''
        str_done = ''
    else:
        str_gen = 'Generating instance... '
        str_wr = 'Writing instance to file... '
        str_done = 'done.'

    for _ in range(number):
        print(str_gen, end='', flush=True)
        instance = PDPInstance.random(n, p, x_max, y_max)
        print(str_done)

        print(str_wr, end='', flush=True)
        write_instance(instance)
        print(str_done)

        if verbose == 2:
            plot_instance(instance.points)
