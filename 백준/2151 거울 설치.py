import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
house = []
for i in range(N):
    house.append(input()[:-1])

doors = []
for y in range(N):
    for x in range(N):
        if house[y][x]=='#':
            doors.append([y,x])

d = {0:[-1,0], 1:[1,0],2:[0,-1],3:[0,1]}
visited = [[[sys.maxsize] * 4 for _ in range(N)] for _ in range(N)]
Q = deque()
ans  = sys.maxsize

y,x = doors[0]
for key in d.keys():
    dy,dx = d[key]
    ny,nx = y+dy, x+dx
    if -1<ny<N and -1<nx<N and house[ny][nx]!='*':
        Q.append([0,key,ny,nx])

while Q:
    c,dir,y,x = Q.popleft()
    if [y,x]==doors[1]:
        ans = min(ans,c)
    elif visited[y][x][dir]>c:
        visited[y][x][dir] = c
        if house[y][x] == '.':
            dy,dx = d[dir]
            ny,nx = y+dy,x+dx
            if -1<ny<N and -1<nx<N and house[ny][nx]!='*':
                Q.append([c,dir,ny,nx])
        elif house[y][x] == '!':
            tmpy, tmpx = d[dir]
            for key in d.keys():
                dy,dx = d[key]
                if tmpy*dy==-1 or tmpx*dx==-1: continue #반대방향 무시
                ny,nx = y+dy, x+dx
                nextC = c
                if key != dir: 
                    nextC+=1
                if -1<ny<N and -1<nx<N and house[ny][nx]!='*':
                    Q.append([nextC,key,ny,nx])
print(ans)