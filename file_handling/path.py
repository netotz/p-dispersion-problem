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
