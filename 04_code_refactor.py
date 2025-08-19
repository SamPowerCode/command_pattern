#  _________________
# |    HAL 9000     |
#  _________________
# |  ON   OFF  | 01 |
# |  ON   OFF  | 02 |
# |  ON   OFF  | 03 |
# |  ON   OFF  | 04 |
# |  ON   OFF  | 05 |
# |  ON   OFF  | 06 |
# |  ON   OFF  | 07 |
# |_________________|
# |      [UNDO]     |
# |_________________|
#

# command
def no_command():
    pass


def command_light_turn_on(light_obj):
    light_obj.turn_on()


def command_light_turn_off(light_obj):
    light_obj.turn_off()


def command_stereo_turn_on(stereo_obj):
    stereo_obj.turn_on()


def command_stereo_turn_off(stereo_obj):
    stereo_obj.turn_off()


def command_stereo_volume(stereo_obj):
    stereo_obj.turn_off()


# receivers
class Light:
    def __init__(self, location: str):
        self.location = location
        self.level = 0

    def turn_on(self):
        self.level = 100
        print("The Light is now ON.")

    def turn_off(self):
        self.level = 0
        print("The Light is now OFF.")


class Stereo:
    def __init__(self):
        self.state = "OFF"
        self.volume = 0

    def turn_on(self):
        self.state = "ON"
        print(f"The Stereo is now {self.state}.")

    def turn_off(self):
        self.state = "OFF"
        print(f"The Stereo is now {self.state}.")

    def set_volume(self, volume):
        self.volume = 11


# invoker
class SimpleRemote2:
    def __init__(self):
        self.on_command = no_command
        self.off_command = no_command

    def set_command(self, on_command, off_command):
        self.on_command = on_command
        self.off_command = off_command

    def press_on_button(self):
        if self.on_command:
            self.on_command()

    def press_off_button(self):
        if self.off_command:
            self.off_command()


if __name__ == "__main__":
    # client
    light = Light('Kitchen')
    remote = SimpleRemote2()

    # Set the command using a function
    remote.set_command(lambda: command_light_turn_on(light), lambda: command_light_turn_off(light))
    remote.press_on_button()
    remote.press_off_button()
