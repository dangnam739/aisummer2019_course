import random
#Sinh ra m vector co gia tri ngau nhien va co do dai n
def generate_vectors(n=10, m =8):
    vectors = [[0]*n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if random.random() >= 0.5:
                vectors[i][j] = 1

    return vectors

n = 10
m = 8
vectors = generate_vectors(n, m)
print(vectors)
