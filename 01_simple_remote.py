# command
def command_light_turn_on(light_obj):
    light_obj.turn_on()

# receiver
class Light:
    def turn_on(self):
        print("The TV is now ON.")

# invoker
class SimpleRemote:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        if self.command:
            self.command()

if __name__ == "__main__":
    # client
    light = Light()
    remote = SimpleRemote()

    # Set the command using a function
    remote.set_command(lambda: command_light_turn_on(light))
    remote.press_button()
