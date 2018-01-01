from point import *

class Edge:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return 'Edge({}, {})'.format(repr(self.start), repr(self.end))

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

    def get_points(self):
        if self.is_vertical():
            higher = max(self.start.y, self.end.y)
            lower = min(self.start.y, self.end.y)
            return [Point(self.start.x, y) for y in range(lower, higher + 1)]

        higher = max(self.start.x, self.end.x)
        lower = min(self.start.x, self.end.x)
        return [Point(x, self.start.y) for x in range(lower, higher + 1)]

    def is_vertical(self):
        return self.start.x == self.end.x

    def is_horizontal(self):
        return self.start.y == self.end.y

    def is_between_x(self, point):
        """ Return whether point lies between the x coordinates of the edge. """
        return (self.start.x >= point.x >= self.end.x or
                self.end.x >= point.x >= self.start.x)

    def is_between_y(self, point):
        """ Return whether point lies between the y coordinates of the edge. """
        return (self.start.y >= point.y >= self.end.y or
                self.end.y >= point.y >= self.start.y)

    def is_above(self, point):
        """ If the edge is above the point"""
        return self.is_horizontal() and self.is_between_x(point) and self.start.y < point.y

    def is_below(self, point):
        """ If the edge is below the point"""
        return self.is_horizontal() and self.is_between_x(point) and self.start.y > point.y

    def is_left(self, point):
        """ If the edge is to the left of the point """
        return self.is_vertical() and self.is_between_y(point) and self.start.x < point.x

    def is_right(self, point):
        """ If the edge is to the right of the point """
        return self.is_vertical() and self.is_between_y(point) and self.start.x > point.x

    def is_inside(self, point):
        """ If the point is somewhere on the line """
        return self.is_between_x(point) and self.is_between_y(point)

    def shares_horiz_bounds(self, point):
        return self.is_horizontal() and (point.x == self.start.x or point.x == self.end.x)

    def shares_vert_bounds(self, point):
        return self.is_vertical() and (point.y == self.start.y or point.y == self.end.y)

    def shares_space(self, other):
        """ Whether this and other share space. Assumes horizontal and vertical lines only """
        if self.is_vertical():
            if not other.is_vertical():
                return False

            if self.start.x != other.start.x:
                return False

            # All Ys are below or above all of other's Ys
            return not ((self.start.y >= other.start.y and
                    self.start.y >= other.end.y and
                    self.end.y >= other.start.y and
                    self.end.y >= other.end.y)
                    or
                    (self.start.y <= other.start.y and
                    self.start.y <= other.end.y and
                    self.end.y <= other.start.y and
                    self.end.y <= other.end.y))

        if self.is_horizontal():
            if not other.is_horizontal():
                return False

            if self.start.y != other.start.y:
                return False

            # All Xs are below or above all of other's Ys
            return not ((self.start.x >= other.start.x and
                     self.start.x >= other.end.x and
                     self.end.x >= other.start.x and
                     self.end.x >= other.end.x)
                    or
                    (self.start.x <= other.start.x and
                     self.start.x <= other.end.x and
                     self.end.x <= other.start.x and
                     self.end.x <= other.end.x))
        return False
