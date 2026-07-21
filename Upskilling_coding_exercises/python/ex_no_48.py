class Item:
    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty

class Cart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def total(self):
        return sum(i.price * i.qty for i in self.items)

c = Cart()
c.add(Item("Laptop", 50000, 1))
print(c.total())
