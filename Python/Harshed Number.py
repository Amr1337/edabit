# https://edabit.com/challenge/eADRy5SA5QbasA3Qt

def is_harshed(n):
    sum = 0
    temp = n
    while temp > 0:
        sum += temp % 10
        temp = temp // 10
    if n % sum == 0:
        return True
    else:
        return False


'''for i in str(n):
        sum+= int(i)
    if n % sum == 0:
        print(True)
    else:
        print(False)'''

print(is_harshed(75))
print(is_harshed(171))
print(is_harshed(516))
print(is_harshed(89))

'''
is_harshad(75) ➞ False
# 7 + 5 = 12
# 75 is not exactly divisible by 12
 
is_harshad(171) ➞ True
# 1 + 7 + 1 = 9
# 9 exactly divides 171
 
is_harshad(481) ➞ True

is_harshad(89) ➞ False

is_harshad(516) ➞ True

is_harshad(200) ➞ True
'''
