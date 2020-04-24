'''
Module to generate an instance for the PDP.
'''

from models import PDPInstance
from file_handling import write_instance
from .cl_argsparse import parse_arguments

def generate_instance():
    '''
    Generates an random instance based on the arguments parsed.

    The generated instance is saved to a .dat file.
    '''
    n, p, dimensions, number = parse_arguments()
    x_max, y_max = dimensions
    for _ in range(number):
        instance = PDPInstance.random(n, p, x_max, y_max)
        write_instance(instance)
