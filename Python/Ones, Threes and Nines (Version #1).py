# https://edabit.com/challenge/X6xZ2EaqqQbGF7Bwv

class ones_threes_nines:
    def __init__(self, n):
        self.ones = n
        self.threes = n // 3
        self.nines = n // 9



n1 = ones_threes_nines(123)
print(n1.ones)
print(n1.threes)
print(n1.nines)