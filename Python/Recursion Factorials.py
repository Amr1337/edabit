# https://edabit.com/challenge/pPyAgyeNEvQsBytaR

def factorial(n):
    if n == 1 or n == 0:
        return 1

    else:
        return n * factorial(n-1)


print(factorial(5))
print(factorial(3))
print(factorial(1))
print(factorial(0))


'''
factorial(5), 120)
factorial(3), 6)
factorial(1), 1)
factorial(0), 1)

'''