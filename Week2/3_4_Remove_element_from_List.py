###########Removing elements from the List########

#creating a List
List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print("Intial List:")
print(List)

#Using remove(x) x la mot gia tri co trong List
List.remove(5)
List.remove(6)
print("\nList after removal of two elements:")
print(List)

#Using Iterator method
for i in range(1, 5):
    List.remove(i)
print("\nList after removing a range of elements: ")
print(List)

#Using pop() to removing element at a specific locaiton
List.pop(2) #pop List[2]
List.pop(0) #pop List[0]
print("\nList after popin a specific element: ")
print(List)
