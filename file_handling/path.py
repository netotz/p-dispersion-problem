'''
Module for handling directories and getting paths.
'''

import os

def generate_filename(n: int, p: int, index: int = 0) -> str:
    '''
    Generates a name for an instance's file:

    <n>_<p>_<index>.dat
    '''
    return str(n) + '_' + str(p) + '_' + str(index) + '.dat'

def get_filepath(filename: str) -> str:
    '''
    Returns the path of a file based on it's name.
    '''
    current_dir = os.path.dirname(__file__)
    filepath = os.path.join(current_dir, '..', 'instances', filename)
    return os.path.abspath(filepath)
