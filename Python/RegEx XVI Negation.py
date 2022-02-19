# https://edabit.com/challenge/5zDR5LyznNPsnEuYJ

import re


def find_reg(txt):
    # return anything that is not a word
    print(re.findall("[^\w\s]", txt))


find_reg(" alice15@gmail.com ")  # ["@", "."]
