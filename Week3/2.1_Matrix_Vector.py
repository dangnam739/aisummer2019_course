import math
####################Vector##########################
#Cong Vector
def add_vector(vector1, vector2):
    return [v1 + v2 for v1, v2 in zip(vector1, vector2)]

#Tru 2 vector
def minus_vector(vector1, vector2):
    return [v1 - v2 for v1, v2 in zip(vector1, vector2)]

#Do dai vector
def length_vector(vector):
    square_length = 0
    resutl
    for i in vector:
        square_length += i ** 2

    return square_length ** 0.5

#Nhan vecto voi mot so
def mul_vector(vector, alpha):
    mul = []
    for i in vector:
        mul.append(i*alpha)

    return mul

#Nhan 2 vector
def dot_product(vector1, vector2):
    return sum([v1*v2 for v1, v2 in zip(vector1, vector2)])

#Hadamard product(schur product)
# u*v = (u1v1, u2v2, u3v3)
def Hadamard_product(vector1, vector2):
    return [v1 * v2 for v1, v2 in zip(vector1, vector2)]

#Cos(u,v) : Cos goc giua hai vector
def cosin_similarity(vector1, vector2):
    sumxy = sum([v1 * v2 for v1, v2 in zip(vector1, vector2)])
    sumxx = sum([v1 * v2 for v1, v2 in zip(vector1, vector1)])
    sumyy = sum([v1 * v2 for v1, v2 in zip(vector2, vector2)])

    return sumxy / math.sqrt(sumxx * sumyy)

vector1 = [1, 2]
vector2 = [3, 4]

print(add_vector(vector1, vector2))
print(minus_vector(vector1, vector2))
print(length_vector(vector1))
print(mul_vector(vector1,2))
print(dot_product(vector1, vector2))
print(Hadamard_product(vector1, vector2))

vector1 = [5, 3, 2, 7]
vector2 = [2, 9, 4, 1]
print(cosin_similarity(vector1, vector2))

###################Matrix############################
#Matrix Multiplication
def matrix_multiplication(matrix1, matrix2):
    matrix1_nrows = len(matrix1)
    matrix1_nclos = len(matrix1[0])

    matrix2_nrows = len(matrix2)
    matrix2_nclos = len(matrix2[0])

    #create result matrix
    result = [[0] * matrix2_nclos for i in range(matrix1_nrows)]

    for i in range(matrix1_nrows):
        for j in range(matrix2_nclos):
            for k in range(matrix2_nrows):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

matrix1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
matrix2 = [[1, 1, 2, 1],
           [1, 2, 1, 1],
           [1, 1, 1, 2]]

resutl = matrix_multiplication(matrix1, matrix2)
print(resutl)
