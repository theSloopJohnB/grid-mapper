from gridmapper.model.house import *
from nose.tools import *

def get_rectangles():
    """
    rect1          rect2         rect3
    Shaped like    Shaped like   Shaped like
     01234          01234         01234
    0              0  ###        0###
    1###           1  # #        1# #
    2# #           2  ###        2###
    3###           3             3

    rect4          rect5
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

def valid_house_test():
    rect1, rect2, rect3, rect4, rect5 = get_rectangles()

    house = House()
    room1 = Room()
    room1.add_rectangle(rect2)
    room1.add_rectangle(rect3)
    room2 = Room()
    room2.add_rectangle(rect4)
    room3 = Room()
    room3.add_rectangle(rect5)

    house.add_room(room1)
    house.add_room(room2)

@raises(RuntimeError)
def invalid_house_test():
    rect1, rect2, rect3, rect4, rect5 = get_rectangles()

    house = House()
    room2 = Room()
    room2.add_rectangle(rect4)
    room3 = Room()
    room3.add_rectangle(rect5)

    house.add_room(room2)
    house.add_room(room3)

def get_rectangles_test():
    rect1, rect2, rect3, rect4, rect5 = get_rectangles()

    house = House()
    room1 = Room()
    room1.add_rectangle(rect2)
    room1.add_rectangle(rect3)
    room2 = Room()
    room2.add_rectangle(rect4)

    house.add_room(room1)
    house.add_room(room2)

    a = house.rectangles
    b = [rect2, rect3, rect4]
    assert equal_ignore_order(a, b)


def get_edges_test():
    rect1, rect2, rect3, rect4, rect5 = get_rectangles()

    house = House()
    room1 = Room()
    room1.add_rectangle(rect2)
    room1.add_rectangle(rect3)
    room2 = Room()
    room2.add_rectangle(rect4)

    house.add_room(room1)
    house.add_room(room2)

    a = house.edges
    b = [rect2, rect3, rect4]
    bEdges = []

    for rectB in b:
        for edgeB in rectB.edges:
            bEdges.append(edgeB)

    assert equal_ignore_order(a, bEdges)


def equal_ignore_order(a, b):
    """ Use only when elements are neither hashable nor sortable! """
    unmatched = list(b)
    for element in a:
        try:
            unmatched.remove(element)
        except ValueError:
            return False
    return not unmatched

