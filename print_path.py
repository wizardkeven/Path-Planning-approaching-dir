# -----------
# User Instructions:
#
# Modify the the search function so that it returns
# a shortest path as follows:
# 
# [['>', 'v', ' ', ' ', ' ', ' '],
#  [' ', '>', '>', '>', '>', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', '*']]
#
# Where '>', '<', '^', and 'v' refer to right, left, 
# up, and down motions. Note that the 'v' should be 
# lowercase. '*' should mark the goal cell.
#
# You may assume that all test cases for this function
# will have a path from init to goal.
# ----------

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    # ----------------------------------------
    # modify code below
    # ----------------------------------------
    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed[init[0]][init[1]] = 1
    
    expand1 = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]
    step =0
    expand = [[' ' for col in range(len(grid[0]))] for row in range(len(grid))]

    x = init[0]
    y = init[1]
    g = 0

    open = [[g, x, y]]

    found = False  # flag that is set when search is complete
    resign = False # flag set if we can't find expand

    while not found and not resign:
        if len(open) == 0:
            resign = True
            return 'fail'
        else:
            open.sort()
            open.reverse()
            next = open.pop()
            x = next[1]
            y = next[2]
            g = next[0]
            expand1[x][y] = step
            step+=1
            if x == goal[0] and y == goal[1]:
                found = True
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            open.append([g2, x2, y2])
                            closed[x2][y2] = 1
    
    if expand1[goal[0]][goal[1]] <= 0:
        return expand
    print
    for ll in expand1:
        print(ll)
    print('\n======================================\n')
        
    step_back = expand1[goal[0]][goal[1]]
    xb = goal[0]
    yb = goal[1]
    sh_pa_found = False
    ccc = 0
    while(not sh_pa_found):
        for i in range(len(delta)):
            x3 = xb + delta[i][0]
            y3 = yb + delta[i][1]
            if x3 == init[0] and y3 == init[1]:
                sh_pa_found = True
            if x3 >= 0 and x3 < len(grid) and y3 >=0 and y3 < len(grid[0]):
                if expand1[x3][y3] >= 0 and expand[x3][y3] == ' ':
                    if expand1[x3][y3] < step_back:
                        expand[x3][y3] = delta_name[(i+2)%4]
                        if xb == goal[0] and yb == goal[1]:
                            expand[xb][yb] = '*'
                        xb = x3
                        yb = y3
                        step_back = expand1[x3][y3]
                        # print("found back step: "+str(x3)+" ' "+str(y3))
        # ccc+=1
        # if ccc > 20:
        #     break
        
    return expand # make sure you return the shortest path
    
ex = search(grid,init,goal,cost)
for ll in ex:
    print(ll)
