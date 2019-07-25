#T##Phuong thuc tach chuoi

a = 'how kteam free education'
#splip ('<ki tu'): tra ve mot kieu du list bang cach chia chuoi boi mot kieu ki tu, mac dinh = -1, ko gioi han lan tach
#split('<ki tu>', <max_list>): tach voi du so lan cach la max_list
b = a.split(' ', )
print(a)
print(b)
b = a.split(' ', 2) #cat 2 lan --> 3 phan tu
print(b)

#rsplit : Cat tu ben phai qua
#split : cat tu ben trai qua
b = a.rsplit(' ', 2)
print(b)

#partition : tra ve mot tupple voi 3 phan tu, phan tu dau tien trc khi thay ki tu va phan tu sau
b = a.partition('k')
print(b)
b = a.partition('kteam')
print(b)
b = a.partition('y')
print(b)
#rpartition : cat tu phai qua
b = a.rpartition('k')
print(b)
b = a.rpartition('y')
print(b)

### Phuong thuc tien ich

#count : tra ve so luong chuoi trong chuoi
b = a.count('e')
print(b)
b = a.count('e', 1, 10)  #so luong ki tu trong pham vi tu vi tri 1 - 5
print(b)

#startstwith :tra ve True neu chuoi bat dau bang chuoi do, nguoc lai thi False
b = a.startswith('how')
print(b)
b = a.startswith('k', 4)  #ki tu bat dau tu vi tri thu 4
print(b)

#endswith : tra ve True neu ke thuc bang chuoi
b = a.endswith('n')
print(b)

#find: tra ve vi tri dau tien khi tim thay chuoi trong chuoi
b = a.find('kteam')
print(b)

#rfind : tim tu ben phai qua, tra ve vi tri dau tien tim thay
b = a.rfind('f')
print(b)

#index : tuong tu nhu find nhung se loi neu ko tim thay
b = a.index('kteam')
print(b)
b = a.rindex('f')
print(b)


##Phuong thuc xac cac thuc

#islower : kiem tra la chuoi viet thuong hay ko
#isupper : kiem tra chuoi viet hoa toan bo hay ko
#isdigit: ktra co phai so hay ko
#istitle: kiem tra co phai dinh dang title hay ko
#isspace : kiem tra xem co phai tat ca deu la khoang trang hay ko
