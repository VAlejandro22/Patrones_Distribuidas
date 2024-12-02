# PATRON COMMAND
# Command Interface
class Command:
    def execute(self):
        pass

# Concrete Command: Encender luces
class TurnOnLightCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        return self.light.turn_on()

# Concrete Command: Apagar luces
class TurnOffLightCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        return self.light.turn_off()

# Receiver
class Light:
    def turn_on(self):
        return "Luz encendida"

    def turn_off(self):
        return "Luz apagada"

# Invoker
class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        return self.command.execute()

# Uso COMMAND
light = Light()
turn_on = TurnOnLightCommand(light)
turn_off = TurnOffLightCommand(light)

remote = RemoteControl()
remote.set_command(turn_on)
print(remote.press_button())  # Output: Luz encendida

remote.set_command(turn_off)
print(remote.press_button())  # Output: Luz apagada