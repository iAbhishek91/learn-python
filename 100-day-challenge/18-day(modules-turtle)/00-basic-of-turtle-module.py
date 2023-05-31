# few common form of import
# import turtle # this is not advised as you are importing everything and you need to use turtle.something
# from turtle import * # not good practice as this will confuse with other module.
# e.g shape() directly, not knowling from where its coming from
from turtle import Turtle, Screen

# alias
# import turtle as t # sometime this is used for module with long names
abhi_the_turtle = Turtle()

abhi_the_turtle.shape("turtle")  # what is the shape of the turtle
abhi_the_turtle.turtlesize(2, 2, 1)  # change the size of the turtle

abhi_the_turtle.color("cyan")  # set pen color and fill color


screen = Screen()  # create a screen where the turtle would be shown

screen.exitonclick()  # exit the screen onClick
