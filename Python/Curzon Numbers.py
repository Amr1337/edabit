# https://edabit.com/challenge/HYjQKDXFfeppcWmLX

def is_curzon(n):
    return not (2 ** n + 1) % (2 * n + 1)


'''is_curzon(5), True
is_curzon(10), False
is_curzon(14), True
is_curzon(86), True
is_curzon(90), True
is_curzon(115), False
is_curzon(120), False
is_curzon(194), True
is_curzon(293), True

'''
