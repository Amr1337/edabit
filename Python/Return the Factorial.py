# https://edabit.com/challenge/FF6kYPHdAcJnoosr5

def factorial(n):
    fact =1
    for i in range(n,0,-1):
        fact *= i
    return fact
'''
import math
alternative pythonic method:
n = input()
print(math.factorial(n))
'''
print(factorial(2))
print(factorial(6))
print(factorial(3))
print(factorial(12))
print(factorial(5))

'''
factorial(2), 2
factorial(6), 720
factorial(3), 6
factorial(12), 479001600)
factorial(5), 120)

'''