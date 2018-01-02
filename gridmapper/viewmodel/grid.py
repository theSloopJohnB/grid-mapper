from ..model.house import House
from ..model.point import Point

class Grid():
    def __init__(self):
        self.house = House()

    @property
    def rows_pos(self):
        return sorted(set([edge.start.y for edge in self.house.edges if edge.is_horizontal()]))

    @property
    def columns_pos(self):
        return sorted(set([edge.start.x for edge in self.house.edges if edge.is_vertical()]))

    @property
    def column_widths(self):
        cols = self.columns_pos
        return [leading - trailing for leading, trailing in zip(cols[1:], cols[:-1])]

    @property
    def rows_widths(self):
        rows = self.rows_pos
        return [leading - trailing for leading, trailing in zip(rows[1:], rows[:-1])]

    def add_room(self, room):
        self.house.add_room(room)

    def logical_repr(self):
        grid = []
        for row in self.rows_pos:
            grid_row = []
            for col in self.columns_pos:
                grid_row.append(self.house.room_at_point(Point(col, row)))

            grid.append(grid_row)
        return grid
