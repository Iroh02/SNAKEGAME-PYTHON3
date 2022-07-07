from turtle import Turtle
POSITIONS=[(0,0),(-20,0),(-40,0)]
DIST=20
UP=90
DOWN=270
RIGHT=0
LEFT=180
class Snake:
    def __init__(self):
        self.snake = []
        self.createsnake()

    def createsnake(self):

        for j in POSITIONS:
            self.addseg(j)

    def addseg(self,j):
        new = Turtle(shape="square")
        new.color("white")
        new.penup()
        new.goto(j)
        self.snake.append(new)
    def extend(self):
        self.addseg(self.snake[-1].position())
    def move(self):
        for j in range(len(self.snake)-1,0,-1):
            self.snake[j].goto(self.snake[j - 1].xcor(), self.snake[j - 1].ycor())
        self.snake[0].forward(DIST)
    def up(self):
        if self.snake[0].heading()!=DOWN:
         self.snake[0].setheading(UP)

    def down(self):
        if self.snake[0].heading() != UP:
         self.snake[0].setheading(DOWN)

    def right(self):
        if self.snake[0].heading() != LEFT:
         self.snake[0].setheading(RIGHT)

    def left(self):
        if self.snake[0].heading() != RIGHT:
         self.snake[0].setheading(LEFT)
