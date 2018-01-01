from nose.tools import *
from rectangle import *


def valid_room_test():
    rect1_points = [
        Point(0, 0),
        Point(50, 0),
        Point(50, 50),
        Point(0, 50),
    ]
    rect1 = Rectangle(rect1_points)
    pass


@raises(RuntimeError)
def invalid_room_test():
    rect1_points = [
        Point(0, 0),
        Point(50, 0),
        Point(50, 50),
    ]
    rect1 = Rectangle(rect1_points)


@raises(RuntimeError)
def same_space_room_test():
    # This room traces back on itself accidentally and should be invalid
    rect1_points = [
        Point(0, 0),
        Point(10, 0),
        Point(10, 10),
        Point(10, 0),
    ]
    rect1 = Rectangle(rect1_points)


def edge_test_1():
    rect1_points = [
        Point(0, 0),
        Point(50, 0),
        Point(50, 50),
        Point(0, 50),
    ]
    rect1 = Rectangle(rect1_points)
    edges = rect1.get_edges()

    expected = [
        Edge(Point(0, 0), Point(50, 0)),
        Edge(Point(50, 0), Point(50, 50)),
        Edge(Point(50, 50), Point(0, 50)),
        Edge(Point(0, 50), Point(0, 0))
    ]
    assert len(edges) == len(expected)
    assert edges == expected


def inside_test_rect_room():
    rect1_points = [
        Point(0, 0),
        Point(10, 0),
        Point(10, 10),
        Point(0, 10),
    ]
    rect1 = Rectangle(rect1_points)
    assert rect1.inside(Point(5, 5))

    # On the edges
    assert not rect1.inside(Point(0, 5))
    assert not rect1.inside(Point(10, 5))
    assert not rect1.inside(Point(5, 0))
    assert not rect1.inside(Point(5, 10))

    # Outside the edges
    assert not rect1.inside(Point(-5, 5))
    assert not rect1.inside(Point(5, -5))
    assert not rect1.inside(Point(15, 5))
    assert not rect1.inside(Point(5, 15))


# def inside_test_L_room():
#     """
#     Shaped like:
#      01234
#     0###
#     1# #
#     2# ###
#     3#   #
#     4#####
#     """
#     rect1_points = [
#         Point(0, 0),
#         Point(2, 0),
#         Point(2, 2),
#         Point(4, 2),
#         Point(4, 4),
#         Point(0, 4),
#     ]
#     rect1 = Rectangle(rect1_points)
#     assert rect1.inside(Point(1, 1))
#     assert rect1.inside(Point(1, 2))
#     assert rect1.inside(Point(1, 3))
#     assert rect1.inside(Point(3, 3))
#
#     # On the edges
#     assert not rect1.inside(Point(0, 0))
#     assert not rect1.inside(Point(2, 2))
#     assert not rect1.inside(Point(4, 2))
#     assert not rect1.inside(Point(4, 4))
#
#     # Outside the edges
#     assert not rect1.inside(Point(3, 1))
#
#
# def inside_test_u_room():
#     """
#     Shaped like:
#      0123456
#     0### ###
#     1# # # #
#     2# ### #
#     3#     #
#     4#######
#     """
#     rect1_points = [
#         Point(0, 0),
#         Point(2, 0),
#         Point(2, 2),
#         Point(4, 2),
#         Point(4, 0),
#         Point(6, 0),
#         Point(6, 4),
#         Point(0, 4),
#     ]
#     rect1 = Rectangle(rect1_points)
#
#     assert rect1.inside(Point(1, 1))
#     assert rect1.inside(Point(1, 2))
#     assert rect1.inside(Point(1, 3))
#     assert rect1.inside(Point(2, 3))
#     assert rect1.inside(Point(3, 3))
#     assert rect1.inside(Point(4, 3))
#     assert rect1.inside(Point(5, 3))
#     assert rect1.inside(Point(5, 2))
#     assert rect1.inside(Point(5, 1))
#
#     assert not rect1.inside(Point(3, 1))
#     assert not rect1.inside(Point(-1, 1))
#     assert not rect1.inside(Point(1, -1))
#     assert not rect1.inside(Point(3, -1))
#     assert not rect1.inside(Point(3, 5))
#     assert not rect1.inside(Point(7, 1))
#     assert not rect1.inside(Point(7, 3))
#
#

def get_rectangles():
    """
    rect1          rect2         room3
    Shaped like    Shaped like   Shaped like
     01234          01234         01234
    0              0  ###        0###
    1###           1  # #        1# #
    2# #           2  ###        2###
    3###           3             3

    room4          room5
    Shaped like    Shaped like
     01234          01234
    0              0
    1              1
    2 ###          2
    3 # #          3 ###
    4 ###          4 # #
                   5 ###
    """
    rect1_points = [
        Point(0, 1),
        Point(2, 1),
        Point(2, 3),
        Point(0, 3),
    ]
    rect1 = Rectangle(rect1_points)

    rect2_points = [
        Point(2, 0),
        Point(4, 0),
        Point(4, 2),
        Point(2, 2),
    ]
    rect2 = Rectangle(rect2_points)

    rect3_points = [
        Point(0,0),
        Point(2,0),
        Point(2,2),
        Point(0,2),
    ]
    rect3 = Rectangle(rect3_points)

    rect4_points = [
        Point(1,2),
        Point(3,2),
        Point(3,4),
        Point(1,4),
    ]
    rect4 = Rectangle(rect4_points)

    rect5_points = [
        Point(1,3),
        Point(3,3),
        Point(3,5),
        Point(1,5),
    ]
    rect5 = Rectangle(rect5_points)
    return [rect1, rect2, rect3, rect4, rect5]


def test_intersects():
    rect1, rect2, rect3, rect4, rect5 = get_rectangles()

    assert not rect1.intersects(rect2)
    assert rect1.intersects(rect3)
    assert rect1.intersects(rect4)
    assert not rect1.intersects(rect5)

    assert not rect2.intersects(rect3)
    assert not rect2.intersects(rect4)
    assert not rect2.intersects(rect5)

    assert not rect3.intersects(rect4)
    assert not rect3.intersects(rect5)

    assert rect4.intersects(rect5)

def test_conjoins():
    rect1, rect2, rect3, rect4, rect5 = get_rectangles()

    assert rect1.conjoins(rect2)
    assert not rect1.conjoins(rect3)
    assert not rect1.conjoins(rect4)
    assert rect1.conjoins(rect5)

    assert rect2.conjoins(rect3)
    assert rect2.conjoins(rect4)
    assert not rect2.conjoins(rect5)

    assert rect3.conjoins(rect4)
    assert not rect3.conjoins(rect5)

    assert not rect4.conjoins(rect5)
