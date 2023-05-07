import turtle
from random import randint, choice

# snow
turtle.Screen().setup(600, 600)
turtle.Screen().bgcolor('midnight blue')
turtle.speed(8)

colors = ['misty rose', 'ghost white', 'azure', 'light steel blue', 'snow']


def snow():
    size = randint(10, 50)
    line = size // 3
    for _ in range(8):
        for _ in range(3):
            turtle.forward(line)
            turtle.left(45)
            turtle.forward(line)
            turtle.backward(line)
            turtle.right(90)
            turtle.forward(line)
            turtle.backward(line)
            turtle.left(45)
        turtle.forward(line)
        turtle.backward(size + line)
        turtle.left(45)


def flower():
    corner = [60, 120] * 2
    size = randint(10, 50)
    for _ in range(10):
        turtle.left(36)
        for i in range(4):
            turtle.forward(size)
            turtle.left(corner[i])


def place():
    turtle.penup()
    turtle.goto(randint(-200, 200), randint(-200, 200))
    turtle.pendown()
    turtle.pencolor(choice(colors))
    num = randint(1, 2)
    if num == 1:
        snow()
    else:
        flower()


def pen():
    for _ in range(int(input())):
        place()


pen()

# square
color = ['black', 'green', 'blue', 'red', 'yellow']


def square(count, side):
    turtle.shape('turtle')
    for _ in range(count):
        turtle.color(color[randint(0, 4)])
        for _ in range(8):
            for _ in range(4):
                turtle.forward(side)
                turtle.left(90)
            turtle.left(45)
        side += 10


c = int(input())
s = int(input())
square(c, s)
