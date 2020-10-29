import sys
import turtle
import robot


screen = turtle.Screen()
min_y, max_y = -200, 200
min_x, max_x = -100, 100
screen.setup(800, 1200)
screen.title('Toy Robot')
screen.setworldcoordinates(min_x, min_y, max_x, max_y)
screen_x, screen_y = screen.screensize()
t = turtle.Turtle()
t.speed(0)

obstacles_ls = [()]
# variables tracking position and direction
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0

def is_edge():
    global position_x, position_y, min_x, max_x, min_y, max_y
    if position_y == max_y: #TOP EDGE / BOUNDARY
        return True, "top"
    if position_x == min_x: #LEFT BOUND
        return True, "left"
    if position_y == min_y: #BOTTOM
        return True, "bottom"
    if position_x == max_x: #RIGHT
        return True, "right"

def turn_left():
    turtle.left(90)


def turn_right():
    turtle.right(90)


def set_direction(setter_current_direction_index):
    global current_direction_index
    current_direction_index = setter_current_direction_index


def get_direction_index():
    global current_direction_index
    return current_direction_index


def show_position(robot_name):
    print(' > '+robot_name+' now at position (' +
          str(position_x)+','+str(position_y)+').')


def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """

    return min_x <= new_x <= max_x and min_y <= new_y <= max_y


def update_position(steps):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    """

    global position_x, position_y, current_direction_index, directions, obstacles_ls, maze_choice

    new_x = position_x
    new_y = position_y

    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps

    elif directions[current_direction_index] == 'right':
        new_x = new_x + steps

    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps

    elif directions[current_direction_index] == 'left':
        new_x = new_x - steps

    if is_position_allowed(new_x, new_y) and (robot.obstacles.is_path_blocked(position_x, position_y, new_x, new_y) == False):
        position_x = new_x
        position_y = new_y
        turtle.forward(steps)
        turtle.position()
        return True
    elif is_position_allowed(new_x, new_y) == False and (robot.obstacles.is_path_blocked(position_x, position_y, new_x, new_y) == False):
        return "boundary"
    elif (robot.obstacles.is_path_blocked(position_x, position_y, new_x, new_y) == True):
        return "found"

    return False


def border(t, screen_x, screen_y):
    """(Turtle, int, int)

    Draws a border around the canvas in red.
    """
    # Lift the pen and move the turtle to the center.
    t.penup()
    t.home()

    # Move to lower left corner of the screen; leaves the turtle
    # facing west.
    t.forward(screen_x / 2)
    t.right(90)
    t.forward(screen_y / 2)
    t.setheading(180)           # t.right(90) would also work.

    # Draw the border
    t.pencolor('red')
    t.pendown()
    t.pensize(10)
    for distance in (screen_x, screen_y, screen_x, screen_y):
        t.forward(distance)
        t.right(90)

    # Raise the pen and move the turtle home again; it's a good idea
    # to leave the turtle in a known state.
    t.penup()
    t.home()
    t.seth(90)


def draw_obstacles(obstacles_ls):
    t.speed(0)
    t.penup()
    t.color("black")
    t._tracer(False)

    for co_ord in obstacles_ls:
        t.penup()
        t.goto(co_ord[0], co_ord[1])
        t.begin_fill()
        t.goto(co_ord[0], co_ord[1] + 4)
        t.goto(co_ord[0] + 4, co_ord[1] + 4)
        t.goto(co_ord[0] + 4, co_ord[1])
        t.goto(co_ord[0], co_ord[1])
        t.end_fill()
    t._tracer(True)
    t.home()


def draw_grid():
    global min_x, min_y, max_y, max_x
    min_y, min_x, max_y, max_x = obstacles.get_boundaries()
    x_ind = min_x
    y_ind = min_y

    x_range = max_x - min_x
    y_range = max_y - min_y

    t.pencolor('red')
    t.penup()
    t.goto(min_x, min_y)
    t.pendown()
    t.pensize()
    t.left(90)
    while x_ind <= max_x:
        t.pendown()
        t.forward(x_range)
        x_ind += 4
        t.penup()
        t.goto(x_ind, min_y)
    t.penup()
    t.goto(min_x, min_y)
    t.right(90)
    while y_ind <= max_y:
        t.pendown()
        t.forward(y_range)
        t.penup()
        y_ind += 4
        t.goto(min_x, y_ind)
    # t.penup()
    t.home()


def draw_border():
    global min_x, min_y, max_x, max_y

    t.penup()  # LHS vert line
    t.goto(min_x, min_y)
    t.pendown()
    t.color("red")
    t.begin_fill()
    t.goto(min_x, max_y)
    t.goto(min_x + 2, max_y)
    t.goto(min_x+2, min_y)
    t.penup()
    t.end_fill()

    t.penup()  # RHS vert line
    t.goto(max_x - 2, min_y)
    t.pendown()
    t.color("red")
    t.begin_fill()
    t.goto(max_x - 2, max_y)
    t.goto(max_x, max_y)
    t.goto(max_x, min_y)
    t.penup()
    t.end_fill()

    t.penup()  # B Hor line
    t.goto(min_x, min_y)
    t.pendown()
    t.color("red")
    t.begin_fill()
    t.goto(max_x, min_y)
    t.goto(max_x + 2, min_y + 2)
    t.goto(min_x, min_y + 2)
    t.penup()
    t.end_fill()

    t.penup()  # T Hor line
    t.goto(min_x, max_y - 2)
    t.pendown()
    t.color("red")
    t.begin_fill()
    t.goto(max_x, max_y - 2)
    t.goto(max_x, max_y)
    t.goto(min_x, max_y)
    t.penup()
    t.end_fill()


def start_world():
    #border(t, screen_x, screen_y)
    global obstacles_ls, position_x, position_y, current_direction_index, min_y, min_x, max_x, max_y, maze_choice

    draw_border()
    obstacles_ls = robot.obstacles.generate_obstacles()
    min_y, min_x, max_y, max_x = robot.obstacles.get_boundaries()

    screen.setworldcoordinates(min_x, min_y, max_x, max_y)
    draw_obstacles(obstacles_ls)
    screen_x, screen_y = screen.screensize()

    position_x = 0
    position_y = 0
    current_direction_index = 0
    turtle.left(90)


def close_turtle():
    turtle.bye()


def get_limits():
    global min_x, min_y, max_x, max_y
    return min_x, min_y, max_x, max_y


def get_position():
    global position_x, position_y
    return position_x, position_y


def get_obs():
    global obstacles_ls
    return obstacles_ls
