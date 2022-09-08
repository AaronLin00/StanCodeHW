"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10        # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    count = NUM_LIVES
    # Add the animation loop here!
    while count != 0:
        if not graphics.get_brick_number() == 0:
            graphics.detect()
            graphics.ball.move(graphics.get_vx(),graphics.get_vy())
            if graphics.ball.x <= 0 or graphics.ball.x+graphics.ball.width > graphics.window.width:
                graphics.get_nvx()
            if graphics.ball.y <= 0:
                graphics.get_nvy()
            if graphics.ball.y+graphics.ball.height > graphics.window.height:
                graphics.restart()
                count -= 1
            pause(FRAME_RATE)
            # print(graphics.get_brick_number())
            # print(count)
        else:
            print("You win")
            break
    print('Game Over')
if __name__ == '__main__':
    main()
