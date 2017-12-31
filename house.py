class House:
    def __init__(self):
        self.rooms = []

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
        

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point({}, {})'.format(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

