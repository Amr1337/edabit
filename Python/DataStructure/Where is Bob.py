# https://edabit.com/challenge/fDkAuAwR4PMWZwBKs

def find_bob(lst):
    index = -1
    for idx in range(len(lst)):
        if lst[idx] == "Bob":
            index = idx
    return index


print(find_bob(["Jimmy", "Layla", "Bob"])) # 2
print(find_bob(["Bob", "Layla", "Kaitlyn", "Patricia"])) # 0
print(find_bob(["Jimmy", "Layla", "James"])) # -1
print(find_bob(["Paul", "Layla", "Bob"])) # 2
print(find_bob(["Garry", "Maria", "Bethany", "Bob", "Pauline"])) # 3