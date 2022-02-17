# https://edabit.com/challenge/5KqHNS9wS97zN7Xyy

def top_note(d):
    d1 = dict()
    d1["name"] = d["name"]
    d1["top_note"] = max(d["notes"])
    return d1


print(top_note({"name": "John", "notes": [3, 5, 4]}))
print(top_note({"name": "Max", "notes": [1, 4, 6]}))
print(top_note({"name": "Zygmund", "notes": [1, 2, 3]}))


'''
top_note({"name": "Jacek", "notes":[5, 4, 3]}), {"name": "Jacek", "top_note":5})
top_note({"name": "Ewa", "notes":[3,3,3]}), {"name": "Ewa", "top_note":3})
top_note({"name": "Zygmund", "notes":[1,2,3]}), {"name": "Zygmund", "top_note":3})
top_note({"name": "Alex", "notes":[1,4,6]}), {"name": "Alex", "top_note":6})

'''