# https://edabit.com/challenge/2zKetgAJp4WRFXiDT

def number_length(num):
    num = str(num)
    count = 0
    for i in num:
        count += 1
    return count

print(number_length(10))
print(number_length(5000))
print(number_length(0))
print(number_length(4039182))
print(number_length(9999999999999999))
print(number_length(1))
print(number_length(777777777777777777777777777777))




'''
number_length(10), 2)
number_length(5000), 4)
number_length(0), 1)
number_length(4039182), 7)
number_length(9999999999999999), 16)
number_length(1), 1)
number_length(777777777777777777777777777777), 30)
'''