# https://edabit.com/challenge/7PtLRCT5aL9uiqxPs

def last_dig(a, b, c):
    if ((a % 10) * (b % 10)) % 10 == c % 10:
        return True
    else:
        return False


print(last_dig(1, 1, 1))
print(last_dig(12, 15, 10))
print(last_dig(15228, 9209, 72162))
print(last_dig(15, 1, 1))
print(last_dig(123, 15, 10))
print(last_dig(5213, 99219, 6165))
print(last_dig(1523, 513, 512))
print(last_dig(-12, 15, -10))



'''
last_dig(1, 1, 1), True)
last_dig(12, 15, 10), True)
last_dig(15228, 9209, 72162), True)
last_dig(15, 1, 1), False)
last_dig(123, 15, 10), False)
last_dig(5213, 99219, 6165), False)
last_dig(1523, 513, 512), False)
last_dig(-15, 1, 1), False, "Should work with negative numbers.")
last_dig(123, -15, 10), False, "Should work with negative numbers.")
last_dig(-12, 15, -10), True, "Should work with negative numbers.")
last_dig(15228, -9209, -72162), True, "Should work with negative numbers.")
'''