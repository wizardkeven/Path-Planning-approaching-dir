# ----------
# User Instructions:
# 
# Implement the function optimum_policy2D below.
#
# You are given a car in grid with initial state
# init. Your task is to compute and return the car's 
# optimal path to the position specified in goal; 
# the costs for each motion are as defined in cost.
#
# There are four motion directions: up, left, down, and right.
# Increasing the index in this array corresponds to making a
# a left turn, and decreasing the index corresponds to making a 
# right turn.

forward = [[-1,  0], # go up
           [ 0, -1], # go left
           [ 1,  0], # go down
           [ 0,  1]] # go right
forward_name = ['up', 'left', 'down', 'right']

# action has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']

# EXAMPLE INPUTS:
# grid format:
#     0 = navigable space
#     1 = unnavigable space 
       # 0  1  2  3  4  5
grid = [[1, 1, 1, 0, 0, 0],# 0
        [1, 1, 1, 0, 1, 0],# 1
        [0, 0, 0, 0, 0, 0],# 2
        [1, 1, 1, 0, 1, 1],# 3
        [1, 1, 1, 0, 1, 1]]# 4

init = [4, 3, 0] # given in the form [row,col,direction]
                 # direction = 0: up
                 #             1: left
                 #             2: down
                 #             3: right
                
goal = [2, 0] # given in the form [row,col]

cost = [2, 1, 15] # cost has 3 values, corresponding to making 
                  # a right turn, no turn, and a left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D with the given parameters should return 
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
# ----------

# ----------------------------------------
# modify code below
# ----------------------------------------

# f(x,y) = min(f(x2,y2) + cost_action(i))
# print
# print 'cost: '+'L'+' # '+'R'
# print '    '+str(cost)
# print
def optimum_policy2D(grid,init,goal,cost):
    # output grid
    policy2D = [[' ' for x in range(len(grid[0]))] for y in range(len(grid))]
    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    expand1 = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]
    directions = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
    step =0
    # initialize directions and distance with starting point direction
    directions[init[0]][init[1]] = init[2]
    closed[init[0]][init[1]] = 1

    x = init[0]
    y = init[1]
    g = 0
    f = init[2]

    open = [[g, x, y, f]]
    print(cost)
    found = False  # flag that is set when search is complete
    resign = False # flag set if we can't find expand
    pre_ff = -1
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
            f = next[3]
            if pre_ff > 0:
                dd_f = f - pre_ff
            if closed[x][y] == 1:
                expand1[x][y] = g
                directions[x][y] = f
            elif closed[x][y] == 2:
                step_m = [expand1[x][y],g]
                dir_m = [directions[x][y],f]
                if expand1[x][y] < 0:
                    closed[x][y] -=1
                    step_m = g
                    dir_m = f

                expand1[x][y] = step_m
                directions[x][y] = dir_m

            elif closed[x][y] >= 3:
                step_m = expand1[x][y] + g
                dir_m = directions[x][y] + f
                expand1[x][y] = step_m
                directions[x][y] = dir_m

            step+=1
            if x == goal[0] and y == goal[1]:
                found = True
            else:
                for f2 in range(len(forward)):

                    x2 = x + forward[f2][0]
                    y2 = y + forward[f2][1]

                    if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                        
                        if grid[x2][y2] == 0:
                            m_dir_diff = (f2 - f + 4)%4
                            # previous node should be the visited node with least cost to current node        
                            if m_dir_diff != 2:
                                pre_a = -1
                                # previous action is turn right
                                if m_dir_diff == 3:
                                    pre_a = 0
                                elif m_dir_diff == 0: # go staight
                                    pre_a = 1
                                else: # turn left
                                    pre_a = 2
                                g2 = g + cost[pre_a]
                                # if x == 2 and y <= 3:
                                # print('\n({} , {}) ==> ({} , {}), closed ==> {}, g2 ==> {}'.format(x,y,x2,y2,closed[x2][y2],g2))
                                # print('\nopen')
                                # print(open)
                                #     for ex in expand1:
                                #         print(ex)
                                #     print()
                                # if closed[x2][y2] < 2:
                                open.append([g2, x2, y2, f2])
                                closed[x2][y2] += 1
            # print('\n====================================================\n')
    print("expand1")
    for ex in expand1:
        print(ex)
    print("\nclosed")
    for cl in closed:
        print(cl)
    print("\ndirections")
    for di in directions:
        print(di)
    print()
    back_node = goal
    end = False

    while back_node != '' and not end:

        x, y = back_node
        back_node = ''

        if x == init[1] and y == init[2]:
            end = True
        else:
            min_exp_diff = 99
            pre_f = -1
            pre_x = x
            pre_y = y
            pre_it = -1
            need_del = False

            for f2 in range(len(forward)):
                x2 = x + forward[f2][0]
                y2 = y + forward[f2][1]

                if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]) and grid[x2][y2] == 0 and closed[x2][y2] > 0:
                    exp_diff = min_exp_diff
                    if closed[x2][y2] == 1:
                        need_del = False
                        exp_diff = expand1[x][y] - expand1[x2][y2]
                        if expand1[x][y] > expand1[x2][y2] and exp_diff < min_exp_diff:
                            min_exp_diff = exp_diff          
                            pre_x = x2
                            pre_y = y2
                    else:
                        need_del = True

                        for ite in range(closed[x2][y2]):

                            if expand1[x][y] > expand1[x2][y2][ite]:

                                exp_diff = expand1[x][y] - expand1[x2][y2][ite]

                                if exp_diff < min_exp_diff:

                                    min_exp_diff = exp_diff          
                                    pre_it = ite
                                    pre_x = x2
                                    pre_y = y2

            if min_exp_diff >= 99:
                print('fail to proceed at ({}, {}) ==> ({}, {})'.format(x,y,x2,y2))
                continue
            else:
                if closed[pre_x][pre_y] > 1:
                    del expand1[x2][y2][pre_it]
                    del directions[x2][y2][pre_it]

                    if len(expand1[x2][y2]) == 1:
                        expand1[x2][y2] = expand1[x2][y2][0]

                    if len(directions[x2][y2]) == 1:
                        directions[x2][y2] = directions[x2][y2][0]
                else:
                    closed[pre_x][pre_y] -= 1
            
            f_diff = (directions[x][y] - directions[pre_x][pre_y] + 4)%4

            # if goal[0] == x and goal[1] == y:
            #     policy2D[x][y] = '*'
            #     policy2D[pre_x][pre_y] = action_name[1]
            # else:
            # previous node should be the visited node with least cost to current node        
            if f_diff != 2:
                pre_a = -1
                # previous action is turn right
                if f_diff == 3:
                    pre_a = 0
                elif f_diff == 0: # go staight
                    pre_a = 1
                else: # turn left
                    pre_a = 2
                policy2D[pre_x][pre_y] = action_name[pre_a]
                back_node = [pre_x, pre_y]

    return policy2D

p2 = optimum_policy2D(grid,init,goal,cost)

for p in p2:
    print(p)