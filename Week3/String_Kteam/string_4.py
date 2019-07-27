###Cac phuong thuc chuoi #String Method#

a = '12'
print(int(a))
print(type(a))

#capitalize: ra ve chuoi co ky tu dau duoc viet hoa,          #            cac chu cai con lai viet thuong
a = 'how kteam - free education'
b = a.capitalize()
print(b)

#upper : Viet hoa tat ca cac ky tu
b = a.upper()
print(b)
#lower : viet thuong tat ca ca ky tu
b = a.lower()
print(b)
#swapcase : Chu viet thuong -> viet hoa, viet hoa->viet thuong
b = a.swapcase()
print(b)
#title : Viet hoa chu cai dau cua cac tu, con lai chu thuong
b = a.title()
print(b)
#center(width,[fillchar]): can giua mot chuoi voi do rong width, can giua bang ki tu fillchar<chuoi co do dai bang 1>
b = a.center(50, '*')
print(b)
#rjust : (width,[fillchar]): can phai mot chuoi voi do rong width, can giua bang ki tu fillchar<chuoi co do dai bang 1>
b = a.rjust(50, '.')
print(b)
#ljust : (width,[fillchar]): can trai mot chuoi voi do rong width, can giua bang ki tu fillchar<chuoi co do dai bang 1>
b = a.ljust(50, '.')
print(b)

##Phuong thuc xu ly
#encode : ma hoa chuoi
b = a.encode(encoding='utf-8', errors='strict')
print(b)
b = a.encode()
print(b)

#join : cong chuoi, nho mot danh sach
b = a.join([' -1-', '-2- ', '-3- '])
print(b)

#replace: thay the mot chuoi bang mot chuoi moi
b = a.replace('o', 'K') #thay the toan bo
print(b)
b = a.replace('o', 'K', 1)  #thay the 1 chuoi dau tien
print(b)

#strip(): xoa het khoan trang o hai dau, bo di cac ki tu char' ', va ms escape sequence
#strip('<ki tu>'): xoa bo <kiu tu> o hai dau chuoi
a = '   how kteam    \n'
print(a)
b = a.strip()
print(b)
a = 'how kteamh'
b = a.strip('h') #co the cat bo chuoi a.strip('ho')
print(b)

#lstrip(): cat ben phai
#rstrip(): cat ben trai
