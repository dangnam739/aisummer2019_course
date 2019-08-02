##De bai: Cho list data = [1,2,3,4,5,6,7,8,9].
#Cac gia tri trong list the hien diem so cua moi phan tu.
#Phan tu dau co diem so nho nhat la 1 va phan tu cuoi co diem so lon nhat la 9
#Yeu cau : chon ra ngau nhien 1000 phan tu tu list data, va phan tu co diem so lon hon nen duoc chon nhieu hon.

from collections import Counter
import random

#ham tinh xac suat xuat hien cua tung phan tu

def Remove_Duplicate(list):
    result = []

    for elem in list:
        if elem not in result:
            result.append(elem)

    return result

def probability_element(dataList, key):
    list_element = Remove_Duplicate(dataList)
    c = Counter(dataList)

    if key in list_element:
        return float(c[key])/float(len(dataList))
    else:
        return

list = [1, 2, 3, 4, 1, 1, 2, 3, 5, 6, 7, 9, 7, 6, 2, 3, 4, 5, 1, 6, 7, 9]
result = Remove_Duplicate(list)

for i in result:
    print("The probability of element %d is %f" % (i, probability_element(list, i)))

print('--------------------------------------')

score = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#idea: Tinh mien cho tung phan tu
#vd 1: 1/N, 2: 2/N,...9:9/N (N la tong cac gia tri cua diem so)
#sau do voi moi so nguyen r nam trong doan [0,1] xac dinh r nam trong mien nao thi phan tu do duoc chon.
def domain_element(score):
    score.sort()
    sum_elem = sum(score)

    domain_val = []
    domain_val.append(0)

    for elem in score:
      domain = float(elem)/float(sum_elem)
      domain_val.append(domain)

    return domain_val

def index_domain(domainVal, key):
    for i in range(len(domainVal)-1):
        if ((key < domainVal[i + 1]) and (key >= domainVal[i])):
            break;

    return i;

def rand_score(score, N):
    rand_result = []
    domain_val = domain_element(score)

    for i in range(N):
        rand_r = random.random();
        index = index_domain(domain_val, rand_r)
        rand_result.append(score[index])

    return rand_result

N = 100000
result = rand_score(score, N)
c = Counter(result)
for elem in score:
    print("%d : %d: %f" %(elem,c[elem], probability_element(result, elem)))
print(c)
