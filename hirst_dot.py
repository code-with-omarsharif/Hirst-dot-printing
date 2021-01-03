from turtle import Turtle, Screen, colormode
import random

dot = Turtle()
screen = Screen()
colormode(255)

dot.speed("fastest")
dot.hideturtle()
dot.penup()

dot.setheading(230)
dot.forward(250)
dot.setheading(0)

number_of_dot = 100

# Random color generator using colormode module


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    Random_color = (r, g, b)
    return Random_color

# Creating dot with random color


def create_dot(num_of_dot):
    for dot_count in range(1, num_of_dot + 1):
        dot.dot(25, random_color())
        dot.forward(50)
# printing all dot in the same alignment

        if dot_count % 10 == 0:
            dot.setheading(90)
            dot.forward(50)
            dot.setheading(180)
            dot.forward(500)
            dot.setheading(0)


create_dot(number_of_dot)

screen.exitonclick()
