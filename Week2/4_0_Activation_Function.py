import math
#1. Sigmoid ( Logistic) Function

#Tinh chat ham: 0<= f <=1
#               x1 <= x2 thi f(x1) <= f(x2)
list_data = [1, 5, -4, 3, -2]

def sigmoid(data_list):
    result_sig = []

    for i in data_list:
        result_sig.append(1 / (1 + math.exp(-i)))

    return result_sig


result = sigmoid(list_data)
print(list_data)
print("Result of siugmoid function is: ")
print(result)

#2. Tanh function

def tanh(data_list):
    result_tanh = []

    for i in data_list:
        result_tanh.append(2 / (1 + math.exp(-2 * i)) - 1)

    return result_tanh


result = tanh(list_data)
print(list_data)
print("Result of tanh function is: ")
print(result)

#3. ReLU function

def ReLU(data_list):
    result = []

    for i in data_list:
        if (i < 0):
            result.append(0)
        else:
            result.append(i)

    return result


result = ReLU(list_data)
print(list_data)
print("Result of ReLU function is: ")
print(result)

#4. PReLU function

def PReLU(data_list, alpha):
    result = []

    for i in data_list:
        if (i < 0):
            result.append(alpha * i)
        else:
            result.append(i)

    return result

alpha = 0.1
result = PReLU(list_data, alpha)
print(list_data)
print("Result of PReLU function is: ")
print(result)

#5. ELU function

def ELU(data_list, alpha):
    result = []

    for i in data_list:
        if (i < 0):
            result.append(alpha * (math.exp(i) - 1))
        else:
            result.append(i)

    return result

result = ELU(list_data, alpha)
print(list_data)
print("Result of ELU function is: ")
print(result)

#6. Softplus Function

def Softplus(data_list):
    result = []

    for i in data_list:
        result.append(math.log(1 + math.exp(i)))

    return result

result = Softplus(list_data)
print(list_data)
print("Result of Softplus function is: ")
print(result)
