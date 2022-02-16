# https://edabit.com/challenge/o2AKq4xy3nfZabKXL

def solutions(a, b, c):

    # formula used for discrimination is:
    # b^2 - 4ac

    if b**2 - 4*a*c > 0:
        return 2
    elif b**2 - 4*a*c == 0:
        return 1
    elif b**2 - 4*a*c < 0:
        return 0


print(solutions(1, 0, -1))
print(solutions(1, 0, 0))
print(solutions(1, 0, 1))
print(solutions(200, 420, 800))
print(solutions(200, 420, -800))

'''
solutions(1, 0, -1), 2)
solutions(1, 0, 0), 1)
solutions(1, 0, 1), 0)
solutions(200, 420, 800), 0)
solutions(200, 420, -800), 2)
solutions(1000, 1000, 0), 2)
solutions(10000, 400, 4), 1)
'''