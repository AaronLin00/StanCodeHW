"""
File: 
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
VY = 1
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40


window = GWindow(800, 500, title='bouncing_ball.py')

switch = 0
count = 0
y = VY


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball0 = GOval(SIZE, SIZE, x=START_X, y=START_Y)
    ball0.filled = True
    window.add(ball0)
    onmouseclicked(bounce)


def bounce(mouse):
    """
    We don't have to use mouse's coordinate, since the mouse only control start.
    """
    global VX
    global VY
    global y
    global count
    global switch
    if switch != 1:
        switch = 1
        remove_ball0 = window.get_object_at(START_X+(SIZE/2), START_Y+(SIZE/2))
        window.remove(remove_ball0)
        ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
        ball.filled = True
        window.add(ball)
        while count != 3:
            if ball.x < window.width:
                ball.move(VX, y)
                pause(DELAY)
                if ball.y < window.height:
                    y += GRAVITY
                else:
                    y = -y
                    y *= REDUCE
            else:
                count += 1
                ball.x = START_X
                ball.y = START_Y
                y = VY


if __name__ == "__main__":
    main()
