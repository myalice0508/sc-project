"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.gui.events.mouse import onmouseclicked, onmousemoved
from campy.graphics.gobjects import GLabel

FRAME_RATE = 1000 / 120 # 120 frames per second
NUM_LIVES = 3			# Number of attempts

#global variance
graphics = BreakoutGraphics()
can_stop = True

def main():

    # Add animation loop here!
    onmouseclicked(start_game)

def start_game(mouse):
    global can_stop
    global NUM_LIVES
    global FRAME_RATE

    if NUM_LIVES > 0:
        if can_stop == True:
            can_stop = False
            # can't be stopped if the game continuing
            graphics.set_ball_velocity_x()
            graphics.set_ball_velocity_y()
            while True:
                ball_dx = graphics.get_x()
                ball_dy = graphics.get_y()
                graphics.ball.move(ball_dx, ball_dy)
                graphics.check()
                if graphics.ball.y + graphics.ball.height >= graphics.paddle.y + graphics.paddle_h:
                    # drop the window bottom
                    graphics.restart_ball()
                    NUM_LIVES -= 1
                    break
                if graphics.total == 0:
                    # no brick in the window
                    graphics.restart_ball()
                    break
                if graphics.ball.x <= 0:
                    # collide the left window
                    graphics.reverse_x()
                elif graphics.ball.x + graphics.ball.width >= graphics.window.width:
                    # collide the right window
                    graphics.reverse_x()
                elif graphics.ball.y <= 0:
                    # collide the top window
                    graphics.reverse_y()
                pause(FRAME_RATE)
            can_stop = True

if __name__ == '__main__':
    main()
