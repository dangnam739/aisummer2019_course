import random
import math

print(random.random())
print(random.random())
print(random.random())

print(random.randint(1, 9))
print(random.randint(100, 100000))

#Nhap va chuyen doi tu goc ve radian

degree = float(input("Input degree: "))
radian = degree * (math.pi / 180)
print("Output radian: ")
print(radian)

#Kiem tra tam giac vuong

a = int(input("Input a = "))
b = int(input("Input b = "))
c = int(input("Input c = "))

answer = not bool((a * a + b * b - c * c) * (b * b + c * c - a * a) * (c * c + a * a - b * b))
print('Tam giac tren co la tam giac vuong khong ?', answer)
