from nose.tools import *

from edge import *


def vertical_edge_test():
    edges = [Edge(Point(0,0), Point(0, 50)),
             Edge(Point(0,50), Point(0, 0))]
    for edge in edges:
        assert not edge.is_horizontal()
        assert edge.is_vertical()


def horizontal_edge_test():
    edges = [
        Edge(Point(0,0), Point(50, 0)),
        Edge(Point(50,0), Point(0, 0))
        ]
    for edge in edges:
        assert edge.is_horizontal()
        assert not edge.is_vertical()


def is_between_x_test():
    edges = [
        Edge(Point(0,0), Point(50, 0)),
        Edge(Point(50,0), Point(0, 0))
         ]
    for edge in edges:
        assert edge.is_between_x(Point(25,0))
        assert not edge.is_between_x(Point(125,0))


def is_between_y_test():
    edges = [
        Edge(Point(0,0), Point(0, 50)),
        Edge(Point(0,50), Point(0, 0))
    ]
    for edge in edges:
        assert edge.is_between_y(Point(0,25))
        assert not edge.is_between_y(Point(0,125))


def is_above_test():
    edges = [
            Edge(Point(50,0), Point(0, 0)),
            Edge(Point(0,0), Point(50, 0))
        ]
    for edge in edges:
        assert edge.is_above(Point(0,25))
        assert not edge.is_above(Point(0,-25))
        assert not edge.is_above(Point(125,25))
        assert not edge.is_above(Point(-125,25))

    vert_edges = [
        Edge(Point(0,0), Point(0, 50)),
        Edge(Point(0,50), Point(0, 0))
    ]
    for edge in vert_edges:
        assert not edge.is_above(Point(25,25))
        assert not edge.is_above(Point(0,-25))
        assert not edge.is_above(Point(125,25))
        assert not edge.is_above(Point(-125,25))

def is_below_test():
    edges = [
        Edge(Point(50,0), Point(0, 0)),
        Edge(Point(0,0), Point(50, 0))
    ]
    for edge in edges:
        assert edge.is_below(Point(0,-25))
        assert not edge.is_below(Point(0,25))
        assert not edge.is_below(Point(125,-25))
        assert not edge.is_below(Point(-125,-25))

    vert_edges = [
        Edge(Point(0,0), Point(0, 50)),
        Edge(Point(0,50), Point(0, 0))
    ]
    for edge in vert_edges:
        assert not edge.is_below(Point(25,-25))
        assert not edge.is_below(Point(0,-25))
        assert not edge.is_below(Point(125,-25))
        assert not edge.is_below(Point(-125,-25))


def is_left_test():
    edges = [
        Edge(Point(0,0), Point(0, 50)),
        Edge(Point(0,50), Point(0, 0))
    ]
    for edge in edges:
        assert edge.is_left(Point(25,25))
        assert edge.is_left(Point(25,0))
        assert not edge.is_left(Point(0,25))
        assert not edge.is_left(Point(-25,25))
        assert not edge.is_left(Point(25,-25))

    horiz_edges = [
        Edge(Point(50,0), Point(0, 0)),
        Edge(Point(0,0), Point(50, 0))
    ]
    for edge in horiz_edges:
        assert not edge.is_left(Point(25,25))
        assert not edge.is_left(Point(0,25))
        assert not edge.is_left(Point(-25,25))
        assert not edge.is_left(Point(-125,-25))


def is_right_test():
    edges = [
        Edge(Point(0,0), Point(0, 50)),
        Edge(Point(0,50), Point(0, 0))
    ]
    for edge in edges:
        assert edge.is_right(Point(-25,25))
        assert edge.is_right(Point(-25,0))
        assert not edge.is_right(Point(0,25))
        assert not edge.is_right(Point(25,25))
        assert not edge.is_right(Point(-25,-25))

    horiz_edges = [
        Edge(Point(50,0), Point(0, 0)),
        Edge(Point(0,0), Point(50, 0))
    ]
    for edge in horiz_edges:
        assert not edge.is_right(Point(-25,25))
        assert not edge.is_right(Point(-25,0))
        assert not edge.is_right(Point(0,25))
        assert not edge.is_right(Point(-125,-25))
