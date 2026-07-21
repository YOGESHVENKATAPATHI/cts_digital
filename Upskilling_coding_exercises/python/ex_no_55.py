class Budget:
    def __init__(self, limit):
        self.limit = limit
        self.spent = 0

    def add(self, amount):
        self.spent += amount

b = Budget(5000)
b.add(3500)
b.add(2000)
print(b.spent)
