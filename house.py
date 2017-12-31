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
            if not edge.is_vertical() or not edge.is_horizontal():
                raise RuntimeException("Room invalid")
        print ('valid')

    def get_edges(self):
        edges = []
        for index in range(0, len(self.points) - 1):
            edges.append(Edge(self.points[index], self.points[index + 1]))
        edges.append(Edge(self.points[0], self.points[-1]))
        return edges


class Edge:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def is_vertical(self):
        return self.start.x == self.start.x
        
    def is_horizontal(self):
        return self.start.y == self.start.y
        

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
