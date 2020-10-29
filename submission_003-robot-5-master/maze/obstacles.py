
import random
import math
print("Imported obstacles by default")
#from text import world as world
obstacles_ls = []

min_y, max_y = -200, 200
min_x, max_x = -100, 100


def set_obstacles(obs_ls):
    obstacles_ls = obs_ls


def get_boundaries():
    global min_y, min_x, max_y, max_x
    return min_y, min_x, max_y, max_x


def generate_obstacles():
    global obstacles_ls
    obstacles_ls = []
    rand_range = random.randint(0, 10)
    obstacles_ls = [(random.randint(min_x, max_x), random.randint(min_y, max_y))
                    for i in range(rand_range)]
    return obstacles_ls


def is_position_blocked(x, y):
    global obstacles_ls

    for my_tuple in obstacles_ls:
        if (my_tuple[0]) <= x <= (my_tuple[0] + 4) and (my_tuple[1]) <= y(my_tuple[1]+4):
            return True
    return False


def is_path_blocked(x1, y1, x2, y2):
    global obstacles_ls
    # x1 = -20 -> 10 y= 0 path
    # x1 = -14 -> -10 & y = -2 -> 2 obstacle
    # x1 = origin x2 = destination
    # y1 origin y2 dest
    x_range = 0
    x_path_test = 0
    y_range = 0
    # generate_obstacles()
    obstacles_ls_local = get_obstacles()
    #print (f"obstacle_ls in is path possible {obstacles_ls_local}")
    #print (f"obstacle_ls in is path possible {obstacles_ls}")
    # obstacles.set_obstacles(obstacles_ls_local)
    #direction_index = world.get_direction_index()
    if y1 == y2:
        #forward / backward
        # x range 10 - (-20) = 30
        if x1 > x2:  # moving back
            x_range = x1 - x2
            for x_path_test in range(x2, x1 + 1):
                #print (x_path_test)
                for my_tuple in obstacles_ls:
                    #print (my_tuple)
                    if ((my_tuple[0]) <= x_path_test <= (my_tuple[0] + 4)) and ((my_tuple[1]) <= y1 <= (my_tuple[1] + 4)):
                        return True
            return False
        elif x2 >= x1:  # moving forward
            x_range = x2 - x1
            for x_path_test in range(x1, x2+1):
                #print (x_path_test)
                for my_tuple in obstacles_ls:
                    #print (my_tuple)
                    if ((my_tuple[0]) <= x_path_test <= (my_tuple[0] + 4)) and ((my_tuple[1]) <= y1 <= (my_tuple[1] + 4)):
                        #print (f"Blocked at x{x_path_test}")
                        return True
        return False
    if x1 == x2:
        #up /down
        if y1 > y2:  # moving down
            y_range = y1 - y2
            for y_path_test in range(y2, y1 + 1):
                #print (y_path_test)
                for my_tuple in obstacles_ls:
                    #print (my_tuple)
                    if ((my_tuple[1]) <= y_path_test <= (my_tuple[1] + 4)) and ((my_tuple[0]) <= x1 <= (my_tuple[0] + 4)):
                        #print(f"blocked at y{y_path_test}")
                        return True
            return False
        elif y2 >= y1:  # moving up
            y_range = y2 - y1
            for y_path_test in range(y1, y2+1):
                #print (y_path_test)
                for my_tuple in obstacles_ls:
                    #print (my_tuple)
                    if ((my_tuple[1]) <= y_path_test <= (my_tuple[1] + 4)) and ((my_tuple[0]) <= x1 <= (my_tuple[0] + 4)):
                        #print (f"Blocked at y{y_path_test}")
                        return True
            return False

    return True


def get_obstacles():
    global obstacles_ls
    return obstacles_ls
