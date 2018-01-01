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


@raises(RuntimeError)
def same_space_room_test():
    # This room traces back on itself accidentally and should be invalid
    room1_points = [
        Point(0, 0),
        Point(10, 0),
        Point(10, 10),
        Point(10, 0),
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
        Edge(Point(0, 0), Point(50, 0)),
        Edge(Point(50, 0), Point(50, 50)),
        Edge(Point(50, 50), Point(0, 50)),
        Edge(Point(0, 50), Point(0, 0))
    ]
    assert len(edges) == len(expected)
    assert edges == expected


def inside_test_rect_room():
    room1_points = [
        Point(0, 0),
        Point(10, 0),
        Point(10, 10),
        Point(0, 10),
    ]
    room1 = Room(room1_points)
    assert room1.inside(Point(5, 5))

    # On the edges
    assert not room1.inside(Point(0, 5))
    assert not room1.inside(Point(10, 5))
    assert not room1.inside(Point(5, 0))
    assert not room1.inside(Point(5, 10))

    # Outside the edges
    assert not room1.inside(Point(-5, 5))
    assert not room1.inside(Point(5, -5))
    assert not room1.inside(Point(15, 5))
    assert not room1.inside(Point(5, 15))


def inside_test_L_room():
    """
    Shaped like:
     01234
    0###
    1# #
    2# ###
    3#   #
    4#####
    """
    room1_points = [
        Point(0, 0),
        Point(2, 0),
        Point(2, 2),
        Point(4, 2),
        Point(4, 4),
        Point(0, 4),
    ]
    room1 = Room(room1_points)
    assert room1.inside(Point(1, 1))
    assert room1.inside(Point(1, 2))
    assert room1.inside(Point(1, 3))
    assert room1.inside(Point(3, 3))

    # On the edges
    assert not room1.inside(Point(0, 0))
    assert not room1.inside(Point(2, 2))
    assert not room1.inside(Point(4, 2))
    assert not room1.inside(Point(4, 4))

    # Outside the edges
    assert not room1.inside(Point(3, 1))


def inside_test_u_room():
    """
    Shaped like:
     0123456
    0### ###
    1# # # #
    2# ### #
    3#     #
    4#######
    """
    room1_points = [
        Point(0, 0),
        Point(2, 0),
        Point(2, 2),
        Point(4, 2),
        Point(4, 0),
        Point(6, 0),
        Point(6, 4),
        Point(0, 4),
    ]
    room1 = Room(room1_points)

    assert room1.inside(Point(1, 1))
    assert room1.inside(Point(1, 3))
    assert room1.inside(Point(3, 3))
    assert room1.inside(Point(5, 1))
    assert room1.inside(Point(5, 3))

    assert not room1.inside(Point(3, 1))
    assert not room1.inside(Point(-1, 1))
    assert not room1.inside(Point(1, -1))
    assert not room1.inside(Point(3, -1))
    assert not room1.inside(Point(3, 5))
    assert not room1.inside(Point(7, 1))
    assert not room1.inside(Point(7, 3))


def test_intersects():
    """
    room1          room2         room3
    Shaped like:   Shaped like   Shaped like
     01234          01234         01234
    0###           0  ###        0###
    1# #           1  # #        1# #
    2# ###         2  ###        2###
    3#   #         3             3
    4#####         4             4


    room4          room5
    Shaped like    Shaped like
     01234          01234
    0              0
    1 ###          1###
    2 # #          2# #
    3 ###          3###
    """
    room1_points = [
        Point(0, 0),
        Point(2, 0),
        Point(2, 2),
        Point(4, 2),
        Point(4, 4),
        Point(0, 4),
    ]
    room1 = Room(room1_points)

    room2_points = [
        Point(2, 0),
        Point(4, 0),
        Point(4, 2),
        Point(2, 2),
    ]
    room2 = Room(room2_points)

    room3_points = [
        Point(0,0),
        Point(2,0),
        Point(2,2),
        Point(0,2),
    ]
    room3 = Room(room3_points)

    assert not room1.intersects(room2)
    assert room1.intersects(room3)

    assert not room2.intersects(room3)


