import sys
from collections import deque
input = sys.stdin.readline


d = [[-1,0],[1,0],[0,-1],[0,1]]

def bfs(sx,sy):
    Q = deque([[sx,sy]])
    while Q:
        x,y = Q.popleft()
        if not visited[y][x]:
            visited[y][x] = True
            for dy,dx in d:
                ny,nx = y+dy,x+dx
                if -1<ny<N and -1<nx<M and board[ny][nx]:
                    Q.append([nx,ny])


T = int(input())
for i in range(T):
    M, N, K = map(int,input().split())
    
    board = [[0]*M for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    for j in range(K):
        X,Y = map(int,input().split())
        board[Y][X] = 1
    
    cnt = 0
    for y in range(N):
        for x in range(M):
            if not visited[y][x] and board[y][x]:
                cnt+=1
                bfs(x,y)
    print(cnt)
    
