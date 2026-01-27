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


def find_random_neighbour(matrix, solution):
    """Find any random neighbour.

    Args:
        matrix (list): Edge cost matrix
        solution (list): Node list

    Returns:
        list: Neighbour with two adjacent elements swapped.
    """
    i = random.randint(1, len(matrix)-2)

    neighbour = solution.copy()

    neighbour[i] = solution[i+1]
    neighbour[i+1] = solution[i]

    return neighbour, path_cost(matrix, neighbour)


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

    cost = path_cost(matrix, path)

    while num_same_cost < 25:
        new_path, new_cost = find_random_neighbour(matrix, path)

        if new_cost < cost:
            cost, path = new_cost, new_path
            num_same_cost = 0
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
