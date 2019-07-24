#Chuoi Tran
print("Hi, \neu mot ngay nao do")#escape sequence(\n, \a, \b, \t, \\...)
print(r"Hi, \neu mot ngay nao do") #chuoi tran: fix cac escape sequence

########Toan tu trong chuoi#########

#cong chuoi
str_1 = 'How Kteam'
str_2 = 'Free Education'
str_3 = str_1 + str_2
print(str_3)

#nhan chuoi:
str_3 = str_1 * 5
print(str_3)

#in  : Kiem tra mot chuoi co nam trong chuoi khac hay khong
str_4 = 'How'
str_3 = str_4 in str_1  #kiem tra str_4 nam trong str_1 hay khong -> yes: True, no: False
print(str_3)

#Cat chuoi

#Cat tu trai qua phai
str_3 = str_1[0:4]
print(str_3)
str_3 = str_1[1: None] #None la vi tri cuoi
print(str_3)
str_3 = str_1[None :] #None la vi tri dau
print(str_3)

#Cat tu phai qua trai [<start> : <stop> : <step>]
str_3 = str_1[4 : None :1]
print(str_3)

#######Ep kieu######

#Chuoi -> so
str1 = int("100")
str2 = float("9.5")
print(str1)
print(str2)

#So -> Chuoi
str1 = str(15)
print(str1)
print(type(str1))

###Thay doi gia tri ki tu trong chuoi###
str1 = "HowKteam.com"
#gia su muo chuyen o -> 0
str1 = str1[None :1] + '0' + str1[2: None]
print(str1)
print(hash(str1))
