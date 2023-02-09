from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
import time



screen = Screen()
snake1 = Snake()
food = Food()
the_score = Scoreboard()

screen.listen()
screen.onkey(snake1.right, 'd')
screen.onkey(snake1.left, 'a')
screen.onkey(snake1.up, 'w')
screen.onkey(snake1.down, 's')


game_is_on = True
#screen.onkey(game_is_on = False,'')

#screen setup
screen.setup(600,600)
screen.bgcolor('black')
screen.title("snake game")
screen.tracer(0)

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake1.move()

    #detect collision whit food
    if snake1.head.distance(food) < 15:
        food.refresh_food()
        print("gnam gnam")
        snake1.add_segment()
        the_score.increase_score()

    #detec collision whit wall
    if snake1.head.xcor() > 285 or snake1.head.xcor() < -295 or snake1.head.ycor() > 300 or snake1.head.ycor() < -290:
        the_score.reset()
        snake1.reset()


    #detect collision whit tail
    for seg in snake1.segments[1:]:
        if snake1.head.distance(seg) < 10:
            the_score.reset()
            snake1.reset()

screen.exitonclick()