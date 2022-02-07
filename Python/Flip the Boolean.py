# https://edabit.com/challenge/NLY7zGMYocsTbeS6n

def reverse(c):
    if c is True:
        return False
    else:
        if c is False:
            return True
        else:
            return "boolean expected"


print(reverse(True))
print(reverse(False))
print(reverse(0))
print(reverse(None))
print(reverse(""))
print(reverse({}))

'''
reverse(False), True)
reverse(True), False)
reverse(0), "boolean expected")
reverse(None), "boolean expected")
reverse(""), "boolean expected")
reverse({}), "boolean expected")
'''
