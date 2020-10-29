

# TODO: Step 1 - get shape (it can't be blank and must be a valid shape!)
def get_shape():
    shape = input("Shape?: ")
    while shape.lower() not in ["pyramid", "square", "triangle", "diamond", "rhombus"]:
        shape = input("Shape?: ")
    return shape.lower()
    

# TODO: Step 1 - get height (it must be int!)
def get_height():
    height = input("Height?: ")
    if height.isdigit():
        if int(height) > 80 or int(height) < 1:
            return get_height()
        else:
            return (int(height))
    else:
        return get_height()
        

# TODO: Step 2
def draw_pyramid(height, outline):
    h = 1
    l = 1
    if outline == True:
        for h in range(height):
            for l in range(height-1-h):
                print(' ', end='') # printing space required and staying in same line
            for l in range(2*h+1):
                if l==0 or l==2*h or h==height-1:
                    print('*',end='')
                else:
                    print(' ', end='')
            print("\n", end="") # printing new line    
    elif outline == False:
        for i in range(height):
            for j in range(height-1-i):
                print(' ', end='') # printing space required and staying in same line

            for j in range(2*i+1):
                print('*',end='') # printing * and staying in same line
            print("\n", end="") # printing new line
    
# TODO: Step 3
def draw_square(height, outline):
    h = 0
    l = 0
    if outline == True:
        while h < height:
            l = 0
            if (h == 0 or (h == (height - 1)) ):
                while l < height:
                    print('*', end = "")
                    l = l + 1
            else:
                while l < height:
                    if (l == 0 or (l == (height - 1))):
                        print('*', end = "")
                    else:
                        print(" ", end = "")
                    l = l + 1
            print("\n", end="")
            h = h + 1    
    elif outline == False:
        while h < height:
            l = 0
            while l < height:
                print('*', end = "")
                l = l +1
            print("\n", end="")
            h = h + 1
    
# TODO: Step 4
def draw_triangle(height, outline):
    h = 0

    l = 1
    if outline == True:
        for h in range(height):
            for l in range(h+1):
                if l==0 or l==h or h==height-1:
                     print('*',end="")
                else:
                     print(" ", end="")
            print("\n",end="")
    elif outline == False:
        while (h < height):
            l = 0
            while (l < h):
                print("*", end="")
                l = l + 1
            h = h + 1
            print ("*")
        
def draw_diamond(height, outline):

    if outline == True:
        for i in range(1, height+1):
            for j in range(1, height-i+1):
                print(" ", end="")      
            for j in range(1, 2*i):
                if j == 1 or j == 2*i-1:
                    print("*",end="")
                else:
                    print(" ",end="")
            print()
        for i in range(height-1,0,-1):
            for j in range(1,height-i+1):
                print(" ",end="")
            for j in range(1,2*i):
                if j==1 or j==2*i-1:
                    print("*",end="")
                else:
                    print(" ",end="")
            print()
    
    elif outline == False:
                # Upper part of diamond
        for i in range(1, height+1):
            for j in range(1,height-i+1):
                print(" ",end="")
            for j in range(1, 2*i):
                print("*", end="")
            print()
        for i in range(height-1,0,-1):
            for j in range(1, height-i+1):
                print(" ", end="")
            for j in range(1, 2*i):
                print("*", end="")
            print()

def draw_rhombus(height, outline):

    if outline == True:
        for i in range(1,height +1):
            for j in range(1, height - i +1):
                print(end=" ")
            if i == 1 or i == height:
                for j in range(1, height + 1):
                    print("*",end="")
            else:
                for j in range(1, height+1):
                    if(j == 1 or j == height):
                        print("*",end="")
                    else:
                        print(end=" ")
            print()

    elif outline == False:
        for i in range(1, height +1):
            for j in range(1, height - i +1):
                print(end=" ")
            for j in range(1, height +1):
                print("*",end="")
            print()    


# TODO: Steps 2 to 4, 6 - add support for other shapes
def draw(shape, height, outline):
    if shape_param.lower() == "pyramid":
        draw_pyramid(height_param,outline)
    elif shape_param.lower() == "square":
        draw_square(height_param,outline)
    elif shape_param.lower() == "triangle":
        draw_triangle(height_param,outline)
    elif shape_param.lower() == "diamond":
        draw_diamond(height_param,outline)
    elif shape_param.lower() == "rhombus":
        draw_rhombus(height_param,outline)
    

# TODO: Step 5 - get input from user to draw outline or solid
def get_outline():
    outline = input("Outline? Y\\N? \n")
    if outline == 'Y' or outline == 'y':
        return True
    elif outline == 'N' or outline == 'n':
        return False
    


if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    draw(shape_param, height_param, outline_param)

