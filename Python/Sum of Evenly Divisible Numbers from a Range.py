# https://edabit.com/challenge/nWtgKSNGQ3sB52rQ8

def evenly_divisible(a, b, c):
    total = 0
    for i in range(a, b+1):
        if i % c == 0:
            total += i
    return total

print(evenly_divisible(1, 10, 2))
print(evenly_divisible(1, 10, 3))
print(evenly_divisible(0, 12, 3))
print(evenly_divisible(-10, -1, 2))
print(evenly_divisible(-10, -1, 3))
print(evenly_divisible(1, 10, 20))
print(evenly_divisible(-10, 10, 2))


'''
evenly_divisible(1, 10, 2), 30
evenly_divisible(1, 10, 3), 18
evenly_divisible(0, 12, 3), 30
evenly_divisible(-10, -1, 2), -30
evenly_divisible(-10, -1, 3), -18
evenly_divisible(1, 10, 20), 0
evenly_divisible(-10, 10, 2), 0

'''