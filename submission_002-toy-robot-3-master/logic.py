def replay_history(robot_name):
    global history
    global replay
    global silent

    replay = True
    count = 0
    for command in history:
        #print (command)
        if command != "replay" and command != "help" and command != "history" and command != "replay silent":
            handle_command(robot_name,command)
            count += 1
    replay = False
    if silent == False:
        return True, ' > '+robot_name+' replayed '+str(count)+' commands.'
    elif silent == True: 
        return True, ' > '+robot_name+' replayed '+str(count)+' commands silently.'

def rev_replay_history(robot_name):
    global history
    global replay
    global silent

    replay = True
    count = 0
    for command in reversed(history):
        #print (command)
        if command != "replay" and command != "help" and command != "history" and command != "replay silent" and command != "replay reversed" and command != "replay reversed silent":
            handle_command(robot_name,command)
            count += 1
    replay = False
    if silent == False:
        return True, ' > '+robot_name+' replayed '+str(count)+' commands.'
    elif silent == True: 
        return True, ' > '+robot_name+' replayed '+str(count)+' commands silently.'

def n_replay_history(robot_name, n_steps):
    global history
    global replay
    global silent
    n_steps += 1
    replay = True
    count = 0
    for command in history[-n_steps:-1]:
        #print (command)
        if command != "replay" and command != "help" and command != "history" and command != "replay silent":
            handle_command(robot_name,command)
            
            count += 1
    replay = False
    if silent == False:
        return True, ' > '+robot_name+' replayed '+str(count)+' commands.'
    elif silent == True: 
        return True, ' > '+robot_name+' replayed '+str(count)+' commands silently.'

def r_rev_replay_history(robot_name, n_steps):
    global history
    global replay
    global silent
    #n_steps += 1
    replay = True
    count = 0
    for command in history[-2:-2-n_steps:-1]:
        #print (list(command))
        #print(len(list(command)))
        #if len(list(command) > 2):
        if (len(command.split()) > 3):
            print (command.split()) 
        if command != "replay" and command != "help" and command != "history" and command != "replay silent":
            #print (command)
            handle_command(robot_name,command)
            count += 1
    replay = False
    if silent == False:
        return True, ' > '+robot_name+' replayed '+str(count)+' commands.'
    elif silent == True: 
        return True, ' > '+robot_name+' replayed '+str(count)+' commands silently.'

#def n_m_replay_history(robot_name, n_steps,):


        
        
       # if arg == "reversed" or arg == "reversed silent":
          # (do_next, command_output) = rev_replay_history(robot_name)
       # elif command_name == 'replay' and (not is_int(arg) or arg == "silent"):
          # (do_next, command_output) = replay_history(robot_name)


          def replay_history(robot_name):
    global history
    global replay
    global silent

    replay = True
    count = 0
    for command in history:
        #print (command)
        if command != "replay" and command != "help" and command != "history" and command != "replay silent":
            handle_command(robot_name,command)
            count += 1
    replay = False
    if silent == False:
        return True, ' > '+robot_name+' replayed '+str(count)+' commands.'
    elif silent == True: 
        return True, ' > '+robot_name+' replayed '+str(count)+' commands silently.'

def rev_replay_history(robot_name):
    global history
    global replay
    global silent

    replay = True
    count = 0
    for command in reversed(history):
        #print (command)
        if command != "replay" and command != "help" and command != "history" and command != "replay silent" and command != "replay reversed" and command != "replay reversed silent":
            handle_command(robot_name,command)
            count += 1
    replay = False
    if silent == False:
        return True, ' > '+robot_name+' replayed '+str(count)+' commands.'
    elif silent == True: 
        return True, ' > '+robot_name+' replayed '+str(count)+' commands silently.'

def n_replay_history(robot_name, n_steps):
    global history
    global replay
    global silent
    n_steps += 1
    replay = True
    count = 0
    for command in history[-n_steps:-1]:
        #print (command)
        if command != "replay" and command != "help" and command != "history" and command != "replay silent":
            handle_command(robot_name,command)
            
            count += 1
    replay = False
    if silent == False:
        return True, ' > '+robot_name+' replayed '+str(count)+' commands.'
    elif silent == True: 
        return True, ' > '+robot_name+' replayed '+str(count)+' commands silently.'

def r_rev_replay_history(robot_name, n_steps):
    global history
    global replay
    global silent
    replay = True
    count = 0
    for command in history[-2:-2-n_steps:-1]:
        if command != "replay" and command != "help" and command != "history" and command != "replay silent":
            handle_command(robot_name,command)
            count += 1
    replay = False
    if silent == False:
        return True, ' > '+robot_name+' replayed '+str(count)+' commands.'
    elif silent == True: 
        return True, ' > '+robot_name+' replayed '+str(count)+' commands silently.'

def nm_replay_history(robot_name,n_steps, m_steps):
    global history
    global replay
    global silent
    n_steps += 1
    m_steps += 1
    replay = True
    count = 0
    for command in history[-n_steps:-m_steps:]:
        #print (command)
        if command != "replay" and command != "help" and command != "history" and command != "replay silent":
            handle_command(robot_name,command)
            count += 1
    replay = False
    if silent == False:
        return True, ' > '+robot_name+' replayed '+str(count)+' commands.'
    elif silent == True: 
        return True, ' > '+robot_name+' replayed '+str(count)+' commands silently.'
