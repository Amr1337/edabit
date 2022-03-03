# https://edabit.com/challenge/jwzgYjymYK7Gmro93

def get_indices(lst, item):
    indices = []
    for i in range(len(lst)):
        if lst[i] == item:
            indices.append(i)
    return indices


print(get_indices(['a', 'a', 'b', 'a', 'b', 'a'], 'a'))
print(get_indices([1, 5, 5, 2, 7], 7))
print(get_indices([1, 2, 3, 4], 5))
print(get_indices([1, 5, 5, 2, 7], 5))
print(get_indices([8, 8, 8, 8, 8], 8))
print(get_indices([True, False, True, False], True))

'''
get_indices(['a', 'a', 'b', 'a', 'b', 'a'], 'a'), [0, 1, 3, 5])
get_indices([1, 5, 5, 2, 7], 7), [4])
get_indices([1, 5, 5, 2, 7], 5),[1, 2])
get_indices([1, 5, 5, 2, 7], 8), [])
get_indices([8, 8, 8, 8, 8], 8), [0, 1, 2, 3, 4])
get_indices([8, 8, 7, 8, 8], 8), [0, 1, 3, 4])
get_indices([True, False, True, False], True), [0, 2])
get_indices([True, False, True, False], False), [1, 3])
'''
