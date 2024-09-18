from turtle import Turtle
class Scorecard(Turtle):
    def __init__(self):
        super().__init__()
        
        self.color("red")
        self.penup()
        self.hideturtle()
        self.l_score=0
        self.r_score=0
        self.update()
    def update(self):
        self.clear()
        self.goto(-100,250)
        self.write(self.l_score,align="center",font=("Arial",30,"normal"))
        self.goto(100,250)
        self.write(self.r_score,align="center",font=("Arial",30,"normal"))
        
    def left_score(self):
        self.l_score+=1
        self.update()
    
    def right_score(self):
        self.r_score+=1
        self.update()