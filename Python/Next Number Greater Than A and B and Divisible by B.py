# https://edabit.com/challenge/2bTdN8sr3PQKkLHur

def divisible_by_b(a, b):
    next_bigger = a + 1
    while next_bigger % b != 0 and (next_bigger > a and b):
        next_bigger += 1
        if next_bigger % b == 0:
            return next_bigger
    return next_bigger


print(divisible_by_b(17, 8))
print(divisible_by_b(98, 3))
print(divisible_by_b(14, 11))
print(divisible_by_b(11, 8))
print(divisible_by_b(450, 36))
print(divisible_by_b(1019, 13))

'''
divisible_by_b(17, 8), 24)
divisible_by_b(98, 3), 99)
divisible_by_b(14, 11), 22)
divisible_by_b(11, 8), 16)
divisible_by_b(450, 36), 468)
divisible_by_b(1019, 13), 1027)
'''