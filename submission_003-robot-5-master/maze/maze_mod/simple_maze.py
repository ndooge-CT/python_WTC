
import random
import math
print("Imported simple_maze successfully")
obstacles_ls = []
co_ord = []
maze_id = ""
door_ls = []
min_y, max_y = -200, 200
min_x, max_x = -100, 100


def set_obstacles(obs_ls):
    obstacles_ls = obs_ls


def get_doors():
    global door_ls
    return door_ls


def create_random_maze():
    global obstacles_ls, co_ord, door_ls
    co_ord = []
    obstacles_ls = []

    start_x = -90
    end_x = 90
    start_y = -190
    end_y = 186

    levels = 6

    for i in range(levels):
        create_h_line(start_x, end_x, end_y)
        create_h_line(start_x, end_x, start_y)
        create_v_line(start_y, end_y, start_x)
        create_v_line(start_y, end_y, end_x - 4)

        start_x += 14
        end_x -= 14
        start_y += 14
        end_y -= 14
    # for doos in door_ls:
        # print(doos)


def create_h_line(start_x, end_x, end_y):
    door = random.randrange(start_x + 4, end_x - 8, 4)
    doos = (door, end_y)
    door_ls.append(doos)
    #print(f"h-line door {door}")
    for i in range(start_x, end_x, 4):
        if i == door or i == door + 4:
            continue
        else:
            point = (i, end_y)
            obstacles_ls.append(point)
    # print(obstacles_ls)


def create_v_line(start_y, end_y, start_x):
    door = random.randrange(start_y + 4, end_y - 8, 4)
    #print(f"h-line door {door}")
    doos = (start_x, door)
    door_ls.append(doos)
    for i in range(start_y, end_y, 4):
        if i == door or i == door + 4:
            continue
        else:
            point = (start_x, i)
            obstacles_ls.append(point)
    # print(obstacles_ls)


def get_boundaries():
    global min_y, max_y, min_x, max_x
    return min_y, min_x, max_y, max_x


def generate_obstacles():
    global obstacles_ls
    create_random_maze()
    return obstacles_ls


def set_border():
    global min_x, max_x, min_y, max_y
    return min_x, max_x, min_y, max_y


def is_position_blocked(x, y):
    global obstacles_ls

    for my_tuple in obstacles_ls:
        if (my_tuple[0]) <= x <= (my_tuple[0] + 4) and (my_tuple[1]) <= y <= (my_tuple[1]+4):
            return True
    return False


def set_obstacles(obs_local_to_set):
    global obstacles_ls
    obstacles_ls = obs_local_to_set


def is_path_blocked(x1, y1, x2, y2):
    global obstacles_ls

    x_range = 0
    x_path_test = 0
    y_range = 0
    # generate_obstacles()
    #obstacles_ls = generate_obstacles()

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
