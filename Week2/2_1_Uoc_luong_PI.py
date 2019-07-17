U = 0
N = 0

for i in range(1000000):
    #Sinh so trong khoang [-1,1]
    x = random.uniform(-1, 1) # = random.random()*2 - 1
    y = random.uniform(-1, 1) # = random.random()*2 - 1

    if (math.sqrt(x ** 2 + y ** 2) <= 1):
        N_t = N_t + 1

    N = N + 1
#tinh pi
pi = 4 * float(N_t) / float(N)
print(pi)
