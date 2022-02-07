# https://edabit.com/challenge/eJLwXpuaffjFnzENN

def find_even_nums(n):

    return [i for i in range(1,n+1) if i % 2 == 0]


print(find_even_nums(8))
print(find_even_nums(4))
print(find_even_nums(2))
print(find_even_nums(1))
print(find_even_nums(9))
print(find_even_nums(11))

'''
find_even_nums(4), [2, 4]
find_even_nums(8), [2, 4 ,6, 8]
find_even_nums(2), [2]
find_even_nums(1), [])
find_even_nums(9), [2, 4 ,6, 8])
find_even_nums(11), [2, 4 ,6, 8, 10])
'''