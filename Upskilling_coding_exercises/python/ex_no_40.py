class Member:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def create(cls, data):
        n, s = data.split(",")
        return cls(n, int(s))

m = Member.create("Shubh,75000")
print(m.name, m.salary)
