'''
Read an instance from a file and solve it.
'''

from solver import parse_arguments, solve_instance

args = parse_arguments()
solve_instance(*args)
