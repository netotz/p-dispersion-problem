'''
Module for writing and reading instances to and from files.
'''

import os

from models import PDPInstance
from .path import generate_filename, get_filepath

def write_instance(instance: PDPInstance):
    '''
    Receives a PDP Instance and writes it to a file.
    '''
    index = 0
    while True:
        filename = generate_filename(instance.n, instance.p, index)
        filepath = get_filepath(filename)
        if os.path.exists(filepath):
            index += 1
        else:
            break

    folder = get_filepath('')
    if not os.path.exists(folder):
        os.makedirs(folder)

    try:
        with open(filepath, 'w') as file:
            file.write(str(instance))
    except (IOError, OSError) as error:
        print('The instance could not be written:\n', error)
