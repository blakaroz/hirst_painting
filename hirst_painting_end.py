import random
import turtle
from turtle import Turtle,Screen
turtle.colormode(255)
tim = Turtle()
tim.speed("fastest")
tim.up()
tim.hideturtle()

color_list = [(132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56)]

# painting 10 x 10
# each dot 20 and space between 50
tim.backward(200)
tim.left(90)
tim.forward(200)
tim.setheading(0)
def draw(space, size_of_side):
    for i in range(size_of_side):
        for j in range(size_of_side):
            tim.dot(20,random.choice(color_list))
            tim.forward(space)
        tim.backward(space*size_of_side)
        tim.right(90)
        tim.forward(space)
        tim.left(90)



draw(50,10)


screen = Screen()
screen.exitonclick()
