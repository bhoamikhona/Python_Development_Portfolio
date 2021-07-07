from turtle import Turtle, Screen
from random import random, choice

tim = Turtle()
tim.shape("turtle")

""" Challenge 1: Draw a Square """
for _ in range(4):
    tim.forward(100)
    tim.right(90)

tim.reset()

""" Challenge 2: Draw a dashed line """
for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

tim.reset()

""" Challenge 3: Drawing different shapes """
def change_color():
    r = random()
    g = random()
    b = random()

    tim.color(r, g, b)


def draw_shape(no_of_sides):
    for _ in range(no_of_sides):
        tim.forward(100)
        tim.right(360/no_of_sides)


for i in range(3, 11):
    change_color()
    draw_shape(i)

tim.reset()


""" Challenge 4: Generate a random walk """
directions = [0, 90, 180, 270]


def generate_random_walk():
    tim.pensize(15)
    tim.speed("fastest")
    for _ in range(200):
        change_color()
        tim.forward(30)
        tim.right(choice(directions))


generate_random_walk()
tim.reset()


""" Challenge 5: Draw a Spirograph """
tim.speed("fastest")
for angle in range(36):
    change_color()
    current_heading = tim.heading()
    next_heading = current_heading + 10
    tim.setheading(next_heading)
    tim.circle(100)

screen = Screen()
screen.exitonclick()
