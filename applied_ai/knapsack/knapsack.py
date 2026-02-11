import random
from matplotlib import pyplot

def initial_population(pop_size, num_items):
    pop = []

    for _ in range(pop_size):
        individual = []

        for _ in range(num_items):
            individual.append(random.randint(0, 1))

        pop.append(individual)

    return pop


def fitness(individual, knapsack_items, knapsack_max_weight):
    total_weight = 0

    for i in range(len(individual)):
        if individual[i] == 0:
            continue

        total_weight += knapsack_items[i]

    if total_weight > knapsack_max_weight:
        return 0

    return total_weight


def probabilities(fitnesses):
    fitness_t = sum(fitnesses)

    if fitness_t == 0:
        return [1/len(fitnesses)] * len(fitnesses)

    fitness_rel = [fitness / fitness_t for fitness in fitnesses]

    return [sum(fitness_rel[:i+1]) for i in range(len(fitness_rel))]


def roulette_wheel_selection(num_to_select, pop_probs, population):
    result = []

    for _ in range(num_to_select):
        spin = random.random()

        for i in range(len(population)):
            if spin <= pop_probs[i]:
                result.append(population[i])
                break

    return result


def one_point_crossover(parent_a, parent_b):
    children = []

    xover_point = random.randint(1, len(parent_a) - 1)

    child_1 = parent_a[:xover_point] + parent_b[xover_point:]
    child_2 = parent_b[:xover_point] + parent_a[xover_point:]

    children.append(child_1)
    children.append(child_2)

    return children


def mutate_individual(individual):
    i = random.randint(0, len(individual) - 1)
    individual[i] = 1 - individual[i]

    if sum(individual) == 0:
        individual[i] = 1 - individual[i]


def run(stop_at_perc, stop_at_max_weight = False):
    best_fitness = 0
    best_individual = None

    pop = initial_population(POP_SIZE, len(ITEM_WEIGHTS))

    perc_individuals_at_max_weight = 0
    stats = []
    x = 0

    while stop_at_max_weight or perc_individuals_at_max_weight < stop_at_perc:
        x += 1

        fitnesses = []

        for individual in pop:
            fitness_i = fitness(individual, ITEM_WEIGHTS, MAX_WEIGHT)
            fitnesses.append(fitness_i)

            if (fitness_i > best_fitness):
                best_individual = individual
                best_fitness = fitness_i

        if stop_at_max_weight and best_fitness == MAX_WEIGHT:
            break

        perc_individuals_at_max_weight = len([
            f for f in fitnesses if f == MAX_WEIGHT
        ]) / POP_SIZE * 100

        stats.append((x, perc_individuals_at_max_weight))

        if perc_individuals_at_max_weight >= stop_at_perc:
            break

        pop_prob = probabilities(fitnesses)

        new_pop = [best_individual]

        while len(new_pop) < POP_SIZE:
            parents = roulette_wheel_selection(2, pop_prob, pop)

            children = one_point_crossover(parents[0], parents[1])

            if random.random() < MUTATION_RATE:
                mutate_individual(children[0])
                mutate_individual(children[1])

            new_pop.append(children[0])
            new_pop.append(children[1])

        pop = new_pop[:POP_SIZE]

    print("Solution", best_individual, best_fitness)
    print(stats)

    return stats


POP_SIZE = 50
ITEM_WEIGHTS = [3, 9, 5, 6]
MAX_WEIGHT = 18
MUTATION_RATE = 0.2
STOP_AT_PERCENTAGE = 80

pyplot.figure()

pyplot.xlabel('Number of generations')
pyplot.ylabel('Percentage of population at maximum knapsack weight')

for k in range(10):
    stats = run(STOP_AT_PERCENTAGE)

    pyplot.plot(
        [gen for gen, _ in stats],
        [perc for _, perc in stats]
    )

pyplot.show()
