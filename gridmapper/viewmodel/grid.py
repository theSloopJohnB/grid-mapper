from ..model.house import House

class Grid():
    def __init__(self):
        self.house = House()

    @property
    def rows(self):
        return sorted(set([edge.start.y for edge in self.house.edges if edge.is_horizontal()]))

    @property
    def columns(self):
        return sorted(set([edge.start.x for edge in self.house.edges if edge.is_vertical()]))

    def add_room(self, room):
        self.house.add_room(room)

