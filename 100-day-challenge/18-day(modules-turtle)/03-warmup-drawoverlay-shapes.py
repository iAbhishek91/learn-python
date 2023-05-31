import random
from turtle import Turtle, Screen

t = Turtle()
t.speed(2)
colors = ["coral", "cornsilk3", "dark khaki", "DeepPink4", "gold4", "gray28", "green yellow", "LawnGreen", "LightSalmon"]


def draw_shape(sides):
    angle = 360 / sides
    t.color(random.choice(colors))
    for _ in range(sides):
        t.forward(100)
        t.right(angle)
    t.home()


for side in range(3, 16):
    draw_shape(side)

s = Screen()
s.exitonclick()