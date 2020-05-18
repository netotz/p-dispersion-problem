'''
Module for handling directories and getting paths.
'''

import os
import random
from typing import List

def generate_filename(n: int, p: int, index: int = 0) -> str:
    '''
    Generates a name for an instance's file:

    <n>_<p>_<index>.dat
    '''
    return str(n) + '_' + str(p) + '_' + f'{index:02d}' + '.dat'

def get_filepath(filename: str, folder: str = 'instances') -> str:
    '''
    Returns the path of a file based on it's name.
    '''
    current_dir = os.path.dirname(__file__)
    filepath = os.path.join(current_dir, '..', folder, filename)
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
        prefix = str(size) + '_'
        suffix = '.dat'

        filtered_files = [
            file for file in files
            if file.startswith(prefix) and file.endswith(suffix)
        ]

        if not filtered_files:
            print(f' error: there are no instances of size {size}')
            return []
        elif len(filtered_files) == number:
            return filtered_files
        elif len(filtered_files) > number:
            return random.sample(filtered_files, number)
        else:
            print(f'  error: there are only {len(filtered_files)} files, not {number}')
