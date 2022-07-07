from turtle import Turtle

FONT = ("Arial", 24, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,230)
        self.hideturtle()
        self.updatescore()

    def updatescore(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increasescore(self):
        self.score += 1
        self.clear()
        self.updatescore()
    def gameover(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)