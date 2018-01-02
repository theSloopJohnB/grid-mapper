from ..viewmodel.grid import Grid
from mako.template import Template

class GridView:
    def __init__(self, grid):
        self.grid = grid

    def render(self):
        data = {
            'grid_start_left': self.grid.columns_pos[0],
            'grid_start_top': self.grid.rows_pos[0],
            'rows_width': self.grid.rows_widths,
            'columns_width': self.grid.column_widths,
            'cells': [cell for sublist in self.grid.logical_repr() for cell in sublist],
        }
        return Template(filename="templates/playground.mako.html").render(data=data)
