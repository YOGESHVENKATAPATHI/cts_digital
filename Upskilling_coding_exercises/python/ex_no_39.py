class Worker:
    def work(self):
        pass

class Developer(Worker):
    def work(self):
        print("Coding")

class Manager(Worker):
    def work(self):
        print("Managing")

for obj in [Developer(), Manager()]:
    obj.work()
