import keyboard


class Key:
    def __init__(self, key, location, name, sound):
        self.key = key
        self.location = location
        self.name = name
        self.sound = sound

    def struck(self):
        if keyboard.is_pressed(self.key):
            return True
        else:
            return False
