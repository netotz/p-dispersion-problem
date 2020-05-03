'''
Command line arguments parser.

Module to parse arguments from the command line.

The parsed arguments are then used in other module to solve the specified instance.
'''

import sys
import argparse
from typing import Tuple

def parse_arguments() -> Tuple[int, int, Tuple[int, int], int]:
    '''
    An ArgumentParser object receives arguments from the command line
    and solves a PDP instance and returns a tuple of 4 elements:

    (size: int, instances: int, heuristics: Tuple[int, int], verbose: int)

    If no arguments are given the program will end.
    '''

    # parser's description display when --help is used
    description = 'Solves one or more PDP instances specified by the following arguments:'
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
        'size',
        metavar='size',
        type=int,
        default=1,
        choices=(1, 2, 3),
        help='size of the instance: 1 = small, 2 = medium, 3 = large'
    )
    required.add_argument(
        '-H', '--heuristics',
        nargs=2,
        metavar=('constructive', 'localsearch'),
        type=int,
        choices=(0, 1),
        help='''heuristics to use,
        the solution given by the constructive will be sent to the local search.
        
        Constructives: 1 = Greedy construction.
        
        Local search: 1 = First pairwise interchange.
        
        If the constructive option is 0, the local search will receive a random solution'''
    )

    # required exclusive arguments
    # only one argument needs to be specified
    number = required.add_mutually_exclusive_group(required=True)
    number.add_argument(
        '-i', '--instances',
        metavar='n',
        type=int,
        default=1,
        help='number of instances to solve, default to 1'
    )
    number.add_argument(
        '-a', '--all',
        action='store_true',
        help='solve all instances of the specified size'
    )

    # optional arguments
    optional.add_argument(
        '-v', '--verbose',
        type=int,
        default=1,
        choices=(1, 2, 3),
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

    # if all instances will be solved
    if arguments.all:
        instances = 20
    # if chosen shape is rectangular
    else:
        instances = arguments.instances

    return (arguments.size, instances, tuple(arguments.heuristics), arguments.verbose)
