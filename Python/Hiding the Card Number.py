# https://edabit.com/challenge/iRCwdDBkNcHM5QeAm

def card_hide(card_number):
    card_size = len(card_number)
    card_but_last = card_size - 4
    last_digits = (card_but_last * "*") + card_number[-5:-1]
    print(last_digits)

card_hide("1234123456785678")
card_hide("8754456321113213")
card_hide("35123413355523")

'''
card_hide("1234123456785678"), "************5678"
card_hide("8754456321113213"), "************3213"
card_hide("35123413355523"), "**********5523"
'''