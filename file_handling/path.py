'''
Module for handling directories and getting paths.
'''

import os
import random
from typing import List

from solver import SIZES

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

def list_files(size: int, number: int) -> List[str]:
    '''
    Returns a list of number .dat files in the instances/ subdirectory
    according to the specified size.
    '''
    current_dir = os.path.dirname(__file__)
    subdirectory = os.path.abspath(os.path.join(current_dir, '..', 'instances'))
    try:
        files = os.listdir(subdirectory)
    except FileNotFoundError:
        os.makedirs(subdirectory)
        return list_files(size, number)
    else:
        filtered_files = [
            file for file in files
            if file.startswith(SIZES[size]) and file.endswith('.dat')
        ]
        return random.sample(filtered_files, number)
