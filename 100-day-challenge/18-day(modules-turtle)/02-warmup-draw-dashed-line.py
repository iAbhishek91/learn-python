from turtle import Turtle, Screen

t = Turtle()

for _ in range(50):
    t.forward(5)
    t.penup()
    t.forward(5)
    t.pendown()

screen = Screen()
screen.exitonclick()
