from nose.tools import *
from house import *


def horizontal_edge_test():
    edge = Edge(Point(0,0), Point(0, 50))
    assert not edge.is_horizontal()
    assert edge.is_vertical()
