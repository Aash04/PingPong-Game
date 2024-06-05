import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from seperator import Seperator

screen = Screen()

screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
position = [(0, -280), (0, -240), (0, -200), (0, -160), (0, -120), (0, -80), (0, -40), (0, 0), (0, 40), (0, 80),
            (0, 120), (0, 160), (0, 200), (0, 240), (0, 280), ]
for i in position:
    seperator = Seperator(i)

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)

    screen.update()
    ball.move()

    # Detect collision will wall
    if ball.ycor() > 278 or ball.ycor() < -278:
        ball.bounce_y()

    # Detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > 380 and ball.distance(r_paddle) > 50:
        ball.reset_position()
        scoreboard.l_point()

    # Detect L paddle misses
    if ball.xcor() < -380 and ball.distance(l_paddle) > 50:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
