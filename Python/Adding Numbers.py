# https://edabit.com/challenge/2RtztnzMDdyAj2MD3

def add(s1, s2):
    if (s1 is None or s1 == "") or (s2 is None or s2 == ""):
        print("Invalid Operation")
    else:
        return str(int(s1)+int(s2))


print(add("111", "111"))
print(add("91", "19"))
print(add("123456789", "987654322"))


"""
add("91", "19"), "110")
add("123456789", "987654322"), "1111111111")
add("9999999", "1"), "10000000")
add("300", "3000"), "3300")
add("1000", "6200"), "7200")
add("-10", "-20"), "-30")
add("-100", "100"), "0")
add("0", "6200"), "6200")
add("", "6"), "Invalid Operation")
add("", None), "Invalid Operation")
add(None, "23"), "Invalid Operation")
add("", "20"),"Invalid Operation")
"""