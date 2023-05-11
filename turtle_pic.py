import turtle
from random import randint, choice, randrange

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
    size = (randrange(10, 50, 5))
    turtle.left(randrange(0, 360, 10))

    turtle.pencolor(color)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.penup()
    for _ in range(5):
        turtle.forward(size)
        turtle.left(144)
    turtle.end_fill()


def left_mouse_click(x, y):
    star(x, y)


turtle.hideturtle()
turtle.speed(0)
turtle.penup()

turtle.Screen().bgcolor('black')
turtle.Screen().onclick(left_mouse_click)
turtle.Screen().listen()
