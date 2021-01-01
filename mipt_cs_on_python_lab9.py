import turtle
win_width, win_height, bg_color = 2000, 2000, 'white'
turtle.screensize(win_width, win_height, bg_color)


window = turtle.Screen()


def draw_branch(l, n):
    """Example from lecturer T.F. Khiryanov"""
    if n == 0:
        turtle.left(180)
        return
    x = l / (n + 1)
    for i in range(n):
        turtle.forward(x)
        turtle.left(45)
        draw_branch(0.5 * x * (n - i - 1), n - i - 1)
        turtle.left(90)
        draw_branch(0.5 * x * (n - i - 1), n - i - 1)
        turtle.right(135)
    turtle.forward(x)
    turtle.left(180)
    turtle.forward(l)


def koch_curve(size, n):
    """draws Koch's curve with preset size and order"""
    if n == 0:
        turtle.forward(size)
    else:
        koch_curve(size / 3, n - 1)
        turtle.left(60)
        koch_curve(size / 3, n - 1)
        turtle.right(120)
        koch_curve(size / 3, n - 1)
        turtle.left(60)
        koch_curve(size / 3, n - 1)


def koch_snowflake(size, n):
    """draws Koch's snowflake"""
    iter_len = size / 3
    for _ in range(3):
        koch_curve(iter_len, n)
        turtle.right(120)


def start(x: float):
    """This function clears window and make turtle go to start"""
    turtle.clear()
    turtle.penup()
    x = x if x < 0 else -x
    turtle.goto(x, 0)
    turtle.pendown()


def curve_minkowski(length: float, iterations: int):
    """This function draw Minkowski's curve"""
    if iterations == 0:
        turtle.forward(length * 4)
    else:
        curve_minkowski(length/4, iterations - 1)
        turtle.left(90)
        curve_minkowski(length/4, iterations - 1)
        turtle.right(90)
        curve_minkowski(length/4, iterations - 1)
        turtle.right(90)
        curve_minkowski(length/4, iterations - 1)
        curve_minkowski(length/4, iterations - 1)
        turtle.left(90)
        curve_minkowski(length/4, iterations - 1)
        turtle.left(90)
        curve_minkowski(length/4, iterations - 1)
        turtle.right(90)
        curve_minkowski(length/4, iterations - 1)


def levy_curve(iterations=1, actions=None, length=None):
    """draws levy curve with preset orders"""
    instruction = ['l', 'f', 'r', 'f', 'l']
    if not actions:
        actions = ['f']
    if not length:
        length = 200 / 2 ** (iterations/2)
    for i in actions:
        if i == 'f':
            if iterations != 0:
                movement(iterations - 1, instruction, length)
            else:
                turtle.forward(length)
        elif i == 'l':
            turtle.left(45)
        elif i == 'r':
            turtle.right(90)


def dragon_curve_recursive(order: int, length, sign):
    """recursive for drawing dragon curve"""
    if order == 0:
        turtle.forward(length)
    else:
        rootHalf = (1 / 2) ** (1 / 2)
        dragon_curve_recursive(order - 1, length * rootHalf, 1)
        turtle.left(sign * -90)
        dragon_curve_recursive(order - 1, length * rootHalf, -1)


def dragon_curve(order: int, length) -> None:
    """Draw a dragon curve."""
    turtle.left(order * 45)
    dragon_curve_recursive(order, length, 1)


def cantor_set(length, order, down_step=20):
    """draw cantor set with preset order and length"""
    if order == 0:
        turtle.forward(length)
    else:
        turtle.forward(length)
        x, y = turtle.pos()[0], turtle.pos()[1]
        turtle.penup()
        turtle.goto(x - length, y - down_step)
        turtle.pendown()
        cantor_set(length / 3, order - 1, down_step)
        turtle.penup()
        turtle.goto(x - length / 3, y - down_step)
        turtle.pendown()
        cantor_set(length / 3, order - 1, down_step)
