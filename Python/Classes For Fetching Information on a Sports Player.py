# https://edabit.com/challenge/pa65DgwG5HMbtf6iY

class Player:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    # used different methods of string manipulation

    def get_age(self):
        return self.name + "is age " + str(self.age)

    def get_height(self):
        return f"{self.name} is {self.height} cm"

    def get_weight(self):
        return "{} weighs {} kg".format(self.name, self.weight)


p1 = Player("David Jones", 25, 175, 75)
print(p1.get_age())
print(p1.get_height())
print(p1.get_weight())

p2 = Player('Patrick Mahomes', 24, 188, 104)
p3 = Player('Jimmy Garoppolo', 28, 188, 102)
p4 = Player('Julio Jones', 31, 191, 100)

print(p2.get_age())  # Patrick Mahomesis age 24
print(p2.get_height())  # Patrick Mahomes is 188 cm
print(p2.get_weight())  # Patrick Mahomes weighs 104 kg

print(p3.get_age())  # Jimmy Garoppolois age 28
print(p3.get_height())  # Jimmy Garoppolo is 188 cm
print(p3.get_weight())  # Jimmy Garoppolo weighs 102 kg

print(p4.get_age())  # Julio Jonesis age 31
print(p4.get_height())  # Julio Jones is 191 cm
print(p4.get_weight())  # Julio Jones weighs 100 kg

'''

'''
