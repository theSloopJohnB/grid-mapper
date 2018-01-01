import itertools

from gridmapper.model.room import *


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

    @property
    def rectangles(self):
        rects = []
        for room in self.rooms:
            for rect in room.rectangles:
                rects.append(rect)
        return rects

    @property
    def edges(self):
        edges = []
        for rect in self.rectangles:
            for edge in rect.edges:
                edges.append(edge)

        return edges

    def room_at_point(self, point):
        for i in range(0, len(self.rooms)):
            if self.rooms[i].contains_point(point):
                return i

        return -1
