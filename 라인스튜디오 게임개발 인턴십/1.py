from collections import deque
def solution(grid):
    d = [[-1,0],[1,0],[0,1],[0,-1]]
    visited = [[False]*len(grid[0]) for _ in range(len(grid))]
    Q = deque()
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x]==0:
                Q.append([y,x,0])
                visited[y][x] = True
    mini = 0
    while Q:
        y,x,before = Q.popleft()
        for dy,dx in d:
            ny,nx = y+dy,x+dx
            if -1<ny<len(grid) and -1<nx<len(grid[0]) and not visited[ny][nx]:
                mini = max(mini,before+1)
                grid[ny][nx] = before+1
                visited[ny][nx] = True
                Q.append([ny,nx,before+1])
    return mini

# print(solution(	[[0, 0, 1, 1, 1], [1, 0, 0, 1, 1], [0, 0, 0, 0, 1], [1, 1, 1, 1, 1], [0, 0, 1, 0, 1]]))
print(solution([[0, 1, 1, 1, 1], [1, 1, 1, 1, 1], [0, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]))