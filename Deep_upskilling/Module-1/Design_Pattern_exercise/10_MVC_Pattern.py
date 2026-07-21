class Learner:
    def __init__(self, l_id, fullname, score):
        self.l_id = l_id
        self.fullname = fullname
        self.score = score


class LearnerInterface:
    def render_learner(self, learner):
        print("Student ID:", learner.l_id)
        print("Name:", learner.fullname)
        print("Grade:", learner.score)


class LearnerManager:
    def __init__(self, learner, interface):
        self.learner = learner
        self.interface = interface

    def modify_fullname(self, new_fullname):
        self.learner.fullname = new_fullname

    def display_info(self):
        self.interface.render_learner(self.learner)


if __name__ == "__main__":
    my_learner = Learner(101, "Madhi", "A")
    my_interface = LearnerInterface()
    manager = LearnerManager(my_learner, my_interface)
    
    manager.display_info()
    manager.modify_fullname("Ganesh S")
    
    print("\nAfter Update\n")
    manager.display_info()