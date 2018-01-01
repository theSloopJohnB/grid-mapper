from nose.tools import *

from gridmapper.model.edge import *


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


def shares_space_test():
    edge1 = Edge(Point(0, 0), Point(0, 50))

    # Same vertical line
    assert edge1.shares_space(Edge(Point(0, 50), Point(0, 0)))
    # Sharing a point
    assert not edge1.shares_space(Edge(Point(0, 50), Point(0, 100)))
    # Sharing nothing
    assert not edge1.shares_space(Edge(Point(0, 51), Point(0, 100)))
    # Overlapping some
    assert edge1.shares_space(Edge(Point(0, 49), Point(0, 100)))
    # Parallel, non overlapping
    assert not edge1.shares_space(Edge(Point(1, 0), Point(1, 50)))
    # Crossing with horizontal line
    assert not edge1.shares_space(Edge(Point(0, 0), Point(50, 0)))

    edge2 = Edge(Point(0, 0), Point(50, 0))

    # Same vertical line
    assert edge2.shares_space(Edge(Point(50, 0), Point(0, 0)))
    # Sharing a point
    assert not edge2.shares_space(Edge(Point(50, 0), Point(100, 0)))
    # Sharing nothing
    assert not edge2.shares_space(Edge(Point(51, 0), Point(100, 0)))
    # Overlapping some
    assert edge2.shares_space(Edge(Point(49, 0), Point(100, 0)))
    # Parallel, non overlapping
    assert not edge2.shares_space(Edge(Point(0, 1), Point(50, 1)))
    # Crossing with vertical line
    assert not edge2.shares_space(Edge(Point(0, 0), Point(0, 50)))

def is_inside_test():
    edge1 = Edge(Point(0, 0), Point(0, 50))

    # Vertical Line
    assert edge1.is_inside(Point(0, 0))
    assert edge1.is_inside(Point(0, 25))
    assert edge1.is_inside(Point(0, 50))
    assert not edge1.is_inside(Point(0, 51))
    assert not edge1.is_inside(Point(0, -1))
    assert not edge1.is_inside(Point(1, 0))
    assert not edge1.is_inside(Point(-1, 25))
    assert not edge1.is_inside(Point(2, 50))

    edge2 = Edge(Point(0, 0), Point(50, 0))

    # Horizontal Line
    assert edge2.is_inside(Point(0, 0))
    assert edge2.is_inside(Point(25, 0))
    assert edge2.is_inside(Point(50, 0))
    assert not edge2.is_inside(Point(51, 0))
    assert not edge2.is_inside(Point(-1, 0))
    assert not edge2.is_inside(Point(0, 1))
    assert not edge2.is_inside(Point(25, -1))
    assert not edge2.is_inside(Point(50, 1))

def get_points_test():
    edge1 = Edge(Point(0, 0), Point(0, 2))
    edge1_points = edge1.get_points()
    expected1 = [
        Point(0, 0),
        Point(0, 1),
        Point(0, 2),
    ]
    assert edge1_points == expected1

    edge2 = Edge(Point(0, 0), Point(2, 0))
    edge2_points = edge2.get_points()
    expected2 = [
        Point(0, 0),
        Point(1, 0),
        Point(2, 0),
    ]
    assert edge2_points == expected2

def shares_horiz_bounds_test():
    edge1 = Edge(Point(0, 0), Point(2, 0))

    assert edge1.shares_horiz_bounds(Point(0, 1))
    assert edge1.shares_horiz_bounds(Point(0, -1))
    assert edge1.shares_horiz_bounds(Point(0, 0))
    assert edge1.shares_horiz_bounds(Point(2, 1))
    assert edge1.shares_horiz_bounds(Point(2, -1))
    assert edge1.shares_horiz_bounds(Point(2, 0))

    assert not edge1.shares_horiz_bounds(Point(3, 0))
    assert not edge1.shares_horiz_bounds(Point(3, 1))
    assert not edge1.shares_horiz_bounds(Point(3, -1))
    assert not edge1.shares_horiz_bounds(Point(1, 0))
    assert not edge1.shares_horiz_bounds(Point(1, 1))
    assert not edge1.shares_horiz_bounds(Point(1, -1))

def shares_vert_bounds_test():
    edge1 = Edge(Point(0, 0), Point(0, 2))

    assert edge1.shares_vert_bounds(Point(1, 0))
    assert edge1.shares_vert_bounds(Point(-1, 0))
    assert edge1.shares_vert_bounds(Point(0, 0))
    assert edge1.shares_vert_bounds(Point(1, 2))
    assert edge1.shares_vert_bounds(Point(-1, 2))
    assert edge1.shares_vert_bounds(Point(0, 2))

    assert not edge1.shares_vert_bounds(Point(0, 3))
    assert not edge1.shares_vert_bounds(Point(1, 3))
    assert not edge1.shares_vert_bounds(Point(-1, 3))
    assert not edge1.shares_vert_bounds(Point(0, 1))
    assert not edge1.shares_vert_bounds(Point(1, 1))
    assert not edge1.shares_vert_bounds(Point(-1, 1))
