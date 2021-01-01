"""This is file containing a solution for MIPT lecturer T.F. Khiryanov's course on Cracking Algoriths on Python, lab 5. Visualizing of model of the central gravity"""

import graphics as gr

SIZE_X = 600
SIZE_Y = 600

window = gr.GraphWin("Model", SIZE_X, SIZE_Y)

coords = gr.Point(300, 500)
velocity = gr.Point(2, 0)
acceleration = gr.Point(0, 0)


def add(point_1, point_2):
    new_point = gr.Point(point_1.x + point_2.x,
                         point_1.y + point_2.y)

    return new_point


def sub(point_1, point_2):
    new_point = gr.Point(point_1.x - point_2.x,
                         point_1.y - point_2.y)

    return new_point


def check_coords(coords, velocity):
    if coords.x < 0 or coords.x > SIZE_X:
        velocity.x = -velocity.x

    if coords.y < 0 or coords.y > SIZE_Y:
        velocity.y = -velocity.y


def update_coords(coords, velocity):
    return add(coords, velocity)


def update_velocity(velocity, acceleration):
    return add(velocity, acceleration)


def update_acceleration(ball_coords, center_coords):
    diff = sub(ball_coords, center_coords)
    distance_2 = (diff.x ** 2 + diff.y ** 2) ** (3/2)

    G = 2000

    return gr.Point(-diff.x*G/distance_2, -diff.y*G/distance_2)


rectangle = gr.Rectangle(gr.Point(0, 0), gr.Point(SIZE_X, SIZE_Y))
rectangle.setFill('green')
rectangle.draw(window)

sun = gr.Circle(gr.Point(300, 300), 40)
sun.setFill('yellow')
sun.draw(window)

circle = gr.Circle(coords, 10)
circle.setFill('red')
circle.draw(window)

while True:
    x_prev, y_prev = coords.x, coords.y
    acceleration = update_acceleration(coords, gr.Point(300, 300))
    coords = update_coords(coords, velocity)
    velocity = update_velocity(velocity, acceleration)
    check_coords(coords, velocity)
    circle.move(coords.x - x_prev, coords.y - y_prev)
    gr.time.sleep(0.03)


