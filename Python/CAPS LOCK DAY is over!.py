# https://edabit.com/challenge/aqA6KSHRCwfE44Q9m

def normalize(str):
    if str.isupper():
        print(str+"!")
    else:
        print(str)


normalize("CAPS LOCK DAY IS OVER")
normalize("Today is not caps lock day.")
normalize("WE WANT THIS COVID THING TO BE OVER")
normalize("Let us stay calm, no need to panic.")
normalize("DO NOT SHOUT")
normalize("Civilized conversation.")
'''
normalize("CAPS LOCK DAY IS OVER"), "Caps lock day is over!", )
normalize("Today is not caps lock day."), "Today is not caps lock day.")
normalize("WE WANT THIS COVID THING TO BE OVER"), "We want this covid thing to be over!")
normalize("Let us stay calm, no need to panic."), "Let us stay calm, no need to panic.")
normalize("DO NOT SHOUT"), "Do not shout!")
normalize("Civilized conversation."), "Civilized conversation.")
'''