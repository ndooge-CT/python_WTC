def move_square(size): #moves in a square
    
    print("Moving in a square of size "+str(size))
    for i in range(4):
        degrees = 90
        print("* Move Forward "+str(size))
        print("* Turn Right "+str(degrees)+" degrees")

def move_rectangle(length, width): #moves in a rectangle. 
   # length = 20
    #width = 10
    print("Moving in a rectangle of "+str(length)+" by "+str(width))
    for i in range(2):
        degrees = 90
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")
        print("* Move Forward "+str(width))
        print("* Turn Right "+str(degrees)+" degrees")

def move_circle(): #moves in a circle. 
    print("Moving in a circle")
    degrees = 1
    for i in range(360):
        length = 1
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")

def move_square_dancing(length): 
    print("Square dancing - 3 squares of size 20")
    for i in range(3):
        print("* Move Forward "+str(length))
        move_square(length)

def move_crop_circle(length):
    print("Crop circles - 4 circles")
    for i in range(4):
        print("* Move Forward "+str(length))
        move_circle()

def move(): #calls all the different move patterns. 
    size = 10
    length = 20
    width = 10
    move_square(size)
    move_rectangle(length,width)
    move_circle()
    #size = 20
    move_square_dancing(length)
    
    move_crop_circle(length)
    
def move_patterns():
    move()
# TODO: Decompose into functions
def robot_start():
    move_patterns() 
    
if __name__ == "__main__":
    robot_start()
