import robot
import obstacles
import turtle

#import world.obstacles
import sys
from world import obstacles
sys.path.append('/homes/ndooge/problems/submission_002-robot-4/world/')
screen = turtle.Screen()
screen.setup(500, 500)
screen.title('Toy Robot')
screen_x, screen_y = screen.screensize()
t = turtle.Turtle()
t.speed(0)


obstacles_ls = [()]
# variables tracking position and direction
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0

# area limit vars
min_y, max_y = -148, 148
min_x, max_x = -198, 198


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

    global position_x, position_y, current_direction_index, directions, obstacles_ls, mutant
    obstacles_ls = robot.get_obstacles_ls()
    #print (f"world position{obstacles_ls}")
    obstacles.set_obstacles(obstacles_ls)
    new_x = position_x
    new_y = position_y

    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
       # mutant.forward(steps)
       # mutant.position()
    elif directions[current_direction_index] == 'right':
        new_x = new_x + steps
        # mutant.forward(steps)
       # mutant.position()
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
        # mutant.forward(steps)
        # mutant.position()
    elif directions[current_direction_index] == 'left':
        new_x = new_x - steps
        # mutant.forward(steps)
        # mutant.position()
    #obstacles_ls = obstacles.get_obstacles()

    if is_position_allowed(new_x, new_y) and (obstacles.is_path_blocked(position_x, position_y, new_x, new_y) == False):
        position_x = new_x
        position_y = new_y
        turtle.forward(steps)
        turtle.position()
        return True
    elif is_position_allowed(new_x, new_y) == False and (obstacles.is_path_blocked(position_x, position_y, new_x, new_y) == False):
        return "boundary"
    elif (obstacles.is_path_blocked(position_x, position_y, new_x, new_y) == True):
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

    for obs in obstacles_ls:
        #print (f" x-coord {obs[0]} y-coord {obs[1]}")
        t.pencolor('red')
        t.goto(obs[0], obs[1])
        t.pendown()
        t.pensize(1)
        t.forward(4)
        t.left(90)
        t.forward(4)
        t.left(90)
        t.forward(4)
        t.left(90)
        t.forward(4)
        t.penup()
        t.home()


def start_world():
    border(t, screen_x, screen_y)
    global obstacles_ls, position_x, position_y, current_direction_index
    obstacles_ls = [()]
    obstacles_ls = obstacles.generate_obstacles()

    #obstacles_ls = obstacles.get_obstacles()
    draw_obstacles(obstacles_ls)
    # variables tracking position and direction
    position_x = 0
    position_y = 0
    #directions = ['forward', 'right', 'back', 'left']
    current_direction_index = 0
    # Uncomment to draw the graphics as quickly as possible.
    # t.speed(0)
    # Draw a border around the canvas

    # draw stuff with mutant_ninja_turtle_robot.forward, .right, .circle, etc
    turtle.left(90)


def close_turtle():
    turtle.bye()
