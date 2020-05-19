'''
Command line arguments parser.

Module to parse arguments from the command line.

The parsed arguments are then used in other module to solve the specified instance.
'''

import sys
import argparse
from typing import Tuple

from validations import is_valid_n, is_positive_int, is_time

def parse_arguments() -> Tuple[int, int, Tuple[int, int], int, int, int]:
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
        'n',
        type=is_valid_n,
        help='size of the instance, the n points'
    )
    required.add_argument(
        '-H', '--heuristics',
        nargs=2,
        metavar=('constructive', 'localsearch'),
        type=int,
        choices=(0, 1, 2),
        help='''heuristics to use,
        the solution given by the constructive will be sent to the local search.
        
        Constructives: 1 = Greedy construction (GC).
        
        Local search: 1 = First pairwise interchange (IF), 2 = Best pairwase interchange (IM).
        
        If the constructive option is 0, the local search will receive a random solution'''
    )

    # required exclusive arguments
    # only one argument needs to be specified
    instances = required.add_mutually_exclusive_group()
    instances.add_argument(
        '-n', '--number',
        type=is_positive_int,
        help='number of instances to solve, default to 1 if not specified'
    )
    instances.add_argument(
        '-a', '--all',
        action='store_true',
        help='solve the 20 instances of the specified size'
    )

    optional.add_argument(
        '-sr', '--save-results',
        action='store_true',
        help='save experimental results in a CSV file, default to False'
    )
    optional.add_argument(
        '-t', '--time',
        metavar='s',
        type=is_time,
        default=0,
        help='''pause in seconds between plots,
            default to 0 meaning that a click or key press is needed to replot'''
    )
    optional.add_argument(
        '-v', '--verbose',
        type=int,
        default=0,
        choices=(1, 2, 3),
        help='''increase output verbosity:
            1 = output heuristics results (default).
            2 = show plot of the final solution.
            3 = output each step of heuristics and show a plot every time the solution changes.'''
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
        number = 20
    elif arguments.number:
        number = arguments.number
    else:
        number = 1

    return (
        arguments.n,
        number,
        tuple(arguments.heuristics),
        arguments.verbose,
        arguments.save_results,
        arguments.time
    )
