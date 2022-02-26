# https://edabit.com/challenge/yL5WmWTCNwwb4GnR7

def return_unique(lst):
    unique_items = []
    for i in lst:
        if lst.count(i) == 1:
            unique_items.append(i)
    return unique_items


print(return_unique([1, 9, 8, 8, 7, 6, 1, 6]))
print(return_unique([5, 5, 2, 4, 4, 4, 9, 9, 9, 1]))
print(return_unique([9, 5, 6, 8, 7, 7, 1, 1, 1, 1, 1, 9, 8]))
