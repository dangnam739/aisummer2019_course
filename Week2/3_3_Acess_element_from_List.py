######Accessing elements from the List######

#Creating a List
List = ["Elements", "from", "List"]

#Using index number
print("Accessing a elements from the List: ")
print(List[0])
print(List[1])
print(List[2])

# Creating Multi-Demensional List
#(By Nesting a list inside a List)
List = [['Python', 'for'], ['Beginer']]

#Accesing a elenment from the Multi-Demensional List
#using index number
print("\nAcessing a elenment from Muiti-Demensional List:")
print(List[0][1])
print(List[0][0])
print(List[1][0])

List = [1, 2, 'Python', 4, 'List', 6, 'Access']
#Using negative indexxing //chi so nguoc
print("\nAccessing element using negative indexing")
print(List[-1])  #the last element of List
print(List[-3]) #the third last elemet of List
