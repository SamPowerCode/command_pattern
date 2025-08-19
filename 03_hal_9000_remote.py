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
        print(f"The {self.location} light is now ON.")

    def turn_off(self):
        self.level = 0
        print(f"The {self.location} light is now OFF.")


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
class HAL9000Remote:
    def __init__(self):
        self.on_commands = [no_command for _ in range(7)]
        self.off_commands = [no_command for _ in range(7)]
        self.undo_command = no_command

    def set_command(self, index, on_command, off_command):
        self.on_commands[index] = on_command
        self.off_commands[index] = off_command

    def press_on_button(self, index):
        self.on_commands[index]()

    def press_off_button(self, index):
        self.off_commands[index]()

    def __str__(self) -> str:
        buffer = ["\n------ Remote Control -------\n"]
        for i, (on_command, off_command) in enumerate(
                zip(self.on_commands, self.off_commands)
        ):
            buffer.append(
                f"[slot {i}] {on_command.__name__}"
                + f"    {off_command.__name__}\n"
            )
        return "".join(buffer)

if __name__ == "__main__":
    # client
    light_kitchen = Light('Kitchen')
    light_front_door = Light('Front door')
    light_back_door = Light('Back door')
    remote = HAL9000Remote()
    print(remote)

    # Set the command using a function
    remote.set_command(
        0,
        lambda: command_light_turn_on(light_kitchen),
        lambda: command_light_turn_off(light_kitchen)
    )
    remote.set_command(
        1,
        lambda: command_light_turn_on(light_front_door),
        lambda: command_light_turn_off(light_front_door)
    )
    remote.set_command(
        2,
        lambda: command_light_turn_on(light_back_door),
        lambda: command_light_turn_off(light_back_door)
    )
    print(remote)
    remote.press_on_button(0)
    remote.press_off_button(0)
    remote.press_on_button(1)
    remote.press_off_button(1)
    remote.press_on_button(2)
    remote.press_off_button(2)
