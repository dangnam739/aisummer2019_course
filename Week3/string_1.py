#Cac kieu chuoi
#Nhay don: ' '
#Nhay kep: " "
#Ms cach khac: ''' ''', """ """

str = 'How Kteam'
print(str)
print('How Kteam')
print(type(str))

#Su khac bit giua nhay don va nhay kep, nhay kep dung de luu mot chuoi co chua dau nhay don va nhay don dung de luu chuoi co chua dau nhay kep
str_example = "I'm a student"
print(str_example)
str_example = 'In a "secret" relationship'
print(str_example)

#Dau nhay 3: '''. """ dung de luu chuoi nhieu dong
str_line = '''My name is Nam.
I'm a student of Hanoi University of Science and Technology.'''
print(str_line)

#Docstring: Mot dang chu thich nhieu dong, sd nhay 3

"""
Day la chu thich nhieu dong
line 1
line 2
line 3
"""
#In mot so ki tu dac biet
'''
' : \'
" : \"
\ : \\
'''
print('\'\n\"\a')
print('\a')
