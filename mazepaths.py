import random
import array
import numpy as np

def main():
    w = getValidInput("What is the width of the maze? ",4,30)
    h = getValidInput("What is the height of the maze? ",4,30)
    Maze = [[[0,0,0,0] for x in range(w)] for y in range(h)]
    #print(np.matrix(Maze))
    #print('\n'.join([''.join(['{:4}'.format(printelement(pos)) for pos in row]) for row in Maze]))
    print('\n'.join(''.join(printelement(row)) for row in Maze))



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

def printelement(v):
    return "x"


main()
