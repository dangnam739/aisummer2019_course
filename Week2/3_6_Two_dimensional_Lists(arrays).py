from __future__ import print_function
##Nested List
a = [[1, 2, 3],[4, 5, 6]]
print(a[0])
print(a[1])
b = a[0]
print(b)
print(a[0][2])
a[0][1] = 7
print(a)
print(b)
b[2] = 9
print(a[0])
print(b)
print(a)

print()
a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
print(a)
print("Method 1: ")
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()

print("Method 2: ")
for row in a:
    for elem in row:
        print(elem, end=' ')
    print()

#Creating Nested Lists:
n = 3
m = 4
#method 1
a = [[0] * m] * n  #create list of size n*m, n: row, m:column
a[0][0] = 5
print(a[1][0])
#method 2
for i in range(n):
    a[i] = [0] * m
#method 3
for i in range(n):
    a.append([0] * m)
#method 4
a = [[0] * m for i in range(n)]

#adding elements to Lists
n = int(input())
a = []
for i in range(n):
    row = input().split()
    for i in range(len(row)):
        row[i] = int(row[i])
    a.append(row)
