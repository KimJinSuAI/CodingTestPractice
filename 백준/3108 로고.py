import sys
from collections import deque
input = sys.stdin.readline

N = int(input()[:-1])
rects = []
board = [[0]*2001 for _ in range(2001)]
visited = [[0]*2001 for _ in range(2001)]
start = []
for i in range(N):
    x1,y1,x2,y2 = list(map(int,input()[:-1].split()))
    x1+=500;y1+=500;x2+=500;y2+=500
    x1*=2;y1*=2;x2*=2;y2*=2

    for j in range(x1,x2+1):
        board[j][y1],board[j][y2] = 1,1
    for j in range(y1,y2+1):
        board[x1][j],board[x2][j] = 1,1
    start.append([x1,y1])
    
d = [[1,0],[-1,0],[0,1],[0,-1]]

def bfs(x,y):
    Q = deque([[x,y]])
    while Q:
        nx,ny = Q.popleft()
        if visited[nx][ny]==0:
            visited[nx][ny] = 1
            for dx,dy in d:
                nnx = nx + dx
                nny = ny+dy
                if -1<nnx<2001 and -1<nny<2001 and board[nnx][nny] == 1 and visited[nnx][nny]==0:
                    Q.append([nnx,nny])

ans = 0
for x,y in start:
    if visited[x][y]==0:
        ans+=1
        bfs(x,y)
if visited[1000][1000]==1:
    ans-=1
print(ans)
