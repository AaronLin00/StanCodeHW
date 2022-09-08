"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10       # Number of rows of bricks
BRICK_COLS = 10       # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_rows * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_cols * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(PADDLE_WIDTH, PADDLE_HEIGHT)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(window_width-paddle_width)/2, y= window_height- paddle_offset)
        # Center a filled ball in the graphical window
        self.ball = GOval(BALL_RADIUS*2, BALL_RADIUS*2)
        self.ball.filled = True
        self.window.add(self.ball, x=(window_width - ball_radius) / 2, y=(window_height - ball_radius) / 2)
        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        # Initialize our mouse listeners
        self.switch = 0
        self.brick_number = BRICK_ROWS * BRICK_COLS
        self.ballstart = onmouseclicked(self.ballmove)
        self.paddlemove = onmousemoved(self.move)
        # Draw bricks
        count_color = 0
        # The function below create five colors brick and keep same pattern no matter how many rows or columns there are.
        for i in range(BRICK_ROWS):
            count_color = 0
            for j in range(BRICK_COLS):
                self.rect = GRect(BRICK_WIDTH, BRICK_HEIGHT)
                self.rect.filled = True
                if count_color == 0 or count_color == 1:
                    self.rect.fill_color = "red"
                    count_color += 1
                elif count_color == 2 or count_color == 3:
                    self.rect.fill_color = "orange"
                    count_color += 1
                elif count_color == 4 or count_color == 5:
                    self.rect.fill_color = "yellow"
                    count_color += 1
                elif count_color == 6 or count_color == 7:
                    self.rect.fill_color = "green"
                    count_color += 1
                elif count_color == 8:
                    self.rect.fill_color = "blue"
                    count_color += 1
                else:
                    self.rect.fill_color = "blue"
                    count_color = 0
                self.window.add(self.rect, x=i*brick_spacing + i*brick_width, y=brick_offset+j*brick_spacing+j*brick_height)

    def move(self, mouse):
        """
        Help paddle move with the mouse.
        """
        if mouse.x - PADDLE_WIDTH/2 < PADDLE_WIDTH/2:
            self.paddle.x = 0
        elif mouse.x + PADDLE_WIDTH/2 > self.window.width-PADDLE_WIDTH/2:
            self.paddle.x = self.window.width-PADDLE_WIDTH
        else:
            self.paddle.x = mouse.x - PADDLE_WIDTH/2

    def ballmove(self, mouse):
        """
        Ball will drop when click the mouse.
        """
        if self.switch != 1:
            self.switch = 1
            self.__dx = random.randint(1, MAX_X_SPEED)
            self.__dy = INITIAL_Y_SPEED
            if (random.random() > 0.5):
                self.__dx = - self.__dx
        else:
            pass

    def restart(self):
        """
        When the ball hit the bottom, restart function will help ball back to start point.
        """
        self.switch = 0
        self.window.add(self.ball, x=(self.window.width - BALL_RADIUS) / 2, y=(self.window.height - BALL_RADIUS) / 2)
        ballmove = onmouseclicked(self.ballmove)
        self.__dx = 0
        self.__dy = 0
        # print("a")

    def get_vx(self):
        return self.__dx

    def get_vy(self):
        return self.__dy

    def get_nvx(self):
        self.__dx *= -1

    def get_nvy(self):
        self.__dy *= -1

    def get_brick_number(self):
        return self.brick_number

    def detect(self):
        """
        This function can distinguish brick and paddle, the function will remove brick when ball hit the brick.
        """
        detect1 = self.window.get_object_at(self.ball.x, self.ball.y)
        detect2 = self.window.get_object_at(self.ball.x, self.ball.y + 2*BALL_RADIUS)
        detect3 = self.window.get_object_at(self.ball.x + 2*BALL_RADIUS, self.ball.y)
        detect4 = self.window.get_object_at(self.ball.x + 2*BALL_RADIUS, self.ball.y + 2*BALL_RADIUS)
        if detect1 != None:
            if self.ball.y < self.window.height - (PADDLE_OFFSET+PADDLE_HEIGHT):
                self.window.remove(detect1)
                self.brick_number -= 1
                self.get_nvy()
            elif self.__dy > 0:
                self.get_nvy()
        elif detect2 != None:
            if self.ball.y < self.window.height - (PADDLE_OFFSET+PADDLE_HEIGHT):
                self.window.remove(detect2)
                self.brick_number -= 1
                self.get_nvy()
            elif self.__dy > 0:
                self.get_nvy()
        elif detect3 != None:
            if self.ball.y < self.window.height - (PADDLE_OFFSET+PADDLE_HEIGHT):
                self.window.remove(detect3)
                self.brick_number -= 1
                self.get_nvy()
            elif self.__dy > 0:
                self.get_nvy()
        elif detect4 != None:
            if self.ball.y < self.window.height - (PADDLE_OFFSET+PADDLE_HEIGHT):
                self.window.remove(detect4)
                self.brick_number -= 1
                self.get_nvy()
            elif self.__dy > 0:
                self.get_nvy()