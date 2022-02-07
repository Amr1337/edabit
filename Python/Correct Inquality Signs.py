# https://edabit.com/challenge/eA94BuKYjwMoNQSE2

def correct_signs(str):
    return eval(str)

print(correct_signs("3 < 7 < 11"))
print(correct_signs("13 > 44 > 33 > 1"))
print(correct_signs("1 < 2 < 6 < 9 > 3"))
print(correct_signs("4 > 3 > 2 > 1"))
print(correct_signs("5 < 7 > 1"))
print(correct_signs("5 > 7 > 1"))
print(correct_signs("9 < 9"))


'''
correct_signs("3 < 7 < 11"), True)
correct_signs("13 > 44 > 33 > 1"), False)
correct_signs("1 < 2 < 6 < 9 > 3"), True)
correct_signs("4 > 3 > 2 > 1"), True)
correct_signs("5 < 7 > 1"), True)
correct_signs("5 > 7 > 1"), False)
correct_signs("9 < 9"), False)
'''