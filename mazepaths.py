import random
import array
import numpy as np

def main():
    w = getValidInput("What is the width of the maze? ",4,30)
    h = getValidInput("What is the height of the maze? ",4,30)
    Maze = [[[1,1,1,1] for x in range(w)] for y in range(h)]
    end = getrandend(w,h)
    print "Exit at: " + str(end)

    make_maze(Maze,w,h,end)
    print_maze(Maze,w,h,end)

    '''
    j = 0
    i = 0
    while (j <= w-1):
        while (i <= h-1):
            print "Check position [" + str(j) + ", " + str(i) + "] : " + str(Maze[j][i])
            print str(doespathexist(Maze,j,i,w,h,end)) + '\n'
            i = i+1
        j = j+1
    '''


def make_maze(Maze,w,h,end):
    needs_another_pass = True
    while(needs_another_pass == True):
        needs_another_pass = False
        j = 0
        i = 0
        for j in range(h):
            for i in range(w):
                Maze[j][i] = get_element(Maze,j,i,w,h,end)
                #needs_another_pass = try_random_edge(Maze,j,i,w,h,end)
                i = i + 1
            j = j + 1

def try_random_edge(Maze,j,i,w,h,end):
    return False

def get_element(Maze,j,i,w,h,end):
    return [getrandtop(Maze,j,i,end),
            getrandleft(Maze,j,i,end),
            getrandright(Maze,j,i,w,end),
            getrandbottom(Maze,j,i,h,end)]

def getrandtop(Maze,j,i,end):
    if(end == [j,i]):
        return 0
    else:
        if(j == 0):
            return 1
        else:
            if(Maze[j-1][i][3] == 1):
                return 1
            else:
                return random.randint(0, 1)

def getrandbottom(Maze,j,i,h,end):
    if(end == [j,i]):
        return 0
    else:
        if(j == h-1):
            return 1
        else:
            return random.randint(0, 1)

def getrandleft(Maze,j,i,end):
    if(end == [j,i]):
        return 0
    else:
        if(i == 0):
            return 1
        else:
            return random.randint(0, 1)

def getrandright(Maze,j,i,w,end):
    if(end == [j,i]):
        return 0
    else:
        if(i >= w-1):
            return 1
        else:
            return random.randint(0, 1)

def getrandend(w,h):
    opt = random.randint(0, 3)
    if(opt == 0):
        return [random.randint(0, h-1), w-1]
    elif(opt == 1):
        return [random.randint(0, h-1), 0]
    elif(opt == 2):
        return [h-1, random.randint(0, w-1)]
    else:
        return [0, random.randint(0, w-1)]

def doespathexist(Maze,j,i,w,h,end):
    c = 0
    last = None
    pos = [j,i]
    while(end != pos):
        if (pos == None):
            return False
        elif(c > (w*h)):
            return False
        j = pos[0]
        i = pos[1]
        pos = move(Maze,j,i,w,h,set([0,1,2,3]),last,end)
        last = [j,i]
        if(pos != None):
            print "moved [" + str(last[0]) + ", " + str(last[1]) + "] --> [" + str(pos[0]) + ", " + str(pos[1]) + "]"
        else:
            return False
        c = c+1
    return True

def move(Maze,j_curr,i_curr,w,h,rem,last,end):
    if(len(rem) == 0):
        return None
    elif(len(rem) == 1):
        dir = random.randint(0, len(rem) - 1)
        if(dir == 0):
            if (Maze[j_curr][i_curr][0] == 1):
                return None
        elif(dir == 1):
            if (Maze[j_curr][i_curr][1] == 1):
                return None
        elif(dir == 2):
            if (Maze[j_curr][i_curr][2] == 1):
                return None
        else:
            if (Maze[j_curr][i_curr][3] == 1):
                return None
    else:
        dir = random.randint(0, len(rem) - 1)
        rem_array =  np.array([item for item in rem])
        if(rem_array[dir] == 0):
            if ((Maze[j_curr][i_curr][0] == 0) & (j_curr-1 >= 0)):
                if (last == [j_curr-1,i_curr]):
                    return move(Maze,j_curr,i_curr,w,h,rem.difference([0]),last,end)
                else:
                    return [j_curr-1,i_curr]
            else:
                return move(Maze,j_curr,i_curr,w,h,rem.difference([0]),last,end)
        elif(rem_array[dir] == 1):
            if ((Maze[j_curr][i_curr][1] == 0) & (i_curr-1 >= 0)):
                if (last == [j_curr,i_curr-1]):
                    return move(Maze,j_curr,i_curr,w,h,rem.difference([1]),last,end)
                else:
                    return [j_curr,i_curr-1]
            else:
                return move(Maze,j_curr,i_curr,w,h,rem.difference([1]),last,end)
        elif(rem_array[dir] == 2):
            if ((Maze[j_curr][i_curr][2] == 0) & (i_curr+1 <= w-1)):
                if(last == [j_curr,i_curr+1]):
                    return move(Maze,j_curr,i_curr,w,h,rem.difference([2]),last,end)
                else:
                    return [j_curr,i_curr+1]
            else:
                return move(Maze,j_curr,i_curr,w,h,rem.difference([2]),last,end)
        else:
            if ((Maze[j_curr][i_curr][3] == 0) & (j_curr+1 <= h-1)):
                if (last == [j_curr+1,i_curr]):
                    return move(Maze,j_curr,i_curr,w,h,rem.difference([3]),last,end)
                else:
                    return [j_curr+1,i_curr]
            else:
                return move(Maze,j_curr,i_curr,w,h,rem.difference([3]),last,end)


# Printing of Maze:

def print_maze(Maze,w,h,end): #loops through each row in maze and calls print_row()
    j = 0
    col_nums = ""
    p = 0
    while(p < w):
        col = " " + str(p) + "  "
        col_nums = col_nums + str(col[0:3])
        p = p+1
    print col_nums
    for row in Maze:
        print print_row(Maze,row,j,w,h,end)
        j=j+1
    #print(np.matrix(Maze))
    #print('\n'.join([''.join(['{:4}'.format(printelement(pos)) for pos in row]) for row in Maze]))

def print_row(Maze,row,j,w,h,end):  #code to format printing of each row in maze
    this_row = ""

    #this_row = this_row + "    "
    if(j == 0):
        i = 0
        for pos in row:
            if(pos[0] == 1):
                if(end == [j,i]):
                    if(i == 0):
                        this_row = this_row + "+  +"
                    else:
                        this_row = this_row + "  +"
                else:
                    if(i == 0):
                        this_row = this_row + "+--+"
                    else:
                        this_row = this_row + "--+"
            else:
                this_row = this_row + "   "
            i = i + 1
        this_row = this_row + '\n'

    #col = str(j) + "    "
    #this_row = this_row + str(col[0:4])
    i = 0
    for pos in row:
        if(i == 0):
            if(pos[1] == 1):
                if(end == [j,i]):
                    this_row = this_row + " "
                else:
                    this_row = this_row + "|"
            else:
                this_row = this_row + " "

        if(end == [j,i]):
            if(pos[2] == 1):
                if(j == w-1):
                    this_row = this_row + "<> "
                else:
                    this_row = this_row + "<>|"
            else:
                this_row = this_row + "<> "
        else:
            if(pos[2] == 1):
                this_row = this_row + "  |"
            else:
                this_row = this_row + "   "
        i = i+1
    this_row = this_row + " " + str(j) + '\n'

    #this_row = this_row + "    "
    i = 0
    for pos in row:
        if(pos[3] == 1):
            if(i == 0):
                if(end == [j,i]):
                    this_row = this_row + "+  +"
                else:
                    this_row = this_row + "+--+"
            elif((i < w-1) & (j < h-1)):
                if((Maze[j][i][2] == 0) & (Maze[j][i][1] == 0) & (Maze[j+1][i][2] == 0) & (Maze[j][i+1][3] == 0) & (Maze[j][i-1][3] == 0)):
                    this_row = this_row + "---"
                else:
                    this_row = this_row + "--+"
            else:
                if(end == [j,i]):
                    this_row = this_row + "  +"
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
            elif(((j+1) <= (w-1)) & ((Maze[j][i][2] == 1) | (Maze[j+1][i][2] == 1))):
                this_row = this_row + "  +"
            else:
                this_row = this_row + "   "
        i = i + 1
    return this_row

# Helper functions:

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

main()
