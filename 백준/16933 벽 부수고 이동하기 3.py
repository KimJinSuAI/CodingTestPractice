import sys
from collections import deque
input = sys.stdin.readline
N,M,K = map(int,input().split())

board = []
for i in range(N):
    board.append(input()[:-1])
visited = [[[0]*(K+1) for _ in range(M)] for n in range(N)]
visited[0][0] = [1]*(K+1)


def bfs():
    d = [[-1,0],[1,0],[0,-1],[0,1]]
    Q = deque()
    Q.append([0,0,0])
    day = 1

    while Q:
        x,y,wall = Q.popleft()
        for dy,dx in d:
            ny,nx = y+dy,x+dx
            if -1<ny<N and -1<nx<M and not visited[y][x][wall]:
                if board[ny][nx]=='0':
                    Q.append([dis+1,nx,ny,k,nextday])
                elif k:
                    if day==0:
                        Q.append([dis+1,nx,ny,k-1, 1])
                    else:
                        Q.append([dis+2,nx,ny,k-1, 1])
                    
if visited[-1][-1]==0:
    print(-1)
else:
    print(visited[-1][-1])