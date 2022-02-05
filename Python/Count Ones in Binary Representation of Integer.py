# https://edabit.com/challenge/GbyPdqNnp75Wci7Cn


def count_ones(num):
    return bin(num).count('1')


'''
count_ones(12), 2
count_ones(0), 0
count_ones(100), 3
count_ones(101), 4
count_ones(999), 8
count_ones(123456789), 16
count_ones(1234567890), 12

'''