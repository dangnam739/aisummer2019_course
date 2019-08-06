'''
Mo ta du lieu: gom 333 mau, moi mau gom 13 dac trung va mot cot label(gia nha thuc)

Gia su du lieu phan bo theo phuon trinh:
    price = Sigma(ci * fi), i =1->14

trong do, ci la cac tham so can tim va fi bao gom 13 dac trung
theo thu tu xuat hien theo cot du lieu va f14 = 1.0

---> Chieu dai chromosome = 14
---> Kieu du lieu: Floating-point
'''

import random
import matplotlib.pyplot as plt
import numpy as np

n = 4
m = 200
n_generation = 4000
losses = []

#Load data function


def load_data():
    file = open('Boston_Dataset.csv', 'r')

    lines = file.readlines()

    features = []
    prices = []

    for i in range(1, 334):
        temp = lines[i].split(',')
        feature = [float(s.strip()) for s in temp[: len(temp) - 1]]
        feature.append(1.0)
        features.append(feature)
        prices.append(float(temp[-1]))

    file.close()

    return features, prices


#load data
features, prices = load_data()
# for i in range(10):
#     print(features[i])
#     print(prices[i])


def generate_random_value(bound=100):
    return (random.random()) * bound


def compute_loss(individual):
    estimated_prices = []
    for feature in features:
        estimated_price = sum(c * x for x, c in zip(feature, individual))
        estimated_prices.append(estimated_price)

    losses = [abs(y_est - y_gt)
              for y_est, y_gt in zip(estimated_prices, prices)]

    return sum(losses)


def compute_fitness(individual):
    loss = compute_loss(individual)
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

    if gen % 50 == 0:
        losses.append(compute_loss(sorted_population[m - 1]))
        # print('Best loss:', compute_loss(sorted_population[m - 1]))

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
for i in range(n_generation):
    population = create_new_population(population, 2, i)

#figure 1
# print("Show loss: ")
# plt.plot(losses[:333], c='green')
# plt.xlabel('Generations')
# plt.ylabel('Losses')
# plt.show()

#figure2
sorted_population = sorted(population, key=compute_fitness)
print(sorted_population[m - 1])
individual = sorted_population[m - 1]

estimated_prices = []
for feature in features:
    estimated_price = sum(c * x for x, c in zip(feature, individual))
    estimated_prices.append(estimated_price)

losses = losses = [abs(y_est - y_gt)
                   for y_est, y_gt in zip(estimated_prices, prices)]
print(sum(losses))

fig, ax = plt.subplots(figsize=(10, 6))
plt.plot(prices, c='green')
plt.plot(estimated_prices, c='blue')
plt.show()
