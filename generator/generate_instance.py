'''
Module to generate an instance for the PDP.
'''

from typing import Tuple

from models import PDPInstance
from file_handling import write_instance

def generate_instance(n: int, p: int, dimensions: Tuple[int, int], number: int):
    '''
    Generates an random instance based on the arguments parsed:

    n: total number of candidate points.

    p: points to choose from n.

    dimensions: maximum values for coordinates (x, y).

    number: instances to generate.

    The generated instance is saved to a .dat file.
    '''
    x_max, y_max = dimensions
    for _ in range(number):
        instance = PDPInstance.random(n, p, x_max, y_max)
        write_instance(instance)
