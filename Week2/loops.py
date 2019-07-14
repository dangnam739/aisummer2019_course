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


print("===========Nested Loop===========")  #vong lap long nhau
