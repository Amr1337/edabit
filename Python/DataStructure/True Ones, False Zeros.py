# https://edabit.com/challenge/58DYAThA2dxnAsMpL

def integer_boolean(str):
    l = []
    for i in str:
        if i == '1':
            l.append(True)
        else:
            l.append(False)
    return l


print(integer_boolean("100101"))
print(integer_boolean("10"))
print(integer_boolean("001"))
print(integer_boolean(""))
print(integer_boolean("111"))
print(integer_boolean("000"))
print(integer_boolean("10010110"))

'''
Tinteger_boolean("100101"), [True, False, False, True, False, True])
integer_boolean("10"), [True, False])
integer_boolean("001"), [False, False, True])
integer_boolean(""), [])
integer_boolean("111"), [True, True, True])
integer_boolean("000"), [False, False, False])
integer_boolean("10010110"), [True, False, False, True, False, True, True, False])

'''