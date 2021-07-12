from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

is_race_on = False
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
y_coordinate = -125

# creating multiple turtle objects, setting its shape, color, penup, and starting coordinates, and finally appending it
# to a list of turtles
for color in colors:
    turtle = Turtle(shape="turtle")
    turtle.color(color)
    turtle.penup()
    turtle.goto(x=-230, y=y_coordinate)
    y_coordinate += 50
    all_turtles.append(turtle)

if user_bet:
    is_race_on = True

# making turtle move forwards to a random distance, and checking which turtle won.
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
