import time
import keyboard


class Flote:
    def __init__(self, key, loc, button):
        self.key = key
        self.height = 1000
        self.loc = loc
        self.button = button

    def increment(self):
        self.height += 1
        time.sleep(0.005)

    def seeScore(self):
        if (keyboard.is_pressed(self.key) & 500 < self.height & self.height < 550):
            return True
        else:
            return False

    def setHeight(self, height):
        self.height = height

    def setLoc(self, loc):
        self.loc = loc

    def setButton(self, button):
        self.button = button

    def getPress(ky):
        return {'T': '\t', 'q': 'q', 'w': 'w', 'e': 'e', 'r': 'r', 't': 't', 'y': 'y', 'u': 'u', 'i': 'i',
                'o': 'o', 'p': 'p', 'L': '[', 'R': ']', 'S': '\\', 'a': '1', 's': '2', 'd': '4', 'f': '5', 'g': '6',
                'h': '8', 'j': '9', 'k': '-', 'l': '=', 'z': '\b', ' ': 'N'}[ky]

    def getPos(ky):
        return {'T': 1, 'q': 2, 'w': 3, 'e': 4, 'r': 5, 't': 6, 'y': 7, 'u': 8, 'i': 9,
                'o': 10, 'p': 11, 'L': 12, 'R': 13, 'S': 14, 'a': 15, 's': 16, 'd': 18, 'f': 19, 'g': 20, 'h': 22,
                'j': 23, 'k': 25, 'l': 26, 'z': 27, ' ': 0}[ky]