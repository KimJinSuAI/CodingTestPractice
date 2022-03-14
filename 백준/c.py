from collections import deque
def solution(width, height, diagonals):
    answer = 0
    board = [[0 for x in range(width+1)] for y in range(height+1)]
    digs = [[[] for x in range(width+1)] for y in range(height+1)]
    visited = [[False for x in range(width+1)] for y in range(height+1)]
    for dx,dy in diagonals:
        digs[dy-1][dx].append(1)
        digs[dy][dx-1].append(2)
    
    Q = deque([(0,0,0)])
    d = [(1,0),[-1,0],[0,1],[0,-1]]
    while Q:
        y,x,cnt = Q.pop()
        if not visited[y][x]:
            for dy,dx in d:
            dy,dx = 
            Q.append((y,x))
    return answer%10000019
print(solution())