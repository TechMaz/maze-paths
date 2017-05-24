import random
import array
import numpy as np

def main():
    w = getValidInput("What is the width of the maze? ",4,30)
    h = getValidInput("What is the height of the maze? ",4,30)
    Maze = [[[1,1,1,1] for x in range(w)] for y in range(h)]
    i = 0
    j = 0
    for j in range(h):
        for i in range(w):
            Maze[j][i] = [getrandtop(Maze,j,i),
                          getrandleft(Maze,j,i),
                          getrandright(Maze,j,i,w),
                          getrandbottom(Maze,j,i,h)]
            i = i + 1
        j = j + 1
    #print(np.matrix(Maze))
    #print('\n'.join([''.join(['{:4}'.format(printelement(pos)) for pos in row]) for row in Maze]))
    j = 0
    for row in Maze:
        print printrow(Maze,row,j,w,h)
        j=j+1


def getValidInput(prompt,min,max):
    val = raw_input(prompt)
    if(isInt(val)):
        if(int(val) <= max):
            if(int(val) >= min):
                return int(val)
            else:
                print "Oops that's too small, try a larger number!"
                return getValidInput(prompt,min,max)
        else:
            print "Oops that's too big, try a smaller number!"
            return getValidInput(prompt,min,max)
    else:
        print "Oops that's not a valid integer!"
        return getValidInput(prompt,min,max)

def isInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def printrow(Maze,row,j,w,h):
    this_row = ""

    if(j == 0):
        i = 0
        for pos in row:
            if(pos[0] == 1):
                if(i == 0):
                    this_row = this_row + "+--+"
                else:
                    this_row = this_row + "--+"
            else:
                this_row = this_row + "   "
            i = i + 1
        this_row = this_row + '\n'

    i = 0
    for pos in row:
        if(i == 0):
            if(pos[1] == 1):
                this_row = this_row + "|"
            else:
                this_row = this_row + " "

        if(pos[2] == 1):
            this_row = this_row + "  |"
        else:
            this_row = this_row + "   "
        i = i+1
    this_row = this_row + '\n'

    i = 0
    for pos in row:
        if(pos[3] == 1):
            if(i == 0):
                this_row = this_row + "+--+"
            elif((i < w-1) & (j < h-1)):
                if((Maze[j][i][2] == 0) & (Maze[j+1][i][2] == 0) & (Maze[j][i+1][3] == 0) & (Maze[j][i-1][3] == 0)):
                    this_row = this_row + "---"
                else:
                    this_row = this_row + "--+"
            else:
                this_row = this_row + "--+"
        else:
            if(i == 0):
                if((Maze[j][i][2] == 1) | (Maze[j+1][i][2] == 1) | (Maze[j][i+1][3] == 1)):
                    this_row = this_row + "+  +"
                else:
                    this_row = this_row + "+   "
            elif(i >= (w-1)):
                this_row = this_row + "  +"
            elif((Maze[j][i][2] == 1) | (Maze[j+1][i][2] == 1)):
                this_row = this_row + "  +"
            else:
                this_row = this_row + "   "
        i = i + 1
    return this_row

def getrandtop(Maze,j,i):
    if(j == 0):
        return 1
    else:
        if(Maze[j-1][i][3] == 1):
            return 1
        else:
            return random.randint(0, 1)

def getrandbottom(Maze,j,i,h):
    if(j == h-1):
        return 1
    else:
        return random.randint(0, 1)

def getrandleft(Maze,j,i):
    if(i == 0):
        return 1
    else:
        return random.randint(0, 1)

def getrandright(Maze,j,i,w):
    if(i >= w-1):
        return 1
    else:
        return random.randint(0, 1)

main()
