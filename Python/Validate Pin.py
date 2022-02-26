# https://edabit.com/challenge/xG2KB9T7mHgycGCSz

def valid(pin):
    if len(pin) == 4 or len(pin) == 6 and pin.isdigit():
        return True
    else:
        return False


'''print(valid("1234"))
print(valid("45135"))
print(valid("89abc1"))
print(valid("900876"))
print(valid(" 4983"))
print(valid(" "))'''

tests = [
    ['123456', True],
    ['4512a5', False],
    ['', False],
    ['21904', False],
    ['9451', True],
    ['213132', True],
    [' 4520', False],
    ['15632 ', False],
    ['000000', True]
]

for test in tests:
    if valid(test[0]) == test[1]:
        print(test[1])
    else:
        print("Issue found")