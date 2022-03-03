# https://edabit.com/challenge/JiLom4d6aBk7wAJcZ
from math import sqrt, ceil, floor

def is_sastry(n):
    concat = int(str(n) + str(n+1))
    # check if both ceil and floor are valid then it matches
    if ceil(sqrt(concat)) == floor(sqrt(concat)):
        return True
    else:
        return False


print(is_sastry(183))
print(is_sastry(184))
print(is_sastry(106755))
print(is_sastry(129987253440921))
print(is_sastry(157175907513603))

'''
is_sastry(183), True, "Example #1")
is_sastry(184), False, "Example #2")
is_sastry(106755), True, "Example #3")
is_sastry(129987253440921), False)
is_sastry(157175907513603), True)
is_sastry(206611570247935), True)
is_sastry(338752188230098), False)
is_sastry(433610247875715), True)
is_sastry(652333983478884), False)
is_sastry(718717107443715), True)
is_sastry(752199872453889), False)
is_sastry(786704531939448), True)

'''