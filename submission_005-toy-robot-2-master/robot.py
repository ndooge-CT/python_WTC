direction = 'up'

def get_name():
    name = input("What do you want to name your robot? ")
    return name

def greet_child(name):
    print(f"{name}: Hello kiddo!")

def get_command(name):
    command = input(f"{name}: What must I do next? ")
    return command

def get_command_list():
    commands_list = ['off','help','forward', 'back','right','left','sprint']
    return commands_list
def valid_command(command):
    command_list = get_command_list()
    if command.lower() in command_list:
        return True
    else:
        return False

def perform_command(command_ls,name,position):
    
    #print (command_ls)
    if command_ls[0].lower() == 'off':
        shutdown(name)
    if command_ls[0].lower() == 'help':
        help_list_command = help_menu()
        print_help(help_list_command)

    if command_ls[0].lower() == 'forward':
        move_forward(name,command_ls[1],position)
    if command_ls[0].lower() == 'back':
        move_back(name,command_ls[1],position)
    
    if command_ls[0].lower() == 'right':
        move_right(name,position)
    if command_ls[0].lower() == 'left':
        move_left(name,position)
    if command_ls[0].lower() == 'sprint':
        robo_sprint(name, position,command_ls[1])

def move_forward(name,distance,position):
    global direction

    if direction == 'up':
        check_range_y = position[1] + int(distance)
        if check_range_y > -200 and check_range_y < 200:
            print(f" > {name} moved forward by {distance} steps.")
            position[1] += int(distance)
           # print(f"{name} now at position: {position}")
        else:
            print(f"{name}: Sorry, I cannot go outside my safe zone.")
    elif direction == 'down':
        check_range_y = position[1] - int(distance)
        if check_range_y > -200 and check_range_y < 200:
            print(f" > {name} moved forward by {distance} steps.")
            position[1] -= int(distance)
           # print(f"{name} now at position: {position}")
        else:
            print(f"{name}: Sorry, I cannot go outside my safe zone.")
    elif direction == 'right':
        check_range_x = position[0] + int(distance)
        if check_range_x > -100 and check_range_x < 100:
            print(f" > {name} moved forward by {distance} steps.")
            position[0] += int(distance)
          #  print(f"{name} now at position: {position}")
        else:
            print(f"{name}: Sorry, I cannot go outside my safe zone.")
    elif direction == 'left':
        check_range_x = position[0] - int(distance)
        if check_range_x > -100 and check_range_x < 100:
            print(f" > {name} moved forward by {distance} steps.")
            position[0] -= int(distance)
           # print(f"{name} now at position: {position}")
        else:
            print(f"{name}: Sorry, I cannot go outside my safe zone.")
    

def move_back(name, distance, position):
    global direction
    
    if direction == 'up':
        check_range_y = position[1] - int(distance)
        if check_range_y > -200 and check_range_y < 200:
            print(f" > {name} moved back by {distance} steps.")
            position[1] -= int(distance)
            #print(f"{name} now at position: {position}")
        else:
            print(f"{name}: Sorry, I cannot go outside my safe zone.")
    elif direction == 'down':
        check_range_y = position[1] + int(distance)
        if check_range_y > -200 and check_range_y < 200:
            print(f" > {name} moved back by {distance} steps.")
            position[1] += int(distance)
            #print(f"{name} now at back: {position}")
        else:
            print(f"{name}: Sorry, I cannot go outside my safe zone.")
    elif direction == 'right':
        check_range_x = position[0] - int(distance)
        if check_range_x > -100 and check_range_x < 100:
            print(f" > {name} moved back by {distance} steps.")
            position[0] -= int(distance)
            #print(f"{name} now at position: {position}")
        else: 
            print(f"{name}: Sorry, I cannot go outside my safe zone.")
    
    elif direction == 'left':
        check_range_x = position[0] + int(distance)
        if check_range_x > -100 and check_range_x < 100:
            print(f" > {name} moved back by {distance} steps.")
            position[0] += int(distance)
            #print(f"{name} now at position: {position}")   
        else:
            print(f"{name}: Sorry, I cannot go outside my safe zone.")
    
def move_right(name, position):
    global direction
    print(f" > {name} turned right.")
    
    
    if direction == 'up':
        direction = 'right'
    elif direction == 'right':
        direction = 'down'
    elif direction == 'down':
        direction = 'left'
    elif direction == 'left':
        direction = 'up'

def robo_sprint(name, position, distance):
    gogo = int(distance)
    
    while gogo > 0:
        move_forward(name, gogo,position)
        gogo -= 1
        
def move_left(name, position):
    global direction
    print(f" > {name} turned left.")
    
    
    if direction == 'up':
        direction = 'left'
    elif direction == 'right':
        direction = 'up'
    elif direction == 'down':
        direction = 'right'
    elif direction == 'left':
        direction = 'down'
def shutdown(name):
    print(f"{name}: Shutting down..")

def help_menu():
    help_list_command = ["OFF - Shut down robot", "HELP - provide information about commands"]
    #'FOWARD x- move robot forward x steps',
   # 'BACK x - move robot back x steps', 'RIGHT - turn robot 90degrees right', 'LEFT - turn robot 90deg left', 
    #'SPRINT x- robot sprints x steps, then x-1 until x = 0']

    return help_list_command

def print_help(help_list_command):
    #print(help_list_command)
    for i in help_list_command:
        print(i)

def robot_start():
    """This is the entry function, do not change"""
    name = get_name()
    greet_child(name)
    position = [0,0]
    run = True
    #direction = 'up'
    while run == True: 
        try:
            command = get_command(name)
            command_ls = command.split()
            if valid_command(command_ls[0]) == True:
                perform_command(command_ls,name,position)          
                if not ((command_ls[0].lower() == 'off') or (command_ls[0].lower() == 'help')):
                    print(f" > {name} now at position (", end= "")
                    print(*position,sep = ",",end=").\n")
                if command_ls[0].lower() == 'off':
                    run = False
                    break
            
            elif valid_command(command_ls[0]) == False:
                print(f"{name}: Sorry, I did not understand '{command}'.")
        except (EOFError):
            break
    pass


if __name__ == "__main__":
    robot_start()
