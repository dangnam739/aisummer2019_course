#duoc gioi han boi cap ngoac ()
#cac phan tu cua tuple duoc ngan cach boi dau ,
#tuple co kha nang chu moi gia tri
#toc do truy xuat cua tuple nhanh hon list
#dung luong chiem trong bo nho nho hon list
#bao ve du lieu cua ban se khong thay doi
#co the dung lam key cua dictionary


tup = (1,1,2,5,6,'Kteam', 7,7, (2,5,6))
tup1 = (1) #Khong duoc tinh la mot tuple, la mot int
tup2 = (1,)
print(tup1, tup2)
print('------------------------------')
tup = (i for i in range(10)) #generator object from 0 ->9
a = tuple(tup)
print(tup)
print(a)

#Cac toan tu cua tuple giong voi chuoi
tup1 = (1,2,3)
a = tup1 + (2,4,6)
print(a)
#nhan tuple voi mot so
a = tup1*3
print(a)
#in : kiem tra mot phan tu co trong tuple hay ko
a = 3 in tup1
print(a)

#truy xuat toi mot phan tu
a = tup1[0]
b = tup1[2]
c = tup1[-1]
print(a, b, c)
#do dai tuple
a = len(tup1)
print(a)
a = tup1[:-1]
print(a)

tup = [1,5,9,4]
tup[0] = 'Kteam'
tup = (1,5,9,4)

#ma tran
tup = ((1,2,3,4), (4,5,6,7),(7,8,9,10))

#Hash object : kieu du lieu ko the thay doi du lieu ben trong
#Tuple ko cho phep ban sua chua noi dung ben trong nos, khac voi list

#Cac phuong thuc cua Tuple

#count : Tim so lan suat hien cua 1 phan tu trong tuple
tup = (1,2,3,4,4,5,6,4,7)
a = tup.count(4)
print(a)
#index : tra ve vi tri xuat hien dau tien cua phan tu
a = tup.index(6)
print(a)