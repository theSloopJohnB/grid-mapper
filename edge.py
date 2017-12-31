from point import *

class Edge:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return 'Edge({}, {})'.format(repr(self.start), repr(self.end))

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

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
        """ If the edge is to the left of the point"""
        return self.is_vertical() and self.is_between_y(point) and self.start.x < point.x

    def is_right(self, point):
        """ If the edge is to the right of the point"""
        return self.is_vertical() and self.is_between_y(point) and self.start.x > point.x


