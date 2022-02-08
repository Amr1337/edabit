# https://edabit.com/challenge/EZMCpHaNFg2Yfsnxx

def unique_sort(lst):
    l = list(set(lst))
    # could use just --> l.sort()
    lastElementIndex = len(l)-1
    # using bubble sort
    for passNo in range(lastElementIndex, 0, -1):
        for idx in range(passNo):
            if l[idx] > l[idx+1]:
                l[idx], l[idx+1] = l[idx+1], l[idx]
    return l


print(unique_sort([1, 2, 4, 3]))
print(unique_sort([1, 4, 4, 4, 4, 4, 3, 2, 1, 2]))
print(unique_sort([6, 7, 3, 2, 1]))
print(unique_sort([1, 5, 8, 2, 3, 4, 4, 4, 10]))
print(unique_sort([1, 2, 5, 4, 7, 7, 7]))
print(unique_sort([7, 6, 5, 4, 3, 2, 1, 0, 1]))
print(unique_sort([3, 6, 5, 4, 3, 27, 1, 100, 1]))
print(unique_sort([-9, -3.1414, -87, 8, -4.323827, -3.1415, -3.1415]))

'''
unique_sort([1, 5, 8, 2, 3, 4, 4, 4, 10]),
  [1, 2, 3, 4, 5, 8, 10]

unique_sort([1, 2, 5, 4, 7, 7, 7]),
  [1, 2, 4, 5, 7]
unique_sort([7, 6, 5, 4, 3, 2, 1, 0, 1]),
  [0, 1, 2, 3, 4, 5, 6, 7]
unique_sort([3, 6, 5, 4, 3, 27, 1, 100, 1]),
  [1, 3, 4, 5, 6, 27, 100]
unique_sort([-9, -3.1414, -87, 8, -4.323827, -3.1415, -3.1415]),
  [-87, -9, -4.323827, -3.1415, -3.1414, 8]
'''
