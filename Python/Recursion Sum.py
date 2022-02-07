# https://edabit.com/challenge/si2H6WC5YX99cn6LQ

def sum_numbers(n):
    if n == 1:
        return 1
    else:
        return n + sum_numbers(n - 1)


print(sum_numbers(1))
print(sum_numbers(5))
print(sum_numbers(7))
print(sum_numbers(10))
print(sum_numbers(12))
print(sum_numbers(15))
print(sum_numbers(20))
print(sum_numbers(100))

'''
sum_numbers(1), 1)
sum_numbers(5), 15)
sum_numbers(7), 28)
sum_numbers(10), 55)
sum_numbers(12), 78)
sum_numbers(15), 120)
sum_numbers(20), 210)
sum_numbers(100), 5050)
'''
