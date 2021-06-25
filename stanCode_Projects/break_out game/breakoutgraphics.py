"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        self.paddle_w = paddle_width
        self.paddle_h = paddle_height
        self.paddle_o = paddle_offset
        self.ball = ball_radius
        self.brick_c = brick_cols
        self.brick_r = brick_rows
        self.brick_w = brick_width
        self.brick_h = brick_height
        self.brick_s = brick_spacing
        self.brick_o = brick_offset
        self.total = self.brick_r * self.brick_c
        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(self.paddle_w, self.paddle_h)
        self.paddle.filled = True
        self.window.add(self.paddle, (self.window.width - self.paddle_w) / 2, self.window.height - self.paddle_h - self.paddle_o)

        # Center a filled ball in the graphical window
        self.ball = GOval(self.ball*2, self.ball*2)
        self.ball.filled = True
        self.window.add(self.ball, (self.window.width - self.ball.width)/2, (self.window.height -self.ball.height)/2)
        self.restart_ball()

        # Draw bricks
        for i in range(0,self.brick_r):
            for j in range(self.brick_c):
                brick = GRect(self.brick_w, self.brick_h)
                brick.filled = True
                if i%10 < 2:
                    brick.color = 'red'
                    brick.fill_color = 'red'
                elif 2 <= i%10 < 4:
                    brick.color = 'orange'
                    brick.fill_color = 'orange'
                elif 4 <= i%10 < 6:
                    brick.color = 'yellow'
                    brick.fill_color = 'yellow'
                elif 6 <= i%10 < 8:
                    brick.color = 'green'
                    brick.fill_color = 'green'
                elif 8 <= i%10 < 10:
                    brick.color = 'blue'
                    brick.fill_color = 'blue'
                self.window.add(brick, j*(brick.width + self.brick_s), 1 * self.brick_o + i * (self.brick_s + self.brick_h))

        self.__dx = 0
        self.__dy = 0

        # set ball velocity, random the x, y velocity
        self.set_ball_velocity_x()
        self.set_ball_velocity_y()


        # # Initialize our mouse listeners
        onmousemoved(self.move_paddle)


    def move_paddle(self,move_mouse):
        """
        :param move_mouse: when I　move the mouse, the paddle can move
        :return: the limit height and can't over the window width
        """
        self.paddle.x = move_mouse.x - self.paddle_w/2
        self.paddle.y = self.window.height - self.paddle_h - self.paddle_o/2
        if self.paddle.x < 0:
            self.paddle.x = 0
        if self.paddle.x + self.paddle_w > self.window.width:
            self.paddle.x = self.window.width - self.paddle_w

    def set_ball_velocity_x(self):
        """
        :return: set ball.x velocity
        """
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx


    def set_ball_velocity_y(self):
        """
        :return: set ball.y velocity
        """
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dy = -self.__dy

    def get_x(self):
        """
        :return: get private velocity_x
        """
        return self.__dx

    def get_y(self):
        """
        :return: get private velocity_y
        """
        return  self.__dy

    def reverse_x(self):
        """
        :return: get the reverse the velocity_x
        """
        self.__dx = -self.__dx

    def reverse_y(self):
        """
        :return: get the reverse the velocity_y
        """
        self.__dy = -self.__dy

    def restart_ball(self):
        """
        :return: back to original position
        """
        self.window.add(self.ball, (self.window.width - self.ball.width) / 2,
                        (self.window.height - self.ball.height) / 2)


    def check(self):
        """
        :return: the check the ball whether collide the brick
        """
        maybe_wall1 = self.window.get_object_at(self.ball.x, self.ball.y)
        maybe_wall2 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
        maybe_wall3 = self.window.get_object_at(self.ball.x + self.ball.height, self.ball.y + self.ball.width)
        maybe_wall4 = self.window.get_object_at(self.ball.x + self.ball.height, self.ball.y + self.ball.height)
        if maybe_wall1 or maybe_wall2 or maybe_wall3 or maybe_wall4 is not None:
            if maybe_wall1 is self.paddle:
                self.__dy = -self.__dy
                self.ball.move(self.__dx, self.__dy)
            elif maybe_wall2 is self.paddle:
                self.__dy = -self.__dy
                self.ball.move(self.__dx, self.__dy)
            elif maybe_wall3 is self.paddle:
                self.__dy = -self.__dy
                self.ball.move(self.__dx, self.__dy)
            elif maybe_wall4 is self.paddle:
                self.__dy = -self.__dy
                self.ball.move(self.__dx, self.__dy)

            else:
                if maybe_wall1 is not None:
                    self.__dy = -self.__dy
                    self.window.remove(maybe_wall1)
                    self.total -=1
                elif maybe_wall2 is not None:
                    self.__dy = -self.__dy
                    self.window.remove(maybe_wall2)
                    self.total -= 1
                elif maybe_wall3 is not None:
                    self.__dy = -self.__dy
                    self.window.remove(maybe_wall3)
                    self.total -= 1
                else:
                    self.__dy = -self.__dy
                    self.window.remove(maybe_wall4)
                    self.total -= 1