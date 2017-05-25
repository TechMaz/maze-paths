import random
import array
import numpy as np

def main():
    w = getValidInput("What is the width of the maze? ",4,30)
    h = getValidInput("What is the height of the maze? ",4,30)
    Maze = [[[1,1,1,1] for x in range(w)] for y in range(h)]
    end = getrandend(w,h)
    print "Exit at: " + str(end) + " indicated by <>"

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
    Edges = get_shuffle(Maze,w,h)
    needs_another_pass = True
    step_count = 0
    while(needs_another_pass == True):
        needs_another_pass = False
        for e in Edges:
            #print "[ " + str(e[0]) + ", " + str(e[1]) + ", " + str(e[2]) + "]"
            needs_another_pass = try_rand_edge(Maze,e[0],e[1],e[2],w,h,end)
        if (step_count > 1):
            break
        step_count = step_count + 1

'''
        j = 0
        i = 0
        for j in range(h):
            for i in range(w):
                Maze[j][i] = get_element(Maze,j,i,w,h,end)
                i = i + 1
            j = j + 1
'''

def get_shuffle(Maze,w,h):
    Edges = [[y,x,e] for x in range(w) for y in range(h) for e in range(4)]
    #print str(Edges)
    random.shuffle(Edges)
    random.shuffle(Edges)
    #print "\n"
    #print "Edges = " + str(Edges)
    return Edges

'''
def try_random_edge(Maze,j,i,w,h,end):
    if(j == 0):
        if (i = 0):
            return try_rand_edge(Maze,j,i,w,h,end,[2,3])
        elif (i == w-1):
            return try_rand_edge(Maze,j,i,w,h,end,[0,2])
        else:
            return try_rand_edge(Maze,j,i,w,h,end,[0,2,3])
    elif (j == h-1):
        if (i = 0):
            return try_rand_edge(Maze,j,i,w,h,end,[1,3])
        elif (i == w-1):
            return try_rand_edge(Maze,j,i,w,h,end,[0,1])
        else:
            return try_rand_edge(Maze,j,i,w,h,end,[0,1,3])
    else:
        if (i = 0):
            return try_rand_edge(Maze,j,i,w,h,end,[1,2,3])
        elif (i == w-1):
            return try_rand_edge(Maze,j,i,w,h,end,[0,1,2])
        else:
            return try_rand_edge(Maze,j,i,w,h,end,[0,1,2,3])
'''

def try_rand_edge(Maze,j,i,edge,w,h,end):
    #num_pos_edges = len(edges)
    #if(num_pos_edges == 0):
    #    return False
    #else:
    if (edge == 0):
        return attempt_merge(Maze,j,i,j-1,i,w,h,edge)
    elif (edge == 1):
        return attempt_merge(Maze,j,i,j,i-1,w,h,edge)
    elif (edge == 2):
        return attempt_merge(Maze,j,i,j,i+1,w,h,edge)
    else:
        return attempt_merge(Maze,j,i,j+1,i,w,h,edge)

def attempt_merge(Maze,j,i,k,l,w,h,orig_edge):
    if (is_valid_pos(k,l,w,h)):
        if(divided_by_edge(Maze,j,i,k,l,w,h,orig_edge)):
            if(did_merge(Maze,j,i,k,l,w,h,orig_edge)):
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def is_valid_pos(j,i,w,h):
    if ((j < 0) | (j > h-1)):
        return False
    if ((i < 0) | (i > w-1)):
        return False
    return True

def divided_by_edge(Maze,j1,i1,j2,i2,w,h,orig_edge):
    if (orig_edge == 0):
        #print "check [" + str(j1) + "," + str(i1) + "] edge 0 and [" + str(j2) + "," + str(i2) + "] edge 3"
        if ((Maze[j1][i1][0] == 1) | (Maze[j2][i2][3] == 1)):
            return True
        else:
            return False
    elif (orig_edge == 1):
        #print "check [" + str(j1) + "," + str(i1) + "] edge 1 and [" + str(j2) + "," + str(i2) + "] edge 2"
        if ((Maze[j1][i1][1] == 1) | (Maze[j2][i2][2] == 1)):
            return True
        else:
            return False
    elif (orig_edge == 2):
        #print "check [" + str(j1) + "," + str(i1) + "] edge 2 and [" + str(j2) + "," + str(i2) + "] edge 1"
        if ((Maze[j1][i1][2] == 1) | (Maze[j2][i2][1] == 1)):
            return True
        else:
            return False
    else:
        #print "check [" + str(j1) + "," + str(i1) + "] edge 3 and [" + str(j2) + "," + str(i2) + "] edge 0"
        if ((Maze[j1][i1][3] == 1) | (Maze[j2][i2][0] == 1)):
            return True
        else:
            return False

def did_merge(Maze,j1,i1,j2,i2,w,h,orig_edge):
    if (exists_path_between(Maze,j1,i1,j2,i2,w,h) == False):
        if (orig_edge == 0):
            Maze[j1][i1][0] = 0
            Maze[j2][i2][3] = 0
        elif (orig_edge == 1):
            Maze[j1][i1][1] = 0
            Maze[j2][i2][2] = 0
        elif (orig_edge == 2):
            Maze[j1][i1][2] = 0
            Maze[j2][i2][1] = 0
        else:
            Maze[j1][i1][3] = 0
            Maze[j2][i2][0] = 0
        #print "merged [" + str(j1) + "," + str(i1) + "] and [" + str(j2) + "," + str(i2) + "]"
        return True
    else:
        return False

def exists_path_between(Maze,j1,i1,j2,i2,w,h):
    reachable = list()
    reachable.append([j2,i2])
    last = [j2,i2]
    find_reachable(reachable,Maze,j2,i2,w,h)
    return ([j1,i1] in reachable)

def find_reachable(reachable,Maze,j,i,w,h):
    check_reachable(reachable,Maze,j,i,j-1,i,w,h,0)
    check_reachable(reachable,Maze,j,i,j,i-1,w,h,1)
    check_reachable(reachable,Maze,j,i,j,i+1,w,h,2)
    check_reachable(reachable,Maze,j,i,j+1,i,w,h,3)


def check_reachable(reachable,Maze,j,i,k,l,w,h,orig_edge):
    if(is_valid_pos(k,l,w,h)):
        if(divided_by_edge(Maze,j,i,k,l,w,h,orig_edge) == False):
            if(in_list(reachable,[k,l]) == False):
                reachable.append([k,l])
                find_reachable(reachable,Maze,k,l,w,h)

def in_list(l,item):
    if (item in l):
        return True
    else:
        return False

'''
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
            continue
            #print "moved [" + str(last[0]) + ", " + str(last[1]) + "] --> [" + str(pos[0]) + ", " + str(pos[1]) + "]"
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
'''

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
