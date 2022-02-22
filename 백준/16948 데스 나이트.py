import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
r1,c1,r2,c2 = list(map(int,input().split()))
d = [[-2,-1],[-2,1],[0,-2],[0,2],[2,-1],[2,1]]

def bfs():
    visited = [[False for i in range(N)] for j in range(N)]

    Q = deque([(0,r1,c1)])
    while Q:
        dis,y,x = Q.popleft()
        if [y,x] ==[r2,c2]:
            return dis
        if not visited[y][x]:
            visited[y][x] = True
            for dy,dx in d:
                ny,nx = y+dy,x+dx
                if -1<ny<N and -1<nx<N and not visited[ny][nx]:
                    Q.append((dis+1,ny,nx))
    return -1
print(bfs())