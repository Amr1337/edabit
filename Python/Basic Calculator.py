# https://edabit.com/challenge/ZdnwC3PsXPQTdTiKf

def calculator(a, op ,b):
    if op == '/' and b != 0:
        return a // b
    if b == 0:
        return "Can't divide by 0"
    elif op == '+':
        return a + b
    elif op == '-':
        return  a - b
    elif op == '/' and b != 0:
        return a // b
    elif op == '*':
        return a * b

print(calculator(2, '/', 2))
print(calculator(10, '-', 7))
print(calculator(2, '*', 16))
print(calculator(2, '-', 2))
print(calculator(15, '+', 26))
print(calculator(2, '+', 2))
print(calculator(2, "/", 0))



'''
calculator(2, '/', 2), 1
calculator(10, '-', 7), 3
calculator(2, '*', 16), 32
calculator(2, '-', 2), 0
calculator(15, '+', 26), 41
calculator(2, '+', 2), 4
calculator(2, "/", 0), "Can't divide by 0!"
'''