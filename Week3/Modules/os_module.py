import os

#os.getcwd() : tra ve thu muc hien tai
print(os.getcwd())

#os.path.join() : noi string
print(os.path.join('/images/', 'img1.png'))

#split() : tach path va filename
pathname = '/Users/AIVIETNAM/images/logo.png'
(dir_name, file_name) = os.path.split(pathname)
print(dir_name)
print(file_name)
