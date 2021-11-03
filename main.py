import turtle

import colorgram

# colors = colorgram.extract('image.jpeg', 30)
#
# color_list = []
#
# for i in range(0, 30):
#     i_color = colors[i]
#     my_tuple = (i_color.rgb.r, i_color.rgb.g, i_color.rgb.b)
#     color_list.append(my_tuple)
#
#
# print(color_list)

from turtle import Turtle, Screen
import random


my_color_list = [(212, 154, 98), (236, 241, 245), (53, 107, 131), (199, 142, 34), (178, 78, 33), (116, 156, 171),
                 (124, 79, 98), (123, 175, 157), (226, 198, 129), (190, 88, 109), (12, 49, 64), (56, 39, 19),
                 (40, 168, 128), (50, 126, 121), (199, 123, 143), (166, 21, 30), (225, 93, 78), (244, 163, 160),
                 (38, 32, 34), (3, 25, 25), (79, 147, 169), (163, 26, 21), (19, 79, 91), (235, 166, 170),
                 (171, 207, 190), (102, 127, 158), (163, 203, 211)]

turtle.colormode(255)
tim = Turtle()
turtle.setup(600, 1200)
tim.penup()
tim.hideturtle()
tim.setpos(-225, -250)
tim.speed("fastest")


def random_color():
    my_tuple = random.choice(my_color_list)
    return my_tuple


def draw_row():
    for i in range(9):
        tim.dot(20, random_color())
        tim.forward(50)


def turn_tim_left():
    tim.dot(20, random_color())
    tim.left(90)
    tim.forward(50)
    tim.left(90)


def turn_tim_right():
    tim.dot(20, random_color())
    tim.right(90)
    tim.forward(50)
    tim.right(90)


for _ in range(5):
    draw_row()
    turn_tim_left()
    draw_row()
    turn_tim_right()

Screen()
turtle.exitonclick()


