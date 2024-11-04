from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Slippery Snake Slips")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
scoreboard.reset()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
screen.onkey(snake.down,"Down")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    snake.color_shift()
    #detect collision with food
    if snake.head.distance(food) < 15:
        print ("nomnomnom")
        food.refresh()
        snake.extend()
        scoreboard.gain_score()

    if scoreboard.current_score == 5:
        food.special_food()


    #detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor()> 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    #detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()




screen.exitonclick()