#########Statistics - So lieu thong ke##########
from collections import Counter #import pakages Counter de dem so lan xuat hien cua moi gia tri trong chuoi
import time

donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]

#1. Mean <Gia tri trung binh>
print("Donations is: ");
print(donations)
def calculate_Mean(numbers):
    s = sum(numbers) #tong cac phan tu trong list
    N = len(numbers)  #so luong phan tu cua list
    mean = float(s) /float(N)
    return mean

start = time.time()
mean_value = calculate_Mean(donations)
print("Mean of donations is: %f" % mean_value)
print("Time to run function calculate_Mean is: ", (time.time()-start)*1000)

#2. Median
def calculate_Median(numbers):
    N = len(numbers)
    numbers.sort()  #Sap xep chuoi numbers theo chieu tu nho den lon
    if N % 2 == 0:
        m1 = N / 2
        m2 = N / 2 + 1
        m1 = int(m1) - 1
        m2 = int(m2) - 1
        median = (numbers[m1] + numbers[m2]) / 2
    else:
        m = (N + 1) / 2
        m = int(m) - 1
        median = numbers[m]

    return median

median_value = calculate_Median(donations)
print("Median of donations is: ", median_value)

#3. Mode

score = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10, 6, 6]
print("\nSocre of sudents is: ")
print(score)
def calculate_Mode(numbers):
    c = Counter(numbers)  #ham dem so lan xuat hien cua moi phan tu trong numbers, dai dien boi c
    mode = c.most_common(1)  #truyen vao 1, tra ve gia tri va so lan xuat hien cua phan tu cuat hien nhieu nhat, dai dien boi mode

    return mode[0][0]  #phan gia tri cua mode

mode_value = calculate_Mode(score)
print("Mode of students's score is: ", mode_value)

#case : have many of mode_value are same
def calculate_Mode_adv(numbers):
    c = Counter(numbers)
    number_freq = c.most_common()
    max_count = number_freq[0][1]  #gia tri tan so xuat hien nhieu nhat
    modes = []
    for num in number_freq:
        if num[1] == max_count:
            modes.append(num[0])

    return modes

modes_value = calculate_Mode_adv(score)
print("Modes of score is: ", modes_value)

#4. Range of data (Do phan tan -- do lech giua gia tri lon nhat va gia tri nho nhat)

def find_Range(numbers):
    lowest = min(numbers)
    highest = max(numbers)

    r = highest - lowest

    print("Lowest: {0}\tHighest: {1}\tRange: {2}" .format(lowest, highest, r))

find_Range(score)

#5. Variance - Phuong sai (Su khac biet tat ca cac gia tri trong tap tap du lieu co khac biet nhieu so voi gia tri trung binh hay ko -->muc do phan tan cua du lieu)
# Do lech chuan = CBH phuong sai
#Cong thuc tinh phuong sai = tong[(tung gia tri - mean)^2]/so luong phan tu

points = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]
print("\nPoints List: ")
print(points)

def calculate_Variance(numbers):
    mean = calculate_Mean(numbers)
    N = len(numbers)

    diff = []
    for num in numbers:
        diff.append(num - mean)

    squared_diff = []
    for i in diff:
        squared_diff.append(i ** 2)

    sum_squared_diff = sum(squared_diff)
    variance = sum_squared_diff / N

    return variance

print("Variance of points is: ", calculate_Variance(points))
print("Standard deviation of pointss is: ", calculate_Variance(points) ** 0.5)
