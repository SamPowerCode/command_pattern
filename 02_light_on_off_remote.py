# Receiver
class Light:
    def turn_on(self):
        print("The light is on.")

    def turn_off(self):
        print("The light is off.")

# Functional Commands
def light_on_command(light_obj):
    return lambda: light_obj.turn_on()

def light_off_command(light_obj):
    return lambda: light_obj.turn_off()

# Invoker with undo functionality
class SimpleRemoteControl:
    def __init__(self):
        self.slot = None
        self.last_command = None

    def set_command(self, command_pair):
        self.slot = command_pair

    def button_was_pressed(self):
        if self.slot and 'execute' in self.slot:
            self.slot['execute']()
            self.last_command = self.slot

    def undo_button_was_pressed(self):
        if self.last_command and 'undo' in self.last_command:
            self.last_command['undo']()

# Client Code
light = Light()

# Create command pairs with execute and undo functions
light_on_pair = {'execute': light_on_command(light), 'undo': light_off_command(light)}
light_off_pair = {'execute': light_off_command(light), 'undo': light_on_command(light)}

remote = SimpleRemoteControl()

# Turn the light on
remote.set_command(light_on_pair)
remote.button_was_pressed()  # Output: The light is on.

# Undo the last action (turn the light off)
remote.undo_button_was_pressed()  # Output: The light is off.

# Turn the light off
remote.set_command(light_off_pair)
remote.button_was_pressed()  # Output: The light is off.

# Undo the last action (turn the light on)
remote.undo_button_was_pressed()  # Output: The light is on.

# # command
# def command_light_turn_on(light_obj):
#     light_obj.turn_on()
#
#
# def command_light_turn_off(light_obj):
#     light_obj.turn_off()
#
#
# # receiver
# class Light:
#     def __init__(self, location: str):
#         self.location = location
#         self.level = 0
#
#     def turn_on(self):
#         self.level = 100
#         print("The Light is now ON.")
#
#     def turn_off(self):
#         self.level = 0
#         print("The Light is now OFF.")
#
#
# # invoker
# class SimpleRemote2:
#     def __init__(self):
#         self.on_command = None
#         self.off_command = None
#
#     def set_command(self, on_command, off_command):
#         self.on_command = on_command
#         self.off_command = off_command
#
#     def press_on_button(self):
#         if self.on_command:
#             self.on_command()
#
#     def press_off_button(self):
#         if self.off_command:
#             self.off_command()
#
#
# if __name__ == "__main__":
#     # client
#     light = Light('Kitchen')
#     remote = SimpleRemote2()
#
#     # Set the command using a function
#     remote.set_command(lambda: command_light_turn_on(light), lambda: command_light_turn_off(light))
#     remote.press_on_button()
#     remote.press_off_button()
