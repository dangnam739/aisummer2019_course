from PIL import Image

#doc file anh
image = Image.open('Sydney-Opera-House.jpg')

#in cac thuoc tinh cua anh
print(image.format, image.size, image.mode)
#format : loai file anh
#size   : tra ve mot tuple chua chieu rong va chieu cao cua anh
#mode   : cho biet kieu anh: voi L (anh
#dang grayscale - moi pixel co gia tri tu
#0-255)
# RGB : anh dang mau

#hien thi anh
image.show()

#Chuyen sang anh grayscale
img = image.convert('L')

#resize anh
out = image.resize((128, 128))

#rotate anh 45 do
out = image.rotate(45)

#hien thi anh goc va ket qua
img.show()
out.show()
