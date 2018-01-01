import itertools

from gridmapper.model.edge import *

class Rectangle:
    def __init__(self, points):
        self.points = points
        self._validate()

    def __repr__(self):
        return 'Rectangle({})'.format(repr(self.points))

    def __eq__(self, other):
        point_tracker = {point: False for point in self.points}
        for point in other.points:
            point_tracker[point] = True

        # If all true, rectangles must be the same
        return not False in point_tracker.values()


    def _validate(self):
        """
        A room is considered valid if
        1. Rooms are rectangles
        1. all edges are horizontal and vertical lines
        2. lines don't occupy the same space
        3. TODO: Add criteria to check for intersections - should not be allowed
        """
        if len(self.points) != 4:
            raise RuntimeError("Rectangles only")

        # TODO: Add some more rectangle validation

        for edge in self.edges:
            if not edge.is_vertical() and not edge.is_horizontal():
                raise RuntimeError("Room invalid: All edges must be horizontal or vertical")

        for edge1, edge2 in itertools.combinations(self.edges, 2):
            if edge1.shares_space(edge2):
                raise RuntimeError("Room invalid: No edges can share space")

    @property
    def edges(self):
        edges = []
        for index in range(0, len(self.points) - 1):
            edges.append(Edge(self.points[index], self.points[index + 1]))
        edges.append(Edge(self.points[-1], self.points[0]))
        return edges

    def intersects(self, other):
        """ Return whether this rectangle intersects with other. Overlap counts as intersects """
        my_points = {point: False for point in self.points}
        for point in other.points:
            my_points[point] = True

        if False not in my_points.values():
            return True

        for edge in other.edges:
            for point in edge.get_points():
                if self.inside(point):
                    return True

        return False

    def conjoins(self, other):
        """ Whether this and another rectangle share any sides. Corners don't count """
        if self.intersects(other):
            return False

        for edge_self in self.edges:
            for edge_other in other.edges:
                if edge_self.shares_space(edge_other):
                    return True

        return False

    def inside(self, point, include_edges=False):
        """
        Returns whether point is inside of this rectangle.
        """
        # check for line above
        side_checker = {
           'above': 0,
           'below': 0,
           'left': 0,
           'right': 0,
        }

        edges = self.edges
        for edge in edges:
            if edge.is_inside(point):
                return include_edges
            elif edge.is_above(point):
                side_checker['above'] += 1
            elif edge.is_below(point):
                side_checker['below'] += 1
            elif edge.is_left(point):
                side_checker['left'] += 1
            elif edge.is_right(point):
                side_checker['right'] += 1

        for val in side_checker.values():
            if val != 1:
                return False

        return True
