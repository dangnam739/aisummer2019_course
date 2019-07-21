import random

total_flips = 0  #tong so lan tung dong xu

num_heads = 0  #so lan xh mat truoc

num_tails = 0  #so lan xh mat sau

for _ in range(1000):
    #sinh ngau nhien theo phan bo deu trong khoang [0;1]
    n = random.random()

    if n < 0.5:
        num_tails = num_tails + 1
    else:
        num_heads = num_heads + 1

    total_flips = total_flips + 1

print('Total flips : %d' % total_flips)
print('Number of tails : %d' % num_tails)
print('Number of heads : %d' %num_heads)
