class Bulb:
    def power_on(self):
        print("Light ON")

    def power_off(self):
        print("Light OFF")


class BulbOnAction:
    def __init__(self, bulb):
        self.bulb = bulb

    def trigger(self):
        self.bulb.power_on()


class BulbOffAction:
    def __init__(self, bulb):
        self.bulb = bulb

    def trigger(self):
        self.bulb.power_off()


class Controller:
    def assign_action(self, action):
        self.action = action

    def click_button(self):
        self.action.trigger()


if __name__ == "__main__":
    my_bulb = Bulb()
    my_controller = Controller()
    
    my_controller.assign_action(BulbOnAction(my_bulb))
    my_controller.click_button()
    
    my_controller.assign_action(BulbOffAction(my_bulb))
    my_controller.click_button()