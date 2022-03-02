# https://edabit.com/challenge/6dnhESWBcTMMF3gsa

def stupid_addition(n1, n2):
    if type(n1) != type(n2):
        return None
    else:
        if type(n1) == type(n2) == int:
            return str(n1) + str(n2)
        else:
            return int(n1) + int(n2)


print(stupid_addition(1, 2))
print(stupid_addition("2", "2"))
print(stupid_addition(1, "2"))
print(stupid_addition("1", 2))


'''
stupid_addition(1, 2), "12", "Both parameters are integers, therefore they should be concatenated"
stupid_addition("1", "2"), 3, "Both parameters are strings, therefore they should be added")
stupid_addition(1, "2"), None, "The parameters are different data types, therefore None should be returned"
stupid_addition("1", 2), None, "The parameters are different data types, therefore None should be returned"
'''