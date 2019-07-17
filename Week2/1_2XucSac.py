import random

total_flips = 0  #So lan tung
num1, num2, num3, num4, num5, num6 = 0, 0, 0, 0, 0, 0  #So lan xuat hien cua cac mat 1, 2, ,3, 4, 5, 6

for _ in range(10000):
    n = random.randint(1, 6)
    if n == 1:
      num1 = num1 + 1
    elif n == 2:
      num2 = num2 + 1
    elif n == 3:
      num3 = num3 + 1
    elif n == 4:
      num4 = num4 + 1
    elif n == 5:
      num5 = num5 + 1
    else:
      num6 = num6 + 1;

    total_flips = total_flips + 1

print('total_flips = %d' %total_flips)
print('Num of 1 = %d\nNum of 2 = %d\nNum of 3 = %d\nNum of 4 = %d\nNum of 5 = %d\nNum of 6 = %d' %(num1, num2, num3, num4, num5, num6))
