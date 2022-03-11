from collections import deque
tmpright = [[1,1,2,2],[1,1,2,2],[2,2,1,1],[2,2,1,1]]
right = 0
for y in range(4):
    for x in range(4):
        if tmpright[y][x]==1:
            right = right | 1<<(4*y+x)

d = [(0,1),(0,-1),(1,0),(-1,0)]

def counting(grid):
    cnt = 0
    grid = right ^ grid
    for y in range(16):
        if grid & 1<<y:
            cnt+=1
    return cnt

def move(board,y,x,i):
    board2 = board
    tmp = 1<<(4*y+x)
    tmp2 = 0
    dy,dx = d[i]
    for now in range(1,3):
        ny,nx = y+dy*now,x+dx*now
        tmp2 = board2 & 1<<(4*ny+nx)
        board2 = board2 | tmp
        tmp = tmp2
    board2 = board2 | tmp
    return board2




#0000 0000 0000 0000
def solution(grid):
    Q = deque
    answer = 99999999
    tmpgrid = 0
    for y in range(4):
        for x in range(4):
            if grid[y][x] ==1:
                tmpgrid = tmpgrid|1<<(4*y+x)
    Q.append([0,tmpgrid])
    visited = [False for _ in range(1<<16)]



    while Q:
        dis, board = Q.popleft()
        if counting(board)==0:
            return dis
        elif not visited[board]:
            for y in range(4):
                nextBoard = move(board,y,0,0)
                nextCnt = counting(nextBoard)


print(solution([[1,1,1,1],[2,1,2,2],[2,2,2,1],[1,1,2,2]]))