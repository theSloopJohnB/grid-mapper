from rectangle import *

class Room:
    def __init__(self):
        self.rectangles = []

    def add_rectangle(self, new_rect):
        if not self.can_add_rectangle(new_rect):
            raise RuntimeError("Rectangles must not intersect and must conjoin pre-existing rectangles")

        self.rectangles.append(new_rect)

    def can_add_rectangle(self, new_rect):
        if len(self.rectangles) == 0:
            return True

        conjoined = False
        for rect in self.rectangles:
            if rect.intersects(new_rect):
                return False
            if rect.conjoins(new_rect):
                conjoined = True

        return conjoined

    # def is_conjoined(self, other):
    #     conjoined = False
    #     for rect in self.rectangles:
    #         for other_rect in other.rectangles:
    #             if rect.conjoins(other_rect):
    #                 return false
