##########Slicing of a List###############
#(Cat mot danh sach)

#Creating a List
List = ['P', 'Y', 'T', 'H', 'O', 'N', 'L', 'I', 'S', 'T']
print("Intial List: ")
print(List)

#print elements of a range using Slice operation
Sliced_List = List[3:8]  #List[3] to List[7]
print("\nSlicing elements in range 3-8: ")
print(Sliced_List)

#print elements from beginning till end
Sliced_List = List[:]
print("\nPrint all elements using slice operation:")
print(Sliced_List)

#print elements in reverse using Slice operation //List dao chieu nguoc lai
Sliced_List = List[::-1]
print("\nPrint List in reverse: ")
print(Sliced_List)
