###Van dung GA cho viec tim min cua mot ham so
#
# Ham Sphere f(x) = x1^2 + x2^2 + x3^2 + x4^2 + x5^2 + x6^2
# xi thuoc [-20, 20]
#
# Chu y:
#     1. Cac bien xi thuoc R, nen so diem trong khong gian tim kiem la vo han
#         Gen cua chromosome duoc bieu dien bang kieu floating-point
#     2. Ham f(x) co 6 bien. Do do, do dai cau chromosome = 6 = n
#     3. Phan biet 2 nhom thuat ngu:
#         Nhom 1: fitness va accuracy. Thuong gan lien voi bai toan tim max
#         Nhom 2: loss, error, cost. Thuong gan lien voi bai toan tim min
#         --> Doi voi bai toan hay he thong thi gia tri fitness, accuracy cang lon cang tot.
#                                               gia tri loss, error, cost cang nho cang tot.

import  random
import matplotlib.pyplot as plt

n = 6       #size of individual (chromosome)
m = 50      #size of population
n_generations = 100 #number of generations

losses = []

#Ham sinh so thuc trong khoang -20, 20
def generate_random_value(bound = 20):
    return (random.random()*2 - 1)*bound

def compute_loss(individual):
    return sum(gen*gen for gen in individual)

def compute_fitness(individual):
    loss = compute_loss(individual)
    fitness = 1/(loss + 1)
    return fitness

def create_individual():
    return [generate_random_value() for _ in range(n)]

def crossover(individual1, individual2, crossover_rate = 0.9):
    individual1_new = individual1[:]
    individual2_new = individual2[:]

    for i in range(n):
        if random.random() < crossover_rate:
            individual1_new[i] = individual2[i]
            individual2_new[i] = individual1[i]

    return individual1_new, individual2_new

def mutate(individual, mutation_rate = 0.05):
    individual_m = individual[:]

    for i in range(n):
        if random.random() < mutation_rate:
            individual_m[i] = generate_random_value()

    return individual_m

def selection(sorted_old_population):
    index1 = random.randint(0, m-1)

    while True:
        index2 = random.randint(0,m-1)
        if index2 != index1:
            break

    individual_s = sorted_old_population[index1]

    if index2 > index1:
        individual_s = sorted_old_population[index2]

    return individual_s

def create_new_population(old_population, elitism=2, gen=1):
    sorted_population = sorted(old_population, key=compute_fitness)

    if gen%1 == 0:
        losses.append(compute_loss(sorted_population[m-1]))
        print("BEST LOSS: ", compute_loss(sorted_population[m-1]))

    new_population = []

    while len(new_population) < m- elitism:
        #selection:
        individual_s1 = selection(sorted_population)
        individual_s2 = selection(sorted_population)

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
for i in range(n_generations):
    population = create_new_population(population, 2, i)

y = [i for i in range(n_generations)]
plt.plot(y, losses)
plt.show()


