# https://edabit.com/challenge/hGzNSr5CSEpTsmy5W

def not_good_math(n, k):
    while n % 10 != 0:
        n = n - range(1, k)

    return n // 10

#print(not_good_math(22, 3))
print(not_good_math(540, 5))