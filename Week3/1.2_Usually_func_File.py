##Mot so ham thuon dung voi file

#1. Ham os.path.exists
#Chuc nang: Kiem tra file co ton tai hay ko.
from __future__ import print_function
import os

file_path_1 = 'my_file.txt'
check_1 = os.path.exists(file_path_1)
print('File %s is exists, isn\'t ?' % (file_path_1), check_1)

file_path_2 = 'non_existence_file.txt'
check_2 = os.path.exists(file_path_2)
print('File %s is exists, isn\'t ?' % (file_path_2), check_2)

#2. Ham splip : Tach chuoi
line = '001,john,12/06/1999'
infor = line.split(',')  #Tach nhau boi dau ','
for i in infor:
    print(i, end=' ')
print()

#3. Ham join : Ghi du lieu co format
#(moi thuoc tinh cach nhau mot ki tu duoc quy dinh)
infor = ['001', 'john', '12/06/1999']
st = (' | ').join(infor)
print(st)
001,john,12/06/1999
