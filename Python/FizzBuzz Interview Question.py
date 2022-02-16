# https://edabit.com/challenge/WXqH9qvvGkmx4dMvp

def fizz_buzz(num):
    pop = "FizzBuzz"
    if num % 3 == 0 and num % 5 == 0:
        return pop
    elif num % 3 == 0:
        return pop[:4]
    elif num % 5 == 0:
        return pop[4:]
    else:
        return str(num)

print(fizz_buzz(3))
print(fizz_buzz(5))
print(fizz_buzz(15))
print(fizz_buzz(4))

'''
fizz_buzz(3) ➞ "Fizz"
fizz_buzz(5) ➞ "Buzz"
fizz_buzz(15) ➞ "FizzBuzz"
fizz_buzz(4) ➞ "4"
'''