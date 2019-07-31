#a = id('Kteam') #tra ve mot so nguyen int hoac long int, la hang so tuy theo
                #gia tri truyen vao va ko thay doi suot chuong trinh
                #tra ve gia tri cua dia chi tren bo nho
#print(a)
b = 'Kteam'
a = id(b)
print(a)
print(id('Kteam'))

#Cac toan tu di kem

n = 69
print(n)
print(n.__neg__())
print(n+1)
print(n.__add__(1))
print(n-1)
print(n.__sub__(1))
print(n*2)
print(n.__mul__(2))
print(1+n)
print(n.__radd__(1))

#Hashable Object
#hai toan tu =+  += ko khac nhau
s1 = 'HowKteam'
s2 = 'FreeEducation'
print(id(s1))
print(id(s2))
s1 = s1 + 'Python'
s2 += 'Python'
print(id(s1))
print(id(s2))
print('-----------------------------')

#Unhashable Object
s1 = [1,2]
s2 = [3,4]
print(id(s1))
print(id(s2))
s1 = s1 + [0]
s2 += [0]
print(id(s1))
print(id(s2))