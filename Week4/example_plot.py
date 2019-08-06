import random
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

n = 2  # size of indivudal (chromosome)
m = 100  # size of population
n_generations = 100  # number of generations
losses = []  #

# Import data
dataframe = pd.read_csv('data.csv')

areas = dataframe.values[:, 0]
prices = dataframe.values[:, 1]


def plot_dataframe(areas, prices):
    fig = plt.figure('Show dataFrame')
    ax = fig.add_subplot(111)
    plt.xlabel('Area of house (x100m^2)')
    plt.ylabel('Price of house')
    plt.plot(areas, prices, 'o')
    plt.show()


def generate_random_value(bound=100):
    return (random.random()) * bound


def compute_loss(individual):
    a = individual[0]
    b = individual[1]

    estimated_prices = [a * x + b for x in areas]
    estimated_prices = [abs(x) for x in estimated_prices]

    losses = [abs(y_est - y_gt)
              for y_est, y_gt in zip(estimated_prices, prices)]

    return sum(losses)


def compute_fitness(individual):
    loss = compute_loss(individual)
    #loss + 1 de tranh trh mau so = 0
    fitness = 1 / (loss + 1)
    return fitness


def creat_individual():
    return [generate_random_value() for _ in range(n)]


def crossover(individual1, individual2, crossover_rate=0.9):

    individual1_new = individual1[:]
    individual2_new = individual2[:]

    for i in range(n):
        if random.random() < crossover_rate:

            individual1_new[i] = individual2[i]
            individual2_new[i] = individual1[i]

    return individual1_new, individual2_new


def mutate(individual, mutation_rate=0.05):

    individual_m = individual[:]

    for i in range(n):
        if random.random() < mutation_rate:

            individual_m[i] = generate_random_value()

    return individual_m


def selection(sorted_old_population):
    index1 = random.randint(0, m - 1)
    while True:
        index2 = random.randint(0, m - 1)
        if index2 != index1:
            break

    individual_s = sorted_old_population[index1]
    if index2 > index1:
        individual_s = sorted_old_population[index2]
    return individual_s


def create_new_population(old_population, elitism=2, gen=1):

    sorted_population = sorted(old_population, key=compute_fitness)

    if gen % 1 == 0:
        losses.append(compute_loss(sorted_population[m - 1]))
        print('Best loss:', compute_loss(sorted_population[m - 1]))

    new_population = []
    while len(new_population) < m - elitism:
        # Selection
        individual_s1 = selection(sorted_population)
        individual_s2 = selection(sorted_population)

        # Crossover
        individual_c1, individual_c2 = crossover(individual_s1, individual_s2)

        # Mutation
        individual_m1 = mutate(individual_c1)
        individual_m2 = mutate(individual_c2)

        new_population.append(individual_m1)
        new_population.append(individual_m2)

    for ind in sorted_population[m - elitism:]:
        new_population.append(ind[:])

    return new_population


population = [creat_individual() for _ in range(m)]

print('Old Population')
for i in population:
    print(i)

for i in range(n_generations):
    population = create_new_population(population, 2, i)

print('New Population')
for i in population:
    print(i)

print('Show loss:')
y = [i for i in range(n_generations)]
plt.plot(y, losses)
plt.show()

print('\nGia tri du doan:')
predict = population[m - 1]
print(predict)
print('\nKet qua du doan cho can nha rong 800 m^2')
y_result = predict[0] * 8 + predict[1]
print(y_result)


def plot_result(areas, prices, predict):
    a = predict[0]
    b = predict[1]
    x = np.linspace(1, 9)
    y = a*x + b
    fig = plt.figure('Show dataFrame')
    ax = fig.add_subplot(111)
    plt.xlabel('Area of house (x100m^2)')
    plt.ylabel('Price of house')
    plt.plot(areas, prices, 'o')
    plt.plot(x, y)
    plt.show()


plot_result(areas, prices, predict)
