# Cau lenh if _ else

# a = 5
# b = 8

# print(a == b)
# print(a != b)
# print(a > b)
# print(a < b)
# print(a >= b)
# print(a <= b)

#cu phap: if <condition>:
#            //Neu true
#            <code>
#         else:
#             <code>

#total bill
total = 2000

if total >= 1000:
   discout = total * 0.1
   print 'Ban duoc giam:', discout
else:
    discout = total * 0.05
    print 'Ban duoc giam:', discout

print 'So tien can thanh toan:', total - discout

# function use if_else
def check_age(age):
    if (age >= 18):
      return True
    else:
        return False

print(check_age(18))
print(check_age(16))
print(check_age(20))
