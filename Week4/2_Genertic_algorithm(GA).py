import matplotlib.pyplot as plt
import random


n = 20  #size of individual(chromosome)
m = 10 #size of population
n_generattions = 50 #number of generations

#de ve bieu do qua trinh toi uu
fitness = []

def generate_random_value():
    return random.randint(0,1)

def create_individual():
    return [generate_random_value() for _ in range(n)]

def compute_fitness(individual):
    return sum(gen for gen in individual)

def selection(sorted_old_population):
    index1 = random.randint(0, m-1)
    while True:
        index2 = random.randint(0,m-1)
        if index2 != index1 :
            break

    individual_s = sorted_old_population[index1]
    if index2 > index1 :
        individual_s = sorted_old_population[index2]

    return individual_s

def crossover(individual1, individual2, crossover_rate = 0.9):
    individual1_new = individual1[:]
    individual2_new = individual2[:]

    for i in range(n):
        if random.random() <crossover_rate:
            individual1_new[i] = individual2[i]
            individual2_new[i] = individual1[i]

    return individual1_new, individual2_new

def mutate(individual, mutatuon_rate = 0.9):
    individual_m = individual[:]

    for i in range(n):
        if random.random() < mutatuon_rate:
            individual_m[i] = generate_random_value()

    return  individual_m

def create_new_population(old_population, elitism = 2, gen = 1):
    sorted_population = sorted(old_population, key = compute_fitness)#sap xep lai old population

    if gen%1 == 0:
        fitness.append(compute_fitness(sorted_population[m-1]))
        print("BEST: ", compute_fitness(sorted_population[m-1]))

    new_population = []
    while len(new_population) < m - elitism:

        #selection
        individual_s1 = selection(sorted_population)
        individual_s2 = selection(sorted_population) #duplication

        #crossover
        individual_c1, individual_c2 = crossover(individual_s1, individual_s2)

        #mutation
        individual_m1 = mutate(individual_c1)
        individual_m2 = mutate(individual_c2)

        new_population.append(individual_m1)
        new_population.append(individual_m2)

    for ind in sorted_population[m-elitism:]:
        new_population.append(ind[:])

    return new_population

population = [create_individual() for _ in range(m)]

for i in range(n_generattions):
    population = create_new_population(population, 2, i)

y = [i for i in range(n_generattions)]
print(y)
plt.plot(y, fitness)
plt.show()
