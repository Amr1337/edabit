# https://edabit.com/challenge/8oNKM4osgxYyrFtGL

def multiply(lst):
    return [[i]*len(lst) for i in lst]


print(multiply(["*", "%", "$"]))
print(multiply([4, 5]))
print(multiply(["A", "B", "C", "D", "E"]))
print(multiply([1]))

'''
multiply(["*", "%", "$"]), [["*", "*", "*"], ["%", "%", "%"], ["$", "$", "$"]])
multiply([4, 5]), [[4, 4], [5, 5]])
multiply(["A", "B", "C", "D", "E"]), [["A", "A", "A", "A", "A"], ["B", "B", "B", "B", "B"], ["C", "C", "C", "C", "C"], ["D", "D", "D", "D", "D"], ["E", "E", "E", "E", "E"]])
multiply([1]), [[1]])
'''