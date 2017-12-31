from edge import *

class Room:
    def __init__(self, points):
        self.points = points
        self.validate()

    def validate(self):
        """
        A room is considered valid if all edges are horizontal and vertical lines
        """
        for edge in self.get_edges():
            if not edge.is_vertical() and not edge.is_horizontal():
                raise RuntimeError("Room invalid")

    def get_edges(self):
        edges = []
        for index in range(0, len(self.points) - 1):
            edges.append(Edge(self.points[index], self.points[index + 1]))
        edges.append(Edge(self.points[-1], self.points[0]))
        return edges

    # def intersects(self, other):
    #     """ Return whether this room intersects with other """

    # def inside(self, point):
    #     # check for line above
    #     for edge in self.get_edges():
    #
    #     # check for line below
    #     # check for line left
    #     # check for line right

