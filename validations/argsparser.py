'''
Validations for inputs from the command-line argument parsers.
'''

from argparse import ArgumentTypeError
from typing import Tuple

from .numerical import is_float, is_int

def is_valid_n(string: str) -> int:
    '''
    If the string parameter represents a valid value for 'n' returns its value,
    otherwise raises ArgumentTypeError exception.
    '''
    if is_int(string):
        number = int(string)
        if number > 2:
            return number
        msg = f'must be greater than 2'
    else:
        msg = f'invalid int value: {repr(string)}'
    raise ArgumentTypeError(msg)

def is_percentage(string: str) -> float:
    '''
    If the string parameter represents a valid decimal percentage returns its value,
    otherwise raises ArgumentTypeError exception.
    '''
    if is_float(string):
        number = float(string)
        if 0 <= number <= 1:
            return number
        msg = f'invalid decimal percentage: {number}'
    else:
        msg = f'invalid float value: {repr(string)}'
    raise ArgumentTypeError(msg)

def is_positive_int(string: str) -> int:
    '''
    If the string parameter represents a positive integer (> 0) returns its value,
    otherwise raises ArgumentTypeError exception.
    '''
    if is_int(string):
        number = int(string)
        if number > 0:
            return number
        msg = f'invalid positive int value (> 0): {number}'
    else:
        msg = f'invalid int value: {repr(string)}'
    raise ArgumentTypeError(msg)

def is_time(string: str) -> float:
    if is_float(string):
        number = float(string)
        if number >= 0:
            return number
        msg = f'invalid positive float value: {number}'
    else:
        msg = f'invalid float value: {repr(string)}'
    raise ArgumentTypeError(msg)

def are_valid_dimensions(n: int, dimensions: Tuple[int, int]) -> bool:
    '''
    x*y must be greater or equal to n.
    '''
    x, y = dimensions
    # if there is enough space in dimensions for all n points
    if n <= x * y:
        return True
    return False

def is_valid_p(p: int) -> bool:
    if p >= 2:
        return True
    return False
