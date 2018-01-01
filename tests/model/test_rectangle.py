from nose.tools import *
from gridmapper.model.rectangle import *


def eq_rect_test():
    rect1_points = [
        Point(0, 0),
        Point(50, 0),
        Point(50, 50),
        Point(0, 50),
    ]
    rect2_points = [
        Point(0, 50),
        Point(50, 50),
        Point(50, 0),
        Point(0, 0),
    ]
    rect3_points = [
        Point(0, 0),
        Point(10, 0),
        Point(10, 10),
        Point(0, 10),
    ]
    rect1 = Rectangle(rect1_points)
    rect2 = Rectangle(rect2_points)
    rect3 = Rectangle(rect3_points)
    assert rect1 == rect2
    assert rect1 != rect3
    assert rect2 != rect3


def valid_rect_test():
    rect1_points = [
        Point(0, 0),
        Point(50, 0),
        Point(50, 50),
        Point(0, 50),
    ]
    rect1 = Rectangle(rect1_points)
    pass


@raises(RuntimeError)
def invalid_rect_test():
    rect1_points = [
        Point(0, 0),
        Point(50, 0),
        Point(50, 50),
    ]
    rect1 = Rectangle(rect1_points)


@raises(RuntimeError)
def same_space_rect_test():
    # This rect traces back on itself accidentally and should be invalid
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
    edges = rect1.edges

    expected = [
        Edge(Point(0, 0), Point(50, 0)),
        Edge(Point(50, 0), Point(50, 50)),
        Edge(Point(50, 50), Point(0, 50)),
        Edge(Point(0, 50), Point(0, 0))
    ]
    assert len(edges) == len(expected)
    assert edges == expected


def inside_test_rect_rect():
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

def inside_test_with_edges_rect():
    rect1_points = [
        Point(0, 0),
        Point(10, 0),
        Point(10, 10),
        Point(0, 10),
    ]
    rect1 = Rectangle(rect1_points)
    assert rect1.inside(Point(5, 5), include_edges=True)

    # On the edges
    assert rect1.inside(Point(0, 5), include_edges=True)
    assert rect1.inside(Point(10, 5), include_edges=True)
    assert rect1.inside(Point(5, 0), include_edges=True)
    assert rect1.inside(Point(5, 10), include_edges=True)

    # Outside the edges
    assert not rect1.inside(Point(-5, 5), include_edges=True)
    assert not rect1.inside(Point(5, -5), include_edges=True)
    assert not rect1.inside(Point(15, 5), include_edges=True)
    assert not rect1.inside(Point(5, 15), include_edges=True)


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
