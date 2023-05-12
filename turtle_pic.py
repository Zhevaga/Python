import turtle
from random import randint, choice, randrange
from math import sqrt, tan, radians, sin, cos, pi

# heart
turtle.penup()
turtle.fillcolor('red')
turtle.begin_fill()
t = 0
while t < 2 * pi:
    x = 128 * sin(t) ** 3
    y = 8 * (13 * cos(t) - 5 * cos(2 * t) - 2 * cos(3 * t) - cos(4 * t) - 5)
    turtle.goto(x, y)
    t += 0.01
turtle.end_fill()

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

# moon gif
turtle.Screen().bgcolor('blue')

moon = turtle.Turtle()
moon.hideturtle()
moon.dot(100, 'orange')

cl = turtle.Turtle()
cl.shape('circle')
cl.hideturtle()
cl.pencolor('blue')
cl.pensize(100)

while True:
    cl.penup()
    cl.goto(100, 0)
    cl.pendown()

    for _ in range(200):
        cl.backward(1)
        cl._tracer(2, 0)
        cl.clear()


# stars by click
def random_color():
    return randrange(256), randrange(256), randrange(256)


def star(x, y):
    turtle.goto(x, y)

    color = random_color()
    size = (randrange(20, 70, 5))
    turtle.left(randrange(0, 360, 10))

    turtle.pencolor(color)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.penup()
    count = randrange(5, 20, 2)
    for _ in range(count):
        turtle.forward(size)
        turtle.left(180 - (180 / count))
    turtle.end_fill()


def left_mouse_click(x, y):
    star(x, y)


turtle.hideturtle()
turtle.speed(0)
turtle.penup()

turtle.Screen().bgcolor('black')
turtle.Screen().onclick(left_mouse_click)
turtle.Screen().listen()

"""Напишите программу, которая рисует изображение правильных многоугольников
по образцу. Многоугольники должны иметь разный цвет. Площадь всех
многоугольников была одинаковой."""
# import turtle as t
# from math import *
# from random import randrange


# def random_color():
#    return randrange(256), randrange(256), randrange(256)


def figure():
    n = randrange(3, 8)
    a = sqrt((s * 100 * 4 * tan(radians(180) / n)) / n)
    g = 360 / n
    color = random_color()

    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(n):
        turtle.forward(int(a))
        turtle.right(g)
    turtle.forward(int(a))
    turtle.end_fill()


def picture():
    turtle.penup()
    turtle.goto(-250, 250)
    turtle.pendown()
    for _ in range(5):
        y = turtle.ycor()
        for _ in range(5):
            figure()
            turtle.penup()
            turtle.forward(s)
            turtle.pendown()
        turtle.penup()
        turtle.goto(-250, y - s * 2)
        turtle.pendown()


s = int(input())

turtle.Screen().setup(600, 600)
picture()

# chess_board
# import turtle
# from math import sqrt
colors = ('white', 'black')


def square(size_square, color, y):
    turtle.fillcolor(colors[color])
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(size_square)
        turtle.left(90)
    if y != 4:
        turtle.forward(size_square)
    turtle.end_fill()


def row(size_square, count):
    for y in range(5):
        color = (count + y) % 2
        square(size_square, color, y)


def chess_board(size_bord):
    turtle.penup()
    turtle.goto(-100, 100)
    turtle.pendown()
    size_square = sqrt(size_bord) / 5
    for i in range(5):
        y = turtle.ycor()
        count = (i + 1) % 2
        row(size_square, count)
        turtle.penup()
        turtle.goto(-100, y - size_square)
        turtle.pendown()


turtle.Screen().setup(400, 400)
size_bord = int(input('Какая площадь доски тебе нужна?\n'))
chess_board(size_bord)
