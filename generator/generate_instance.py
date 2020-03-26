'''
Module to generate an instance for the PDP.
'''

from typing import Tuple

from cl_argsparse import parse_arguments

def generate_instance(n: int, p: int, dimensions: Tuple[int, int]):
    '''
    Generates an random instance based on the parameters:

    n: total number of candidate points. They will be randomly located on a bidimensional plane.

    p: number of points to select from n.

    dimensions: maximum values that the coordinates (x, y) of the n points can have.

    The generated instance is saved to a .dat file.
    '''

if __name__ == '__main__':
    n, p, dimensions = parse_arguments()
    # generate_instance(n, p, dimensions)
