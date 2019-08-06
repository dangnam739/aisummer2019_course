import random

n = 20  #size of individual(chromosome)
m = 10 #size of population

def generate_random_value():
    return random.randint(0,1)

def create_individual():
    return [generate_random_value() for _ in range(n)]

def print_List(list):
    for elem in list:
        print(elem)

population = [create_individual() for _ in range(m)]
print_List(population)


population_fitness = []

for i in population:
    population_fitness.append(sum(i))

print(population_fitness)



#Sinh ra 20 10 cap so ngau nhien trong [0,9]
random_numbers = [(random.randint(0,9), random.randint(0,9)) for _ in range(10)]
print(random_numbers)

def selection(sorted_old_population, m):
    index1 = random.randint(0, m-1)
    while True:
        index2 = random.randint(0,m-1)
        if index2 != index1 :
            break

    individual_s = sorted_old_population[index1]
    if index2 > index1 :
        individual_s = sorted_old_population[index2]

    return individual_s


