'''
Module to illustrate the points of an instance and the solution in a plane.
'''
from typing import List

import matplotlib.pyplot as plt

from .pdp_instance import Solution
from .point import Point

def plot_instance(points: List[Point]):
    '''
    Plots all the points of an instance.
    '''
    x_coords = [p.x for p in points]
    y_coords = [p.y for p in points]

    plt.style.use('dark_background')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Generated points')
    # plot all points
    plt.scatter(
        x_coords, y_coords,
        facecolor='xkcd:cerulean', edgecolor='black',
        linewidth=0.4
    )
    plt.show()

def plot_instance_solution(points: List[Point], solution: Solution):
    '''
    Plots the points of an instance and the points of its solution.
    '''
    solset = set(solution)
    sol_x, sol_y, can_x, can_y = [], [], [], []
    for p in points:
        # if point is in the solution
        if p in solution:
            sol_x.append(p.x)
            sol_y.append(p.y)
        # if point is outside the solution
        else:
            can_x.append(p.x)
            can_y.append(p.y)
    plt.style.use('dark_background')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Solution points in red')
    # plot points outside the solution
    plt.scatter(
        can_x, can_y,
        facecolor='xkcd:cerulean', edgecolor='black',
        linewidth=0.25, alpha=0.3
    )
    # plot points in the solution
    plt.scatter(
        sol_x, sol_y,
        facecolor='red', edgecolor='black',
        linewidth=1
        )
    plt.show()
