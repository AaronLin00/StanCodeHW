"""
File: 
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked


window = GWindow()

SIZE = 10
count = 1
mousex = 0
mousey = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """

    onmouseclicked(create_circle)


def create_circle(mouse):
    """
    Use mousex and mousey to save previous coordinate and remove the circle when second click appear.
    """
    global mousex
    global mousey
    global count
    if not count % 2 == 0:
        circle = GOval(SIZE, SIZE, x=mouse.x - SIZE / 2, y=mouse.y - SIZE / 2)
        circle.filled = False
        window.add(circle)
        mousex = mouse.x
        mousey = mouse.y
    else:
        remove_circle = window.get_object_at(mousex, mousey)
        window.remove(remove_circle)
        line = GLine(mousex, mousey, mouse.x, mouse.y)
        window.add(line)
    count += 1


if __name__ == "__main__":
    main()
