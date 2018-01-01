from ..model.house import House
from ..model.point import Point

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

    def logical_repr(self):
        grid = []
        for row in self.rows:
            grid_row = []
            for col in self.columns:
                grid_row.append(self.house.room_at_point(Point(col, row)))

            grid.append(grid_row)
        return grid
