from math import *
import turtle
window = turtle.Screen()


def multifaceted_shape_turtle(num_sides, line_length, dirs=1):
    turtle.shape('turtle')
    angle = 360 / num_sides
    if dirs != 1:
        angle = -angle
    for _ in range(num_sides):
        turtle.left(angle)
        turtle.forward(abs(line_length))


def nested_multifaceted(number_shapes, first_radius, step):
    for i in range(3, number_shapes + 1):
        half_inner_angle = (180 * (i - 2)) / (i * 2)
        turtle.left(half_inner_angle)
        lin_len = 2 * first_radius * sin(pi / i)
        multifaceted_shape_turtle(i, lin_len)
        turtle.right(half_inner_angle)
        first_radius += step
        turtle.penup()
        turtle.forward(step)
        turtle.pendown()


def arch_spiral_square():
    turtle.shape('turtle')
    k = 10
    fi_rad = 1.57
    fi_degr = 90
    for i in range(0, 1000):
        ro = k * fi_rad
        turtle.forward(ro)
        turtle.left(fi_degr)
        fi_rad += 0.5
        ro += ro


def draw_square(x, y, line_length):
    turtle.shape('turtle')
    turtle.color('green', 'Red')
    turtle.pensize(2)
    turtle.penup()
    turtle.pencolor('blue')
    turtle.goto(x, y)
    turtle.pendown()
    for i in range(4):
        turtle.forward(line_length)
        turtle.left(90)
        turtle.stamp()


def nested_square(num_increment, lin_len):
    increment = lin_len / num_increment
    for _ in range(num_increment):  # nested square
        start_x = -lin_len // 2
        start_y = -lin_len // 2
        draw_square(start_x, start_y, lin_len)
        lin_len -= increment


def spider_with_paws(num_paw, line_length):
    angle = 360 / num_paw
    for _ in range(num_paw):  # spider with paws
        turtle.shape('turtle')
        turtle.forward(line_length)
        turtle.stamp()
        turtle.goto(0, 0)
        turtle.right(angle)


def draw_circle(accuracy=36, small_length=10, dirn=1):
    multifaceted_shape_turtle(accuracy, small_length, dirn)


def draw_flower_of_circles(num_petal, accuracy_measure=36, circle_len=10):
    direction = 1
    for _ in range(num_petal):
        draw_circle(accuracy=accuracy_measure, small_length=circle_len, dirn=direction)
        direction = -direction


def draw_butterfly(num_circles, inner_circle_len, grow_volume):
    turtle.right(90)
    for _ in range(num_circles):
        draw_flower_of_circles(2, inner_circle_len)
        inner_circle_len += grow_volume


def draw_spring(num_arc, outer_radius, inner_radius):
    turtle.right(90)
    turtle.penup()
    turtle.goto(-600, 0)
    turtle.pendown()
    turtle.pensize(5)
    turtle.circle(outer_radius, -180)
    for _ in range(num_arc - 1):
        turtle.circle(inner_radius, -180)
        turtle.circle(outer_radius, -180)


def draw_smile(face_color, eye_color):
    turtle.penup()
    turtle.goto(0, -200)
    turtle.pendown()
    turtle.fillcolor(face_color)
    turtle.begin_fill()
    turtle.circle(200)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(80, 70)
    turtle.pendown()
    turtle.fillcolor(eye_color)
    turtle.begin_fill()
    turtle.circle(30)
    turtle.penup()
    turtle.goto(-80, 70)
    turtle.pendown()
    turtle.circle(30)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(0, 40)
    turtle.pendown()
    turtle.pensize(20)
    turtle.right(90)
    turtle.forward(80)
    turtle.penup()
    turtle.goto(100, -60)
    turtle.pendown()
    turtle.left(180)
    turtle.pensize(20)
    turtle.pencolor('red')
    turtle.circle(100, -180)

