import turtle
from random import randint as ri


color = ['black', 'green', 'blue', 'red', 'yellow']


def square(count, side):
    turtle.shape('turtle')
    for _ in range(count):
        turtle.color(color[ri(0, 4)])
        for _ in range(8):
            for _ in range(4):
                turtle.forward(side)
                turtle.left(90)
            turtle.left(45)
        side += 10


c = int(input())
s = int(input())
square(c, s)

# цветок из ромбов
corner = [60, 120] * 2


def flower(count, side):
    for _ in range(count):
        turtle.left(360 // count)
        for i in range(4):
            turtle.forward(side)
            turtle.left(corner[i])


flower(int(input()), int(input()))
