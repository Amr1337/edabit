# https://edabit.com/challenge/Aj377wZtxWya7gjK9

def sum_missing_numbers(l):
    result = 0
    for i in range(min(l), max(l)):
        if i not in l:
            result += i
    return result


print(sum_missing_numbers([4, 3, 8, 1, 2]))
print(sum_missing_numbers([17, 16, 15, 10, 11, 12]))
print(sum_missing_numbers([1, 2, 3, 4, 5]))
print(sum_missing_numbers([-1, -4, -3, -2, -6, -8]))


'''
sum_missing_numbers([1, 2, 3, 4, 5]), 0)
sum_missing_numbers([4, 3, 8, 1, 2]), 18)
sum_missing_numbers([17, 16, 15, 10, 11, 12]), 27)
sum_missing_numbers([-1, -4, -3, -2, -6, -8]), -12)
'''