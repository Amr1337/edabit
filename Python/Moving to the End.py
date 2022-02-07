# https://edabit.com/challenge/nTW4KgmJxpLDXcWPt

def move_to_end(lst, n):
    for i in lst:
        if i == n:
            lst.remove(n)
            lst.append(n)
    '''print([lst1 for lst1 in lst if lst1 != n] +
          [lst2 for lst2 in lst if lst2 == n])'''
    print(lst)

move_to_end([1, 3, 2, 4, 4, 1], 1)
move_to_end([7, 8, 9, 1, 2, 3, 4], 9)
move_to_end([7, 7, 7, 6, 6, 6, 6], 7)
move_to_end(["a", "c", "c", "c", "b", "c"], "b")
move_to_end(["a", "c", "c", "c", "b", "c"], "c")
move_to_end(["a", "a", "a", "b"], "a")

'''
move_to_end([1, 3, 2, 4, 4, 1], 1), [3, 2, 4, 4, 1, 1]
move_to_end([7, 8, 9, 1, 2, 3, 4], 9), [7, 8, 1, 2, 3, 4, 9]
move_to_end([7, 7, 7, 6, 6, 6, 6], 7), [6, 6, 6, 6, 7, 7, 7]
move_to_end(["a", "c", "c", "c", "b", "c"], "b"), ["a", "c", "c", "c", "c", "b"])
move_to_end(["a", "c", "c", "c", "b", "c"], "c"), ["a", "b", "c", "c", "c", "c"])
move_to_end(["a", "a", "a", "b"], "a"), ["b", "a", "a", "a"]
'''