from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

screen.listen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def counter_clockwise():
    current_heading = tim.heading()
    new_heading = current_heading - 10
    tim.setheading(new_heading)


def clockwise():
    current_heading = tim.heading()
    new_heading = current_heading + 10
    tim.setheading(new_heading)


def clear():
    screen.reset()


screen.onkeypress(fun=move_forward, key="w")
screen.onkeypress(fun=move_backward, key="s")
screen.onkeypress(fun=counter_clockwise, key="a")
screen.onkeypress(fun=clockwise, key="d")
screen.onkeypress(fun=clear, key="c")

screen.exitonclick()
