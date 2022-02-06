# https://edabit.com/challenge/JSJEuuWduBB5hEX6k

def XO(str):
    lower_str = str.lower()
    if lower_str.count('x') == lower_str.count('o') == 0:
        return True
    else:
        if str.lower().count('x') == str.lower().count('o'):
            return True
        else:
            return False

print(XO("ooxx"))
print(XO("xooxx"))
print(XO("ooxXm"))
print(XO("zpzpzpp"))
print(XO("zzoo"))
print("")

print(XO("Xo"))
print(XO("x"))
print(XO("xxxoo"))
print(XO(""))
'''
XO("Xo"), True
XO("x"), False
XO("o"), False
XO("xxxoo"), False
XO(""), True
'''