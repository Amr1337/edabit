# https://edabit.com/challenge/noqQNSr5o9qzvXWzL

def shift_to_right(n1, n2):
    top = n1
    bottom = 2 ** n2
    result = top // bottom
    return result

print(shift_to_right(80, 3)) #  ➞ 10
print(shift_to_right(-24, 2)) #  ➞ -6
print(shift_to_right(-5, 1)) # ➞ -3
print(shift_to_right(4666, 6)) # ➞ 72
print(shift_to_right(3777, 6)) # ➞ 59
print(shift_to_right(-512, 10)) # ➞ -1