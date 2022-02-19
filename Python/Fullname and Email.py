# https://edabit.com/challenge/gB7nt6WzZy8TymCah

class Employee():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def email(self):
        return "{}.{}@company.com".format(self.first_name, self.last_name.lower())


emp1 = Employee("John", "Smith")
print(emp1.fullname())
print(emp1.email())

emp2 = Employee("Mary", "Sue")
print(emp2.fullname())
print(emp2.email())
