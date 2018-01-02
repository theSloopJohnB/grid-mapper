from gridmapper.model.room import *
from gridmapper.view.grid_view import *
from mako import exceptions

def get_rectangles():
    rect0_points = [
        Point(210, 100),
        Point(340, 100),
        Point(340, 200),
        Point(210, 200),
    ]
    rect0 = Rectangle(rect0_points)

    rect1_points = [
        Point(440, 100),
        Point(340, 100),
        Point(340, 200),
        Point(440, 200),
    ]
    rect1 = Rectangle(rect1_points)

    return [rect0, rect1]

def make_grid():
    rects = get_rectangles()
    room1 = Room()
    room1.add_rectangle(rects[0])
    room1.add_rectangle(rects[1])
    # room2 = Room()
    # room2.add_rectangle(rects[2])

    grid = Grid()
    grid.add_room(room1)
    # grid.add_room(room2)
    return grid

def main():
    grid = make_grid()
    gridview = GridView(grid)

    try:
        with open('out/test.html', mode='w') as file:
            file.write(gridview.render())
    except:
        print(exceptions.text_error_template().render())

if __name__ == "__main__":
    main()
