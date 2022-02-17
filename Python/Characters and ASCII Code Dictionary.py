# https://edabit.com/challenge/jpW2fAzfPtop8AYfW

def to_dict(l):
    d = dict()
    for i in l:
        d[i] = ord(i)
    return d


print(to_dict(["a", "b", "c"]))
print(to_dict(["!", ".", "?"]))
print(to_dict(["^"]))
print(to_dict([" "]))
print(to_dict([]))

'''
to_dict(["a", "b", "c"]), [{"a": 97}, {"b": 98}, {"c": 99}])
to_dict(["!", ".", "?"]), [{"!": 33}, {".": 46}, {"?": 63}])
to_dict(["^"]), [{"^": 94}])
to_dict([" "]), [{" ": 32}])
to_dict([]), [])

'''