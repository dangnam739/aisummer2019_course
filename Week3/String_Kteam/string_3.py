import math
import re
###Dinh dang chuoi bang toan tu %####
#Cu phap: <string> %(value_1, value_2, ...,value_n) --> ko co dau ','

print('My name is %s' % ('ChrisZang'))
print('The valued of pi is: %f' % (math.pi))
print('The sum from %d to %d is %d' %(1,4,10))
print('The value of pi is %.3f' %(math.pi))


###Dinh dang bang chuoi f(f-string)###
#cu phap: f'<gia tri trong chuoi'
# Kteam = 'Kteam <- This'
# result = f'{Kteam} - Free Education'
# print(result)
# name = 'Nam'
# address = 'Ha Noi'
# age = '20'

# print(f'Nam: {name}\nAddress: {address}\nAge: {age}')

###Dinh dang bang phuong thuc format###
print('a:{}, b:{}, c:{}'.format(1, 2, 3))  #Truyen lan luot cac gia tri trong format theo thu thu a, b, c
print('a:{1}, b:{2}, c{0}'.format('one', 'two', 'three'))  #truyen tho thu tu trong {} c->a->b
print('Only one value: {0}'.format(1,3)) #0 : chi so trong format
print('Two same values: {0}, {0}'.format(1, 2))
print('1:{one}, 2:{two}'.format(one=111, two=222))

#dinh dang can le
#Can le trai: {:(c)<n}
#       phai: {:(c)>n}
#       giua: {:(c)^n}
# c: So ki tu ban muon thay the vao cho trong, neu de trong thi c =' ', con n la so ki tu de can le
print('{:^10}'.format('Kteam'))
print('{:^50}'.format('Kteam'))
print('{:^^50}'.format('Kteam'))
print('How{:*^50}Free Education'.format('Kteam')) #can le giua
print('How{:*>50}Free Education'.format('Kteam'))  #can le phai
print('How{:*<50}Free Education'.format('Kteam'))  #can le trai

# phan dinh dang
row_1 = '+ {:-<6} + {:-^15} + {:->10} +'.format('', '', '')
row_2 = '| {:<6} | {:^15} | {:>10} |'.format('ID', 'Ho va ten', 'Noi sinh')
row_3 = '| {:<6} | {:^15} | {:>10} |'.format('123', 'Yui Hatano', 'Japanese')
row_4 = '| {:<6} | {:^15} | {:>10} |'.format('6969', 'Sunny Leone', 'Canada')
row_5 = '+ {:-<6} + {:-^15} + {:->10} +'.format('', '', '')

# phan xuat ket qua
print(row_1)
print(row_2)
print(row_3)
print(row_4)
print(row_5)
