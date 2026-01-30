"""Steepest Ascent Hill Climbing Algorithm, with a list of 25 coordinates.
"""

import random
from matplotlib import pyplot
import numpy


def load_points(filename):
    """Load a text file into an array.

    Args:
        filename (string): Filename in current folder.

    Returns:
        list: array of points
    """
    points = []

    with open(filename, 'r', encoding='utf8') as f:
        for line in f:
            line = line.strip()

            points.append(tuple(float(x) for x in line.split(',')))

    return points


def distance(points):
    point1 = numpy.array(points[0])
    point2 = numpy.array(points[1])

    return numpy.linalg.norm(point1 - point2)


def path_cost(solution):
    """Calculate the cost of a solution.

    Args:
        matrix (list): Edge cost matrix
        solution (list): Node list

    Returns:
        int: Cost of traversing the solution nodes.
    """
    cost = 0

    for i in range(0, len(solution)):
        cost += distance((solution[i], solution[i - 1]))

    return cost


def find_best_neighbour(solution, solution_cost):
    """Find the optimal neighbour.

    Args:
        solution (list): Node list
        solution_cost (float): Cost of the solution path

    Returns:
        list: Best neighbour with a lower cost
    """
    neighbours = []

    # Generate a collection of neighbouring paths,
    # each with just two adjacent elements swopped.
    for i in range(1, len(solution) - 1):
        for j in range(1, len(solution) - 1):
            if (i == j):
                continue

            neighbour = solution.copy()

            neighbour[i] = solution[j]
            neighbour[j] = solution[i]

            neighbours.append(neighbour)

    # Iterate through all the neighbours to find the best one.
    best_neighbour, best_cost = neighbours[0], path_cost(neighbours[0])

    for neighbour in neighbours:
        cost = path_cost(neighbour)

        if cost < best_cost:
            best_neighbour, best_cost = neighbour, cost

    return best_neighbour, best_cost


def hill_climbing(points):
    """Implement the steepest ascent hill climbing algorithm.

    Args:
        points (list): Array of coordinates

    Returns:
        list: Array of all path costs found.
    """
    costs = []

    # Start with list of points in random order.
    indices = list(range(len(points)))
    random.shuffle(indices)
    path = [points[i] for i in indices]

    num_iterations = 0

    cost = path_cost(path)

    while num_iterations < 100:
        num_iterations += 1

        new_path, new_cost = find_best_neighbour(path, cost)

        if new_cost < cost:
            cost, path = new_cost, new_path.copy()
        costs.append(cost)

    return costs, path


points = load_points('points.txt')

pyplot.figure()

for i in range(10):
    path_costs, final_path = hill_climbing(points)

    total_iterations = len(path_costs)
    final_cost = path_costs[-1]

    print(f"Run {i+1}: path cost = {final_cost}, iterations = {total_iterations}")
    print(final_path)

    pyplot.plot(range(len(path_costs)), path_costs)

pyplot.show()

final_path.append(final_path[0])

pyplot.figure()
pyplot.plot(
    [points[0] for points in final_path],
    [points[1] for points in final_path],
)
pyplot.show()
