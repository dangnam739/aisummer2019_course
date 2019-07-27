from collections import Counter

file = open('Iris.csv', 'r')

#readline giup viec doc file theo tung dong, moi dong la 1 chuoi
lines = file.readlines()

#print 10 frist line
# for i in range(10):
#     print(lines[i])

# file.close()

#dung ham splip() de phan tach cac cot gia tri
for i in range(10):
    feature = lines[i].split(',')
    print('%s | %s | %s | %s | %s | %s' %(feature[0], feature[1], feature[2], feature[3], feature[4], feature[5]))

file.close()
print('\n------------------------------------\n')

for i in range(1, 10):
    feature = lines[i].split(',')
#strip() dung d xoa khoang trang o hai dau string
    sepal_length = float(feature[1].strip())
    sepal_width  = float(feature[2].strip())
    pedal_length = float(feature[3].strip())
    pedal_width  = float(feature[4].strip())

    species = 0
    if feature[5].strip() == 'Iris-versicolor':
        species = 1
    elif feature[5].strip() == 'Iris-virginica':
        species = 2

    print('| %s | %s | %s | %s | %s |' %(sepal_length, sepal_width, pedal_length, pedal_width, species))

print('\n------------------------------------\n')
## Luu tat ca vao mot list
data_Iris = []
for i in range(1, len(lines)):
    feature = lines[i].split(',')

    sepal_length = float(feature[1].strip())
    sepal_width = float(feature[2].strip())
    pedal_length = float(feature[3].strip())
    pedal_width = float(feature[4].strip())

    species = 0
    if feature[5].strip() == 'Iris-versicolor':
        species = 1
    elif feature[5].strip() == 'Iris-virginica':
        species = 2

    data_Iris.append([sepal_length, sepal_width, pedal_length, pedal_width, species])

file.close()

print(data_Iris[0])
print(data_Iris[50])
print(data_Iris[100])

#Tinh cac dac trung cua tung thuoc tinh
print('\n------------------------------------\n')
print('Tinh cac dac trung cua tung thuoc tinh Iris\n')

#Cac ham thong ke

def calculate_Mean(numbers):
    s = sum(numbers)  # tong cac phan tu trong list
    N = len(numbers)  # so luong phan tu cua list
    mean = float(s) / float(N)
    return mean


def calculate_Median(numbers):
    N = len(numbers)
    numbers.sort()  # Sap xep chuoi numbers theo chieu tu nho den lon
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


def calculate_Mode(numbers):
    # ham dem so lan xuat hien cua moi phan tu trong numbers, dai dien boi c
    c = Counter(numbers)
    # truyen vao 1, tra ve gia tri va so lan xuat hien cua phan tu cuat hien nhieu nhat, dai dien boi mode
    mode = c.most_common(1)

    return mode[0][0]  # phan gia tri cua mode


def calculate_Mode_adv(numbers):
    c = Counter(numbers)
    number_freq = c.most_common()print('+{:-^30}+{:-^20}+{:-^10}+{:-^10}+{:-^20}+'.format('', '', '', '', ''))
    max_count = number_freq[0][1]  # gia tri tan so xuat hien nhieu nhat
    modes = []
    for num in number_freq:
        if num[1] == max_count:
            modes.append(num[0])

    return modes


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

def calculate_Standard_Deviation(numbers):
    return calculate_Variance(numbers)** 0.5

def calculate_Min(numbers):
    return min(numbers)

def calculate_Max(numbers):
    return max(numbers)

#Tach cac du lieu vao tung thuoc tinh tu data
sepal_length_list = []
sepal_width_list = []
pedal_length_list = []
pedal_width_list = []
species_list = []

for feature in data_Iris:
    sepal_length_list.append(feature[0])
    sepal_width_list.append(feature[1])
    pedal_length_list.append(feature[2])
    pedal_width_list.append(feature[3])
    species_list.append(feature[4])

print('+{:-^30}+{:-^20}+{:-^10}+{:-^10}+{:-^20}+'.format('', '', '', '', ''))
print('|{:^30}|{:^20}|{:^10}|{:^10}|{:^20}|'.format('Feature', 'Mean', 'Min', 'Max', 'Standard Deviation'))
print('+{:-^30}+{:-^20}+{:-^10}+{:-^10}+{:-^20}+'.format('', '', '', '', ''))
#Sepal_Length
print('|{:<30}|{:<20}|{:<10}|{:<10}|{:<20}|'.format('Sepal Length', calculate_Mean(sepal_length_list),
                                                                    calculate_Min(sepal_length_list),
                                                                    calculate_Max(sepal_length_list), calculate_Standard_Deviation(sepal_length_list)))
#Sepal width
print('|{:<30}|{:<20}|{:<10}|{:<10}|{:<20}|'.format('Sepal Width', calculate_Mean(sepal_width_list),
                                                                   calculate_Min(sepal_width_list),
                                                                   calculate_Max(sepal_width_list), calculate_Standard_Deviation(sepal_width_list)))
#Pedal Length
print('|{:<30}|{:<20}|{:<10}|{:<10}|{:<20}|'.format('Pedal Length', calculate_Mean(pedal_length_list),
                                                                    calculate_Min(pedal_length_list),
                                                                    calculate_Max(pedal_length_list), calculate_Standard_Deviation(pedal_length_list)))
#Pedal Width
print('|{:<30}|{:<20}|{:<10}|{:<10}|{:<20}|'.format('Pedal Width', calculate_Mean(pedal_width_list),
                                                                   calculate_Min(pedal_width_list),
                                                                   calculate_Max(pedal_width_list), calculate_Standard_Deviation(pedal_width_list)))
#species
print('|{:<30}|{:<20}|{:<10}|{:<10}|{:<20}|'.format('Species', calculate_Mean(species_list),
                                                               calculate_Min(species_list),
                                                               calculate_Max(species_list),
                                                               calculate_Standard_Deviation(species_list)))
print('+{:-^30}+{:-^20}+{:-^10}+{:-^10}+{:-^20}+'.format('', '', '', '', ''))
