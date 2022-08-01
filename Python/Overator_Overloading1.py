class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __mul__(self, other):
        return self.salary * other.days

class TimeSheet:
    def __int__(self, name, days):
        self.name = name
        self.days = days

e = Employee('vivek', 500)
t = TimeSheet('vivek', 25)
print('This month salary:', e*t)
