# https://edabit.com/challenge/YfoKQWNeYETb9PYpw

def profit(d):
    profit_per_item = d["sell_price"] - d["cost_price"]
    total_value = profit_per_item * d['inventory']
    return round(total_value)


print(profit({"cost_price": 32.67,"sell_price": 45.00,"inventory": 1200}))
print(profit({'cost_price': 0.1, 'sell_price': 0.18, 'inventory': 259800}))
print(profit({'cost_price': 185.00, 'sell_price': 299.99, 'inventory': 300}))
print(profit({'cost_price': 378.11, 'sell_price': 990.00, 'inventory': 99}))
print(profit({'cost_price': 4.67, 'sell_price': 5.00, 'inventory': 78000}))

'''
profit({'cost_price': 32.67, 'sell_price': 45.00, 'inventory': 1200}), 14796)
profit({'cost_price': 0.1, 'sell_price': 0.18, 'inventory': 259800}), 20784)
profit({'cost_price': 185.00, 'sell_price': 299.99, 'inventory': 300}), 34497)
profit({'cost_price': 378.11, 'sell_price': 990.00, 'inventory': 99}), 60577)
profit({'cost_price': 4.67, 'sell_price': 5.00, 'inventory': 78000}), 25740)
profit({'cost_price': 19.87, 'sell_price': 110.00, 'inventory': 350}), 31546)
profit({'cost_price': 2.91, 'sell_price': 4.50, 'inventory': 6000}), 9540)
profit({'cost_price': 68.01, 'sell_price': 149.99, 'inventory': 500}), 40990)
profit({'cost_price': 1.45, 'sell_price': 8.50, 'inventory': 10000}), 70500)
profit({'cost_price': 10780, 'sell_price': 34999, 'inventory': 10}), 242190)
'''