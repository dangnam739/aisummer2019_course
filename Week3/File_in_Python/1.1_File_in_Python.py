#1. Doc file
#Cu phap:
#          var_file = open( < file_name > , < mode > )
#          ...
#          var_file.close()

filepath = 'hello.txt'
filehandle = open(filepath, 'r')

data = filehandle.read()
print(type(data))
print('----------------------')
print(data)

filehandle.close()

# 2. Ghi file
file_path = 'my_file.txt'
file_handle = open(file_path, 'w')

text1 = 'writing line 1\n'
text2 = 'writing line 2\n'
text3 = 'writing line 3\n'

file_handle.write(text1)
file_handle.write(text2)
file_handle.write(text3)

file_handle.close()

#2.1 Ghi tiep vao file da ton tai
file_path = 'my_file.txt'
file_handle = open(file_path, 'a')

text4 = 'writing line 4\n'

file_handle.write(text4)

file_handle.close()
