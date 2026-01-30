"""Steepest Ascent Hill Climbing Algorithm, with a list of 25 coordinates.
"""

import random
import math
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


def find_neighbours(solution):
    """Find all the neighbours.

    Args:
        solution (list): Node list

    Returns:
        list: Neighbours
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

    return neighbours


def find_random_neighbour(solution):
    """Find any random neighbour.

    Args:
        solution (list): Node list

    Returns:
        list: Neighbour with any two elements swapped.
    """
    i = random.randint(0, len(solution)-1)
    j = random.randint(0, len(solution)-1)

    neighbour = solution.copy()

    neighbour[i] = solution[j]
    neighbour[j] = solution[i]

    return neighbour


def simulated_annealing(path):
    """Implement the simulated annealing algorithm.

    Args:
        path (list): Current solution

    Returns:
        tuple: costs, new path, number of iterations
    """
    total_iterations = 0

    TEMP_MAX = 20
    TEMP_MIN = 0.0005
    ALPHA = 0.9995

    temp = TEMP_MAX
    costs = []

    cost = path_cost(path)

    while temp >= TEMP_MIN:
        costs.append(cost)
        total_iterations += 1

#        for neighbour in find_neighbours(path):
        for neighbour in [find_random_neighbour(path)]:
            new_cost = path_cost(neighbour)

            if new_cost < cost:
                # Always accept a better route.
                probability = 1
            else:
                probability = math.exp((cost - new_cost) / temp)

            if probability >= random.random():
                cost, path = new_cost, neighbour.copy()
                break

        temp = temp * ALPHA

    return costs, path, total_iterations


def plot_route(final_path):
    final_path.append(final_path[0])

    pyplot.figure()
    pyplot.plot(
        [points[0] for points in final_path],
        [points[1] for points in final_path],
    )
    pyplot.show()


points = load_points('points.txt')

results = []

for i in range(10):
    # Start with list of points in random order.
    indices = list(range(len(points)))
    random.shuffle(indices)
    path = [points[i] for i in indices]

    path_costs, final_path, total_iterations = simulated_annealing(path)

    final_cost = path_costs[-1]

    print(f"Run {i+1}: path cost = {final_cost}, iterations = {total_iterations}")
    print(final_path)
    plot_route(final_path)

    results.append((path_costs, final_path))

shortest_cost = results[0][0]
shortest_path = results[0][1]

pyplot.figure()

for result in results:
    path_costs, path = result

    if (path_costs[-1] < shortest_cost[-1]):
        shortest_path = path

    pyplot.plot(range(len(path_costs)), path_costs)

pyplot.show()

plot_route(shortest_path)
