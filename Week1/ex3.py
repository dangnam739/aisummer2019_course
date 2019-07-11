#Tao ham trong python

#Cu phap: def <ten_ham> (tham_so):
#             <noi_dung_ham: thut_le_4_khoang_trong>

#function print
def get_groceries():
    print('milk')
    print('flour')
    print('sugar')
    print('butter')

get_groceries()

#function to print my name
def hello(name):
    print('Hello ' + name)

name = 'Kieu Dang Nam'

hello(name)

#function bao gom tham so co the gan gia tri mac dinh. Cu phap (<tham_so> = <gia_tri_mac_dinh>)
def hello_1(name='World'):
    print('Hello ' + name)

hello_1()
name = 'Nam'

hello_1(name)

#function plus with 3
def plus_3(val):
    result = val + 3
    print 'The sum of', val, 'and 3 is:', result

val = 10
plus_3(val)

#function Return
def add_three(val):
    result = val + 3
    return result

res = add_three(10)
print(res)

#function nhieu tham so
def sum_of_3val(val1, val2, val3):
    resutl = val1 + val2 + val3
    print'Sum of ', val1, ',', val2, ',', val3, 'is:', resutl

sum_of_3val(1,2,3)
