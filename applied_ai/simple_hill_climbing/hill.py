"""Simple Hill Climbing Algorithm.
"""

import random
from matplotlib import pyplot


def load_matrix(filename):
    """Load a text file into a 2D array.

    Args:
        filename (string): Filename in current folder.

    Returns:
        list: 2D list
    """
    matrix = []

    with open(filename, 'r', encoding='utf8') as f:
        for line in f:
            line = line.strip()

            matrix.append(list(int(x) for x in line.split(',')))

    return matrix


def path_cost(matrix, solution):
    """Calculate the cost of a solution.

    Args:
        matrix (list): Edge cost matrix
        solution (list): Node list

    Returns:
        int: Cost of traversing the solution nodes.
    """
    cost = 0

    for i in range(0, len(solution)):
        cost += matrix[solution[i]][solution[i - 1]]

    return cost


def find_best_neighbour(matrix, solution):
    """Find the optimal neighbour.

    Args:
        matrix (list): Edge cost matrix
        solution (list): Node list

    Returns:
        list: Closest neighbour with only two elements swapped.
    """
    neighbours = []

    # Generate a collection of neighbouring paths,
    # each with just two adjacent elements swopped.
    for i in range(len(solution) - 1):
        neighbour = solution.copy()

        neighbour[i] = solution[i+1]
        neighbour[i+1] = solution[i]

        neighbours.append(neighbour)

    # Iterate through all the neighbours to find the best one.
    best_neighbour = neighbours[0]

    best_cost = path_cost(matrix, best_neighbour)

    for neighbour in neighbours:
        current_cost = path_cost(matrix, neighbour)

        if current_cost < best_cost:
            best_cost = current_cost
            best_neighbour = neighbour

    return best_neighbour, best_cost


def hill_climbing(matrix):
    """Implement the simple hill climbing algorithm.

    Args:
        matrix (list): Edge cost matrix

    Returns:
        list: Array of all path costs found.
    """
    costs = []

    # Start with list of indices in random order.
    path = list(range(len(matrix)))
    random.shuffle(path)

    num_same_cost = 0

    while num_same_cost < 25:
        cost = path_cost(matrix, path)

        possible_path = find_best_neighbour(matrix, path)[0]

        new_path, new_cost = find_best_neighbour(matrix, possible_path)

        if new_cost < cost:
            cost = new_cost
            path = new_path
        else:
            num_same_cost += 1

        costs.append(cost)

    return costs


matrix = load_matrix('matrix.txt')

pyplot.figure()

for i in range(10):
    path_costs = hill_climbing(matrix)

    total_iterations = len(path_costs)
    final_cost = path_costs[-1]

    print(f"Run {i+1}: path cost = {final_cost}, iterations = {total_iterations}")

    pyplot.plot(range(len(path_costs)), path_costs)

pyplot.show()
