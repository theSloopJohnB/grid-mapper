from nose.tools import *
from gridmapper.viewmodel.grid import *
from gridmapper.model.room import *

def get_rectangles():
    """
    rect0         rect1        rect2
    Shaped like   Shaped like  Shaped like
     01234         01234        01234
    0  ###        0###         0
    1  # #        1# #         1
    2  ###        2###         2 ###
    3             3            3 # #
                               4 ###
    """
    rect0_points = [
        Point(2, 0),
        Point(4, 0),
        Point(4, 2),
        Point(2, 2),
    ]
    rect0 = Rectangle(rect0_points)

    rect1_points = [
        Point(0,0),
        Point(2,0),
        Point(2,2),
        Point(0,2),
    ]
    rect1 = Rectangle(rect1_points)

    rect2_points = [
        Point(1,2),
        Point(3,2),
        Point(3,4),
        Point(1,4),
    ]
    rect2 = Rectangle(rect2_points)

    return [rect0, rect1, rect2]

def columns_rows_test():
    rects = get_rectangles()
    room1 = Room()
    room1.add_rectangle(rects[0])
    room1.add_rectangle(rects[1])
    room2 = Room()
    room2.add_rectangle(rects[2])

    grid = Grid()
    grid.add_room(room1)
    grid.add_room(room2)

    assert grid.rows_pos == [0, 2, 4]
    assert grid.columns_pos == [0, 1, 2, 3, 4]

def width_test():
    # TODO add test for correct heights and widths
    assert False

def single_rect_test():
    # TODO fill this in
    assert False

def two_rect_test():
    # TODO fill this in with somethin
    assert False

def logical_grid_test():
    rects = get_rectangles()
    room1 = Room()
    room1.add_rectangle(rects[0])
    room1.add_rectangle(rects[1])
    room2 = Room()
    room2.add_rectangle(rects[2])

    grid = Grid()
    grid.add_room(room1)
    grid.add_room(room2)
    s = grid.logical_repr()
    expected = [
        [ 0,  0,  0,  0,  0],
        [ 0,  0,  0,  0,  0],
        [-1,  1,  1,  1, -1],
    ]
    assert s == expected

