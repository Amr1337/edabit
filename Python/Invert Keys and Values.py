# https://edabit.com/challenge/Axim3Ld5zu9RFLZKr

def invert(d):
    inv_d = {v:k for k,v in d.items()}
    return inv_d


print(invert({ "z": "q", "w": "f" }))
print(invert({ "a": 1, "b": 2, "c": 3 }))
print(invert({ "zebra": "koala", "horse": "camel" })
)