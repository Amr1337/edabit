# https://edabit.com/challenge/cXnkmRdxqJrwdsP4n

def dis(price, discount):
    discount_value = (price * discount) / 100
    discounted_price = price - discount_value
    print(round(discounted_price, 2))

dis(100, 75)
dis(211, 50)
dis(593, 61)
dis(1693, 80)
dis(700, 10)

'''
dis(100, 75), 25
dis(211, 50), 105.5
dis(593, 61), 231.27
dis(1693, 80), 338.6
dis(700, 10), 630
'''