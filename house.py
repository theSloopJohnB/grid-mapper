import itertools

from room import *


class House:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)
        self.validate()

    def validate(self):
        for room1, room2 in itertools.combinations(self.rooms, 2):
            if room1.is_intersection(room2):
                raise RuntimeError("House invalid: No rooms can share space")
