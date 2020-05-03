'''
Generate an instance from the command line and save it to a file.
'''

from generator import generate_instance, parse_arguments

args = parse_arguments()
generate_instance(*args)
