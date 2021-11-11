import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
dots = []
for i in range(4):
    x,y = list(map(int,input().split()))
    dots.append([y,x])
a1,a2,b1,b2 = dots

d = [[1,0],[-1,0],[0,1],[0,-1]]
visited = [[[False]*4]*(N+1) for _ in range(M+1)]
route
Q = deque()
Q.append(a1)

while Q:
    y,x = Q.popleft()
    for i,dy,dx in enumerate(d):
        ny,nx = y+dy, x+dx
        if i==0: t= 1
        elif i==1: t= 0
        elif i==2: t=3
        elif i==3: t=4
        if -1<ny<M+1 and -1<nx<N+1 and not visited[ny][nx][t]:
            visited[y][x][i] = True
            visited[ny][nx][t] = True
            Q.append([ny,nx])


print(visited)
