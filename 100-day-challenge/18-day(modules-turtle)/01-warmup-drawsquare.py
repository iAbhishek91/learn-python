# draw a square
from turtle import Turtle, Screen

turtle = Turtle()

turtle.speed(1)  # speed can be 0 to 10

for _ in range(4): 
    turtle.right(90)
    turtle.forward(200)

screen = Screen()
screen.exitonclick()
