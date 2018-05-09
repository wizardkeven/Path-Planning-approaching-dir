# ----------
# User Instructions:
# 
# Write a function optimum_policy that returns
# a grid which shows the optimum policy for robot
# motion. This means there should be an optimum
# direction associated with each navigable cell from
# which the goal can be reached.
# 
# Unnavigable cells as well as cells from which 
# the goal cannot be reached should have a string 
# containing a single space (' '), as shown in the 
# previous video. The goal cell should have '*'.
# ----------

grid = [[1, 1, 1, 0, 0, 0],# 0
        [1, 1, 1, 0, 1, 0],# 1
        [0, 0, 0, 0, 0, 0],# 2
        [1, 1, 1, 0, 1, 1],# 3
        [1, 1, 1, 0, 1, 1]]# 4
init = [4, 3]
goal = [2, 0]
cost = 1 # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def optimum_policy(grid,goal,cost):
    # ----------------------------------------
    # modify code below
    # ----------------------------------------
    expand1 = [[99 for row in range(len(grid[0]))] for col in range(len(grid))]
    policy = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    action = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
    change = True

    while change:
        change = False

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if goal[0] == x and goal[1] == y:
                    if expand1[x][y] > 0:
                        expand1[x][y] = 0

                        change = True

                elif grid[x][y] == 0:
                    for a in range(len(delta)):
                        x2 = x + delta[a][0]
                        y2 = y + delta[a][1]

                        if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x2][y2] == 0:
                            v2 = expand1[x2][y2] + cost

                            if v2 < expand1[x][y]:
                                change = True
                                expand1[x][y] = v2
    for vv in expand1:
        print(vv)
    print("================================\n")

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
                if expand1[x3][y3] >= 0 and policy[x3][y3] == ' ':
                    if expand1[x3][y3] < step_back:
                        policy[x3][y3] = delta_name[(i+2)%4]
                        if xb == goal[0] and yb == goal[1]:
                            policy[xb][yb] = '*'
                        xb = x3
                        yb = y3
                        step_back = expand1[x3][y3]

    return policy
    
po = optimum_policy(grid,goal,cost)

for p in po:
    print(p)
