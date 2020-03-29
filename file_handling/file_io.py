'''
Module for writing and reading instances to and from files.
'''

from models import PDPInstance
from .path import generate_filename, get_filepath

def write_instance(instance: PDPInstance):
    '''
    Receives a PDP Instance and writes it to a file.
    '''
    filename = generate_filename(instance.n, instance.p)
    filepath = get_filepath(filename)
    with open(filepath, 'w') as file:
        file.write(str(instance))
