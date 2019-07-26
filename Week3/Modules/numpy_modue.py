import numpy as np

#tao mot numpy array co 1 chieu
a = np.array([1, 2, 3])

print(type(a))

print(a.shape)  #in ra size cua mang: 1x3

print(a[0], a[1], a[2])

a[1] = 7
print(a)

print('\n---------------------------------\n')

#Tao mot numpy array co 2 chieu
b = np.array([[1, 2, 3],
              [4, 5, 6]])
print(b.shape) #2x3
print(b[0, 0], b[0, 1], b[1, 0])

print('\n---------------------------------\n')

#Tao mot numpy array co 2 chieu
#Kieu unsigned int 8 bit (chua gia tri tu 0 -> 255)
width  = 300
height = 250
image = np.zeros((width, height), np.uint8)
print(image)
