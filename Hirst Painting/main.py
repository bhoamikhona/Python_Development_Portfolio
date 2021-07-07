# import colorgram
import turtle
from random import choice

# list_of_colors = colorgram.extract("image.jpg", 25)
# rgb_colors = []
#
# for color in list_of_colors:
#     red = color.rgb.r
#     green = color.rgb.g
#     blue = color.rgb.b
#     rgb_colors.append((red, green, blue))
#
# print(rgb_colors)

tim = turtle.Turtle()

color_list = [(236, 35, 108), (145, 28, 65), (239, 74, 34), (6, 148, 93), (232, 168, 40), (184, 158, 46),
              (44, 191, 233), (27, 127, 195), (126, 193, 74), (253, 223, 0), (85, 28, 93), (172, 36, 98),
              (246, 219, 44), (42, 172, 112), (216, 130, 165), (216, 58, 26), (235, 164, 190), (156, 25, 22),
              (20, 189, 230), (238, 169, 157), (162, 210, 182)]

tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

turtle.colormode(255)

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle.Screen()
screen.exitonclick()
