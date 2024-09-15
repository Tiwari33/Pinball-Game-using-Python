from turtle import Turtle,Screen
from create_paddle import Paddle
from ball import Ball
from score_paddle import Scorecard
import time
screen=Screen()
screen.bgcolor("black")
screen.setup(700,600)
screen.tracer(0)
paddle1=Paddle((320,0))
paddle2=Paddle((-320,0))
ball=Ball()
scorecard=Scorecard()

screen.listen()
screen.onkey(paddle1.up,"Up")
screen.onkey(paddle1.down,"Down")
screen.onkey(paddle2.up,"w")
screen.onkey(paddle2.down,"s")
game_on=True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor()>270 or ball.ycor()<-270:
        ball.bounce_y()
        
    if ball.distance(paddle1)<50 and ball.xcor()>290 or ball.distance(paddle2)<50 and ball.xcor()<-290:
       ball.bounce_x()
       
    if ball.xcor()>350:
        ball.reset_position()
        scorecard.left_score()
    if ball.xcor()<-350:
        ball.reset_position()
        scorecard.right_score()
    if scorecard.l_score==3 :
        game_on=False
        scorecard.goto(0,0)
        scorecard.write("Game Over",align="center",font=("Arial",36,"normal"))
        scorecard.goto(0,-100)
        scorecard.write("Left Won!!",align="center",font=("Arial",30,"normal"))
    elif scorecard.r_score==3:
        game_on=False
        scorecard.goto(0,0)
        scorecard.write("Game Over",align="center",font=("Arial",36,"normal"))
        scorecard.goto(0,-100)
        scorecard.write("Right Won!!",align="center",font=("Arial",30,"normal"))
            
        
    
screen.exitonclick()