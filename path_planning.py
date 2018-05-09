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

cost = [2, 1, 20] # cost has 3 values, corresponding to making 
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
print
print 'cost: '+'L'+' # '+'R'
print '    '+str(cost)
print
def optimum_policy2D(grid,init,goal,cost):
    # output grid
    policy2D = [[' ' for x in range(len(grid[0]))] for y in range(len(grid))]
    value = [[999 for row in range(len(grid[0]))] for col in range(len(grid))]
    directions = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
    # initialize directions and distance with starting point direction
    directions[init[0]][init[1]] = init[2]
    value[init[0]][init[1]] = 0
    # open_list = [init]
    # trajectory = [init]
    
    change = True

    print 'grid'
    for gg in grid:
        print gg
    print
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
                    for i in range(len(action)):
                        return_action = action[i] # get possible action return to previous state 1,0,-1 corresponding to previously turned left(-1), go straight(0) and turn right(1)
                        cur_f = (directions[x][y] - back_action + 4)%4 # get previous direction
                        x2 = x + forward[cur_f][0]
                        y2 = y + forward[cur_f][1]

                        if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x2][y2] == 0:
                            if x ==0 and y ==4 and x2 == 0 and y == 3:
                                print
                                print 'x , y ==>             ('+str(x)+' , '+str(y)+')'
                                print 'pre_a ==>              '+str(action_name[pre_a])
                                print 'cur_f ==>              '+str(forward_name[cur_f])
                                print 'Previous dir ==>      ('+str(x2)+' , '+str(y2)+') ==> '+str(directions[x2][y2])

                            if directions[x2][y2] > -1:
                                v2 = value[x2][y2] + cost[pre_a]
                                if x2 == 0 and y == 3:
                                    print 'x2, y2 ==>            ('+str(x2)+' , '+str(y2)+')'
                                    print 'v2 ==>                 '+str(v2)

                                if v2 < value[x][y]:
                                    change = True

                                    value[x][y] = v2
                                    directions[x][y] = (directions[x2][y2] - pre_a + 4)%4
                                    print 'current value matrix:'
                                    for vv in value:
                                        print vv
                                    print
                                    print 'current direction matrix:'
                                    for dd in directions:
                                        print dd
                                    print '\nAssign => directions['+str(x)+']['+str(y)+'] = '+str(cur_f)+'\n'

                                    policy2D[x2][y2] = action_name[i]
                            if x ==0 and y in [3,4]:
                                print '============================================'
    
                if goal[0] == x and goal[1] == y:
                        #         if value[x][y] > 0:
                        #             value[x][y] = 0
                    policy2D[x][y] = '*'    
    for i in range(len(value)):
        for j in range(len(value[0])):
            if value[i][j] == 999:
                value[i][j] = 0
    print 'value'
    for vv in value:
        print(vv)
    print
    print 'directions'
    for dd in directions:
        print dd
    print

    return policy2D

p2 = optimum_policy2D(grid,init,goal,cost)

for p in p2:
    print(p)