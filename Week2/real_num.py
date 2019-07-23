from decimal import *  #Lay toan bo noi dung cua thu vien decimal
getcontext().prec = 30  #Lay toi da 30 chu so thap phan


print(Decimal(10) / Decimal(3))
a = Decimal(100) / Decimal(17)
print(a)
print(type(a))
