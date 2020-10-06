from random import randint


class Sai():
    def __init__(self, face=6):
        self.face = face

    def pao(self):
        return randint(1, self.face)
