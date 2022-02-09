# https://edabit.com/challenge/5XXXppAdfcGaootD9

def sum_odd_and_even(lst):
    result_list = []
    # using generator instead of list comprehension
    result = sum((i for i in lst if i % 2 ==0))
    result_list.append(result)
    result = sum(((i for i in lst if i % 2 !=0)))
    result_list.append(result)
    return result_list


print(sum_odd_and_even([1, 2, 3, 4, 5, 6]))
print(sum_odd_and_even([-1, -2, -3, -4, -5, -6]))
print(sum_odd_and_even([0, 0]))
print(sum_odd_and_even([]))



'''
sum_odd_and_even([-1, -2, -3, -4, -5, -6]), [-12, -9])
sum_odd_and_even([0, 0]), [0, 0])
sum_odd_and_even([]), [0, 0])
'''