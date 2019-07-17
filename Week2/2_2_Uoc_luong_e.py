N = 10

e = 1.0

def factorial(n):
    if n == 0:
      return 1
    result = 1;
    for i in range(2, n+1):
      result = result * i

    return result


for i in range(1, N+1):
     e = e + 1/float(factorial(i))

print(e)
