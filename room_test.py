from room import *
from nose.tools import *


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


def add_rect_good_test():
    room = Room()
    rect1, rect2, _, _, _ = get_rectangles()
    room.add_rectangle(rect1)
    room.add_rectangle(rect2)


@raises(RuntimeError)
def add_rect_same_test():
    room = Room()
    rect1, _, _, _, _ = get_rectangles()
    room.add_rectangle(rect1)
    room.add_rectangle(rect1)


@raises(RuntimeError)
def add_rect_intersect_test():
    room = Room()
    rect1, _, _, rect4, _ = get_rectangles()
    room.add_rectangle(rect1)
    room.add_rectangle(rect4)



