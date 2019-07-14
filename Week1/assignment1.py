import math

def der_Identity(x):
    return 1

def der_Logistic(x):
    return math.exp(-x) / pow((1 + math.exp(-x)), 2)

def der_Tanh(x):
    return 2 * der_Logistic(2*x)

def der_ReLU(x):
    if x < 0:
      return 0
    else:
      return 1

def der_PReLU(x, alpha):
    if x < 0:
      return alpha
    else:
      return 1

def der_ELU(x, alpha):
    if x < 0:
      return alpha * math.exp(x)
    else:
      return 1

def der_SoftPlus(x):
    return math.exp(x) / (1 + math.exp(x))

x = 1
alpha = 10
print(der_Identity(x))
print(der_Logistic(x))
print(der_Tanh(x))
print(der_ReLU(x))
print(der_PReLU(x, alpha))
print(der_ELU(x, alpha))
print(der_SoftPlus(x))
