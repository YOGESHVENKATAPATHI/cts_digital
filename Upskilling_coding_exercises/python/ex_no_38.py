class Staff:
    def __init__(self):
        self.salary = 0

    def set_salary(self, salary):
        self.salary = salary
        return self

    def increase(self, percent):
        self.salary += self.salary * percent / 100
        return self

    def show(self):
        print(self.salary)

Staff().set_salary(50000).increase(10).show()
