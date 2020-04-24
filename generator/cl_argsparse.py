'''
Command line arguments parser.

Module to parse arguments from the command line.

The parsed arguments are then used in other module to generate an instance.
'''

import sys
import argparse
from typing import Tuple

def parse_arguments() -> Tuple[int, int, Tuple[int, int], int]:
    '''
    An ArgumentParser object receives arguments from the command line
    and returns them in a tuple of 4 elements.

    (n: int, p: int, dimensions: Tuple[int, int], instances: int)

    If no arguments are given the program will end.
    '''
    # parser's description display when --help is used
    description = 'Generates an random instance with the following arguments:'
    # instantiate argument parser
    parser = argparse.ArgumentParser(description=description)

    # remove optional arguments from parser but store it to append it at the end
    #* this 'hack' is used because otherwise the
    #* required exclusive arguments are displayed as optional when they aren't
    optional = parser._action_groups.pop()

    # required arguments
    # both 'n' and 'p' must be specified
    required = parser.add_argument_group('requiered arguments')
    required.add_argument(
        'n',
        type=int,
        help='total number of candidate points'
    )
    required.add_argument(
        'p',
        type=float,
        help='percentage of points to select'
    )

    # required exclusive arguments
    # only one argument needs to be specified
    shape = required.add_mutually_exclusive_group(required=True)
    shape.add_argument(
        '-s', '--square',
        metavar='length',
        type=int,
        help='locate the n points in a squared plane of dimensions length * length at most'
    )
    shape.add_argument(
        '-r', '--rectangle',
        metavar=('length', 'width'),
        nargs=2,
        type=int,
        help='locate the n points in a rectangular plane of dimensions length * width at most'
    )

    # optional arguments
    optional.add_argument(
        '-i', '--instances',
        metavar='n',
        type=int,
        default=1,
        help='number of instances to generate, default to 1'
    )
    optional.add_argument(
        '-v', '--verbose',
        type=int,
        default=0,
        choices=(1, 2),
        help='increase output verbosity'
    )
    # append optional arguments to parser to display at the end
    parser._action_groups.append(optional)

    # if no arguments are given, display help as if -h was used
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    # parse arguments from command line
    arguments = parser.parse_args()

    # if chosen shape is squared
    if arguments.square:
        dimensions = (arguments.square, arguments.square)
    # if chosen shape is rectangular
    else:
        dimensions = tuple(arguments.rectangle)

    p = int(arguments.p * arguments.n)

    # return parsed arguments gathered in a tuple
    return (arguments.n, p, dimensions, arguments.instances)
