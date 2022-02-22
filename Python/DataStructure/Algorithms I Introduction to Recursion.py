# https://edabit.com/challenge/x6McEkHer8A3Hke2q

def factorial(num):
    if num == 1:
        return num
    else:
        return num*factorial(num-1)

print(factorial(5))

'''
factorial(7), 5040)
factorial(1), 1)
factorial(9), 362880)
factorial(2), 2)

'''