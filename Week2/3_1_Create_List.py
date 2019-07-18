############Creating a List#############
List = []
print("Intital blank List: ")
print(List)

#creating a List with the use of a String
List = ['PythonList']
print("\nList with the use of String:  ")
print(List)

#creating a List with the use of multiple value
List = ["Python", "List"]
print("\nList containing multiple values: ")
print(List[0])
print(List[1])

#creting a Multi-Dimensional List
#(By Nesting a list inside List)
List = [['Python', 'List'], ['inside']]
print("\Multi-Demensional List: ")
print(List)

#creating a List with the use of Numbers
#(Having duplicate values)
List = [1, 2, 3, 3, 4, 4, 6, 5]
print("\nList with the use of Numbers: ")
print(List)
for i in List:
    print(List[i])

#creating a List with mixed type of values
#(Having numbers and strngs)
List = [1, 2, 'Python', 4, 5, 'List']
print("\nList with the use of Mixed Values: ")
print(List)
