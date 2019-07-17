from __future__ import print_function
import random

print("==============While Loop============")
#                   While Loop
# syntax:
#         while < expression > :
#             <code>

#print Hello World 3 times
count = 0
while count < 3:
    count = count + 1
    print('Hello World !')

#while_True_break
while True:
    num = random.randint(1, 20)
    print('So sinh ra co gia tri la %d' % num)

    if num == 18:
        break
print('Da thoat khoi vong lap while')


print("==============For Loop============")
#                   For Loop
# syntax:
#         for <iterator_var> in <sequence>:
#            <code>

#Iterating over a list //Lap lai mot danh sach
print("List Iteration : ")
l = ["geeks", "for", "geeks"]
for i in l:
    print(i)

#Iterating over a tuple (immutable) //tuple bat bien
print("\nTuple Iteration")
t = ("geeks", "for", "geeks")
for i in t:
  print(i)

# Iterating over a string
print("\nString Iteration")
s = "Hello"
for i in s:
    print(i)

#Iterating over dictionary
print("Dictionary teration")
d = dict()
d['xyz'] = 123
d['abc'] = 345

for i in d:
    print("%s %d" %(i, d[i]))


print("===========Nested Loop===========")  #v            ong lap long nhau

# for iterator_var in sequence:
#     for iterator_var in sequence:
#         statements(s)
#         statements(s)

# while expression:
#     while expression:
#         statement(s)
#         statement(s)

# example1:
for i in range(1, 5):
    for j in range(i):
        print(i, end=' ')
    print()

for i in range(2, 10):
    print(i)
    print(range(i))

print("======Loop Control Statements========")

# Continue Statement ->It returns the control to the beginning of the loop
#print all letter except 'a' and 't'
for letter in 'Python Tutorial':
    if letter == 'a' or letter == 't':
        continue
    print ('Current Letter :', letter)
    var = 10

print ("===================")
# Break Statement -> It brings control out of the loop

for letter in 'Python Tutorial':
    if letter == 'u' or letter == 'l':
        break

print('Current Letter :', letter)

# Pass Statement  //dung de viet cac vong lap trong
#We use pass statement to write empty loops.
#Pass is also used for empty control statement, function and classes.

for letter in 'Python Tutorial':
  pass
print("Last Letter :", letter)
