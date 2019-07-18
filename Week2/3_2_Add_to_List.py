#######Adding List#########
#creating a List
List = []
print("Intial blank List: ")
print(List)

#Addition of Elements in the List
List.append(1)
List.append(2)
List.append(5)
print("\nList after Addition of Three elements: ")
print(List)

#Adding elements to the List using Iterator
for i in range(1, 5): #i chay tu 1->4
    List.append(i)

print("\nList after Addition of elements from 1-4:")
print(List)

#Adding Tuples to the List
List.append((5, 6))
print("\nList after Addition of a List: ")
print(List)

#Addition of List to List
List2 = ['Python', 'List']
List.append(List2)
print("\nList after Addition of a List: ")
print(List)

#Addition of Elements at specific Position
#(Using Insert Method)
List.insert(3, 12)  #insert vao list[3] gia tri 12
List.insert(0, 'Python')
print("\nList after performing Insert Operation: ")
print(List)

#Addition of multiple elements to the List at the end
#Using Extend Method (Co the them nhieu elements cung mot luc)
List.extend([8, "made by", "Chris"])
print("\nList after performing Extend Operation: ")
print(List)
