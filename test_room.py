from nose.tools import *
from room import *


def valid_room_test():
    room1_points = [
                Point(0, 0),
                Point(50, 0),
                Point(50, 50),
                Point(0, 50),
            ]
    room1 = Room(room1_points)
    pass


@raises(RuntimeError)
def invalid_room_test():
    room1_points = [
                Point(0, 0),
                Point(50, 0),
                Point(50, 50),
            ]
    room1 = Room(room1_points)

def edge_test_1():
    room1_points = [
        Point(0, 0),
        Point(50, 0),
        Point(50, 50),
        Point(0, 50),
    ]
    room1 = Room(room1_points)
    edges = room1.get_edges()

    expected = [
        Edge(Point(0,0), Point(50,0)),
        Edge(Point(50,0), Point(50,50)),
        Edge(Point(50,50), Point(0,50)),
        Edge(Point(0,50), Point(0,0))
    ]
    assert len(edges) == len(expected)
    assert edges == expected


