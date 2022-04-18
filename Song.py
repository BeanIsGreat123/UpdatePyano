from Flote import *
from Enums import *


class Song:

    def __init__(self, sheet):
        self.sheet = sheet

    def compose(self):
        composition = []
        for element in self.sheet:
            pos = Flote.getPos(element)
            ky = Flote.getPress(element)
            insert = Flote(element, pos, ky)
            composition.append(insert)
        composition[0].setHeight(0)
        return composition
