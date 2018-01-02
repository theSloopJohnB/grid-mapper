from gridmapper.model.room import *
from gridmapper.view.grid_view import *
from mako import exceptions

def get_rectangles():
    rect0_points = [
        Point(210, 100),
        Point(640, 100),
        Point(640, 400),
        Point(210, 400),
    ]
    rect0 = Rectangle(rect0_points)

    rect1_points = [
        Point(640, 100),
        Point(740, 100),
        Point(740, 300),
        Point(640, 300),
    ]
    rect1 = Rectangle(rect1_points)
    #
    # rect2_points = [
    #     Point(340, 100),
    #     Point(440, 100),
    #     Point(440, 200),
    #     Point(340, 200),
    # ]
    # rect2 = Rectangle(rect2_points)

    return [
        [rect0],
        [rect1],
        # [rect2],
    ]

def make_grid():
    grid = Grid()
    for room in get_rectangles():
        room1 = Room()
        for rect in room:
            room1.add_rectangle(rect)
        grid.add_room(room1)

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
