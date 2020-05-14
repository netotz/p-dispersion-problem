'''
Module for writing and reading instances to and from files.
'''

import os
import csv
from typing import List

from models import PDPInstance, Point
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

def read_instance(filename: str) -> PDPInstance:
    '''
    Reads a file that contains a PDP instance and returns its object.
    '''
    filepath = get_filepath(filename)
    try:
        # if file is empty
        if os.stat(filepath).st_size == 0:
            print('   File %s is empty.' % filename)
            return None

        with open(filepath, 'r') as file:
            # read every line of the file and parse it to constructor's arguments of Point class
            points = [Point(*map(int, line.split())) for line in file]

        # get p from filename
        p = int(filename.split('_')[1])
        # return an object of PDPInstance
        return PDPInstance(p, points)
    except FileNotFoundError as error:
        print('  ', error)
        return None
    except ValueError:
        print('   File %s has invalid format.' % filename)
        return None

def write_results(filename: str, data: List[List[str]]):
    '''
    Writes a CSV file containing the results of an experiment.
    '''
    folder = get_filepath('', 'results')
    if not os.path.exists(folder):
        os.makedirs(folder)

    filepath = get_filepath(filename, 'results')
    try:
        with open(filepath, 'w', newline='') as file:
            writer = csv.writer(file)
            for row in data:
                writer.writerow(row)
    except (IOError, OSError) as error:
        print('The results could not be written:\n', error)
