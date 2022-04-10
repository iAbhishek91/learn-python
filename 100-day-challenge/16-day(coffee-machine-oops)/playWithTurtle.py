# turtle is pre-downloaded with python
from turtle import Turtle, Screen

mini = Turtle("turtle")
mini.color("green")

count = 0
while count < 10:
    mini.speed("slow")
    mini.color("green")
    mini.forward(350)
    mini.color("red")
    mini.backward(350)
    count += 1

canvas = Screen()

canvas.exitonclick()