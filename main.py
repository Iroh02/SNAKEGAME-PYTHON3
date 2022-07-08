from turtle import Screen
from food import Food
import time
from snake import Snake
from scoreboard import Scoreboard
screen = Screen()
wannplay=True
while wannplay:
 screen.bgcolor("black")
 screen.tracer(0)
 snake=Snake()
 food=Food()
 score=Scoreboard()
 screen.listen()
 screen.onkey(snake.up,"Up",)
 screen.onkey(snake.down,"Down")
 screen.onkey(snake.right,"Right")
 screen.onkey(snake.left,"Left")
 isgameon=True
 while isgameon:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.snake[0].distance(food)<15:
        print("nom nom")
        food.refresh()
        snake.extend()
        score.increasescore()

    if snake.snake[0].xcor()>300 or snake.snake[0].xcor()<-320 or snake.snake[0].ycor()>270 or snake.snake[0].ycor()<-270 :
     isgameon=False
     score.gameover()
#          detect collision
     for seg in snake.snake[1:]:
         if snake.snake[0].distance(seg)<10:
             score.gameover()
             isgameon=False
 choice= screen.textinput(title="SNAKE GAME",prompt="Play again?Y/N")
 choice=choice.lower()
 if choice=='y':
     wannplay=True
     screen.clear()
 elif choice=='n':
     wannplay=False
     screen.clear()
     screen.bye()

