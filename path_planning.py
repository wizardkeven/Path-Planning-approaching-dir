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

cost = [3, 1, 2] # cost has 3 values, corresponding to making 
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
    value = [[999 for row in range(len(grid[0]))] for col in range(len(grid))]
    directions = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
    visited = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    # initialize directions and distance with starting point direction
    directions[init[0]][init[1]] = init[2]
    value[init[0]][init[1]] = 0
    visited[init[0]][init[1]] = 1

    # 0: go straight; 3: right turn; 1: left turn
    dir_diff = [3,0,1]
    
    change = True

    print ('grid')
    for gg in grid:
        print (gg)
    print()
    while change:
        change = False
               
        for x in range(len(grid)):
            for y in range(len(grid[0])):
            #     if goal[0] == x and goal[1] == y:
            #         if value[x][y] > 0:
            #             value[x][y] = 0
            #             policy2D[x][y] = '*'

            #             change = True

            #     el
                if grid[x][y] == 0:
                    
                    # suppose current possible forwarding
                    for cur_f in range(len(forward)):
                        # possible previous forwarding
                        x2 = x - forward[cur_f][0]
                        y2 = y - forward[cur_f][1]

                        if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x2][y2] == 0:
                            # if x ==0 and y ==4 and x2 == 0 and y == 3:
                            #     print
                            #     print 'x , y ==>             ('+str(x)+' , '+str(y)+')'
                            #     print 'cur_f ==>              '+str(forward_name[cur_f])
                            #     print 'Previous dir ==>      ('+str(x2)+' , '+str(y2)+') ==> '+str(directions[x2][y2])
                            m_dir_diff = (cur_f - directions[x2][y2] + 4)%4
                            # previous node should be the visited node with least cost to current node        
                            if directions[x2][y2] > -1 and m_dir_diff != 2:
                                pre_a = -1
                                # previous action is turn right
                                if m_dir_diff == 3:
                                    pre_a = 0
                                elif m_dir_diff == 0: # go staight
                                    pre_a = 1
                                else: # turn left
                                    pre_a = 2

                                v2 = value[x2][y2] + cost[pre_a]
                                # if x2 == 0 and y == 3:
                                #     print 'x2, y2 ==>            ('+str(x2)+' , '+str(y2)+')'
                                #     print 'v2 ==>                 '+str(v2)

                                if v2 < value[x][y]:
                                    change = True

                                    value[x][y] = v2
                                    if directions[x][y] < 0:
                                        directions[x][y] = cur_f
                                    else:
                                        directions[x][y] = [directions[x][y], cur_f]

                                    # print 'current value matrix:'
                                    # for vv in value:
                                    #     print vv
                                    # print
                                    # print 'current direction matrix:'
                                    # for dd in directions:
                                    #     print dd
                                    # print '\nAssign => directions['+str(x)+']['+str(y)+'] = '+str(cur_f)+'\n'

                                    # policy2D[x2][y2] = action_name[pre_a]
                            # if x ==0 and y in [3,4]:
                            #     print '============================================'
    
                # if goal[0] == x and goal[1] == y:
                #         #         if value[x][y] > 0:
                #         #             value[x][y] = 0
                #     policy2D[x][y] = '*'    
    
    current_node = init[:-1]

    while current_node != '':
       
        x, y = current_node

        current_node = ''

        if visited[x][y] > 2:
            print('impossible path at {} , {}'.format(x,y))
            continue
        
        print('x , y ==>'+str(x)+' , '+str(y))
        best_action = ""
        best_node = []
        min_diff = 99
        best_forward = -1
        for cur_f in range(len(forward)):
            # possible previous forwarding
            x2 = x + forward[cur_f][0]
            y2 = y + forward[cur_f][1]

            if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x2][y2] == 0 and value[x][y] < 999 and value[x2][y2] < 999:
                if visited[x2][y2] > 1:
                    continue
                if visited[x][y] == 2 and visited[x2][y2] >= 1:
                    print('Overlapping ==> {}, {}'.format(x2,y2))
                    continue
                print('\ndebug: x2 , y2 ==> '+str(x2)+' , '+str(y2))
                va_diff = abs(value[x2][y2] - value[x][y])
                print('va_diff ==> '+str(va_diff))

                m_dir_diff = (cur_f - directions[x][y] + 4)%4
                print('m_dir_diff ==> '+str(m_dir_diff))
                print('directions[{}][{}] = {}'.format(x,y,directions[x][y]))
                # previous node should be the visited node with least cost to current node        
                if directions[x][y] > -1 and m_dir_diff != 2:
                    cur_a = -1
                    # current action is turn right
                    if m_dir_diff == 3:
                        cur_a = 0
                    elif m_dir_diff == 0: # go staight
                        cur_a = 1
                    else: # turn left
                        cur_a = 2
                    
                    if va_diff < min_diff and va_diff >= 0:

                        min_diff = va_diff
                        best_action = action_name[cur_a]
                        best_forward = cur_f
                        best_node = [x2,y2]

        if min_diff < 99:
            policy2D[x][y] = best_action
            visited[best_node[0]][best_node[1]] += 1
            current_node = best_node
            directions[best_node[0]][best_node[1]] = best_forward
            print('\nChanged ==> min_diff: {}\tbest_action: {}\tbest_forward: {}\tbest_node: {}\tvisited[{}][{}]: {}'.format(min_diff,best_action,best_forward,best_node,best_node[0],best_node[1],visited[best_node[0]][best_node[1]]) )
        print('\n==============================================\n')
                        


    for i in range(len(value)):
        for j in range(len(value[0])):
            if value[i][j] == 999:
                value[i][j] = 0
    print ('value')
    for vv in value:
        print(vv)
    print()
    print ('directions')
    for dd in directions:
        print (dd)
    print()

    return policy2D

p2 = optimum_policy2D(grid,init,goal,cost)

for p in p2:
    print(p)