# https://edabit.com/challenge/ta8GBizBNbRGo5iC6

class Calculator:
    def add(self, n1, n2):
        return n1 + n2

    def subtract(self, n1, n2):
        return n1 - n2

    def multiply(self, n1, n2):
        return n1 * n2

    def divide(self, n1, n2):
        return n1 // n2


calculator = Calculator()
print(calculator.add(10, 5))
print(calculator.subtract(10, 5))
print(calculator.multiply(10, 5))
print(calculator.divide(10, 5))


'''
calculator.add(5,5), 10, "5 + 5 = 10")
calculator.add(20,5), 25, "20 + 5 = 25")
calculator.subtract(30,5), 25, "30 - 5 = 25")
calculator.subtract(100,5), 95, "100 - 5 = 95")
calculator.multiply(5,5), 25, "5 * 5 = 25")
calculator.multiply(100,5), 500, "100 * 5 = 500")
calculator.divide(10,5), 2, "10 / 5 = 2")
calculator.divide(100,5), 20, "100 / 5 = 20")

'''