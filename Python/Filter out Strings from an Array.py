# https://edabit.com/challenge/nunJurLEibCyn8fzn

def filter_list(lst):
    new = []
    for i in lst:
        # check if items are of int type and append to new list
        # common mistake: don't pop or remove items from the list
        # you're using in the for loop as it will reduce the length of it.
        if isinstance(i, int):
            new.append(i)
    return new



print(filter_list([1, 2, "a", "b"]))
print(filter_list([1, "a", "b", 0, 15]))
print(filter_list([1, 2, "aasf", "1", "123", 123]))
print(filter_list(["jsyt", 4, "yt", "6"]))
print(filter_list(["r", 5, "y", "e", 8, 9]))
print(filter_list(["a", "e", "i", "o", "u"]))
print(filter_list([4, "z", "f", 5]))
print(filter_list(["$%^", 567, "&&&"]))



'''
filter_list([1, 2, "a", "b"]), [1, 2])
filter_list([1, "a", "b", 0, 15]), [1, 0, 15])
filter_list([1, 2, "aasf", "1", "123", 123]), [1, 2, 123])
filter_list(["jsyt", 4, "yt", "6"]), [4])
filter_list(["r", 5, "y", "e", 8, 9]), [5, 8, 9])
filter_list(["a", "e", "i", "o", "u"]), [])
filter_list([4, "z", "f", 5]), [4, 5])
filter_list(["abc", 123]), [123])
filter_list(["$%^", 567, "&&&"]), [567])
filter_list(["w", "r", "u", 43, "s", "a", 76, "d", 88]), [43, 76, 88])
'''