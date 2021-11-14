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

def bfs(a1,a2,b1,b2):
    visited = [[False]*(N+1) for _ in range(M+1)]
    move = [[[-1,-1]] *(N+1) for _ in range(M+1)]
    Q = deque()
    Q.append([a1[0],a1[1],-1,-1])

    while Q:
        y,x,by,bx= Q.popleft()
        if not visited[y][x]:
            visited[y][x] = True
            move[y][x] = [by,bx]
            if [y,x] == a2:
                break
            for dy,dx in d:
                ny,nx = y+dy, x+dx
                if -1<ny<M+1 and -1<nx<N+1 and [y,x] not in [b1,b2] and not visited[ny][nx]:
                    Q.append([ny,nx,y,x])
        
    ans = 0
    visited2 = [[False]*(N+1) for _ in range(M+1)]
    y,x = a2
    while True:
        visited2[y][x] = True
        y,x = move[y][x]
        if [y,x]==[-1,-1]:
            break
        ans+=1

    move = [[[-1,-1]] *(N+1) for _ in range(M+1)]
    Q = deque()
    Q.append([b1[0],b1[1],-1,-1])
    while Q:
        y,x,by,bx = Q.popleft()
        if not visited2[y][x]:
            visited2[y][x] = True
            move[y][x] = [by,bx]
            if [y,x] == b2:
                break
            for dy,dx in d:
                ny,nx = y+dy, x+dx
                if -1<ny<M+1 and -1<nx<N+1 and not visited2[ny][nx]:
                    Q.append([ny,nx,y,x])

    y,x = b2
    if move[y][x]==[-1,-1]:
        return sys.maxsize
    else:
        while True:
            y,x = move[y][x]
            if [y,x]==[-1,-1]:
                break
            ans+=1


        return ans

tmp = min(bfs(a1,a2,b1,b2),bfs(b1,b2,a1,a2))
if tmp==sys.maxsize:
    print("IMPOSSIBLE")
else:
    print(tmp)