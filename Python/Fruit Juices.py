# https://edabit.com/challenge/Mv5qSgZKTLrLt9zzW

def get_drink_ID(name, capacity):
    cap = ""
    for i in capacity:
        if i.isdigit():
            cap += cap.join(i)
    n = ""
    # splits the sentence to lists of words and slice each word
    # with first 3 letters
    for i in name.split(" "):
        n += i[:3]
    return (n + cap).upper()


print(get_drink_ID("apple", "500ml"))
print(get_drink_ID("pineapple", "45ml"))
print(get_drink_ID("orange", "750ml"))
print(get_drink_ID("passion fruit", "1ml"))
print(get_drink_ID("mango", "1000ml"))
print(get_drink_ID("very berry", "253ml"))
print(get_drink_ID("raspberry and lime", "350ml"))

'''
get_drink_ID("apple", "500ml"), "APP500")
get_drink_ID("pineapple", "45ml"), "PIN45")
get_drink_ID("orange", "750ml"), "ORA750")
get_drink_ID("passion fruit", "1ml"), "PASFRU1")
get_drink_ID("mango", "1000ml"), "MAN1000")
get_drink_ID("very berry", "253ml"), "VERBER253")
get_drink_ID("raspberry and lime", "350ml"), "RASANDLIM350")
'''