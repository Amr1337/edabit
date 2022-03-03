# https://edabit.com/challenge/vAS4Hp4wzSEnQs3tZ

def greetings(name):
    GUEST_LIST = {
        "Randy": "Germany",
        "Karla": "France",
        "Wendy": "Japan",
        "Norman": "England",
        "Sam": "Argentina"
    }
    if name not in GUEST_LIST.keys():
        return f"Hi! I'm a Guest"
    else:
        return f"Hi! I'm {name}, and I'm from {GUEST_LIST.get(name)}"


print(greetings("Randy"))
print(greetings("Sam"))
print(greetings("Monti"))
print(greetings("Trudy"))
print(greetings("Wendy"))
'''
greeting("Randy"), "Hi! I'm Randy, and I'm from Germany.")
greeting("Sam"), "Hi! I'm Sam, and I'm from Argentina.")
greeting("Monti"), "Hi! I'm a guest.")
greeting("Trudy"), "Hi! I'm a guest.")
greeting("Wendy"), "Hi! I'm Wendy, and I'm from Japan.")
'''