import sys
from collections import deque
input = sys.stdin.readline

N = int(input()[:-1])
tiles = []

rpt = [N,N-1]
idx = 0
cnt = N
tmp = []
for i in range(1,N*N-N//2+1):
    tmp.append([i]+input()[:-1].split())
    if i == cnt:
        tiles.append(tmp)
        idx = (idx+1)%2
        cnt += rpt[idx]
        tmp = []

Q = deque([[1,0,0,[1]]])
visited = [False for _ in range(N*N-N//2+1)]
Old = [[-1,-1],[1,-1],[0,-1]]
Ord = [[-1,0],[1,0],[0,1]]
Eld = [[-1,0],[1,0],[0,-1]]
Erd = [[-1,1],[1,1],[0,1]]

target = tiles[-1][-1][0]
mini = [-1,[]]
while Q:
    dist, y,x, route = Q.popleft()
    now = tiles[y][x][0]
    if not visited[now]:
        visited[now] = True
        if mini[0]<now:
            mini = [now,route]
            if now== target:
                break
        left = tiles[y][x][1]
        right = tiles[y][x][2]
        if y%2:
            ld,rd = Eld,Erd 
        else:
            ld,rd = Old,Ord

        for dy,dx in ld:
            ny,nx = y+dy,x+dx
            if -1<ny<N and -1<nx<len(tiles[ny]) and not visited[tiles[ny][nx][0]] and left==tiles[ny][nx][2]:
                Q.append([dist+1,ny,nx,route+[tiles[ny][nx][0]]])
        for dy,dx in rd:
            ny,nx = y+dy,x+dx
            if -1<ny<N and -1<nx<len(tiles[ny]) and not visited[tiles[ny][nx][0]] and right==tiles[ny][nx][1]:
                Q.append([dist+1,ny,nx,route+[tiles[ny][nx][0]]])
            
print(len(mini[1]))
for i in mini[1]:
    print(i, end=" ")
print()
    
