import sys
import copy
from collections import deque
r, c = list(map(int, (sys.stdin.readline().split())))
Map = []
Swans = []
water = []
d = [[-1,0],[1,0],[0,-1],[0,1]]
for y in range(r):
    Map.append(list(sys.stdin.readline()[:c]))

for y in range(r):##
    for x in range(c):
        if Map[y][x]=="L":
            Swans.append((y,x))
            Map[y][x] = '.'
            
waterVisited = [[False]*c for _ in range(r)]
for y in range(r):                                      #처음에 모든 "."에 대해 근처 X를 다음 녹을지점으로 추가하고 방문여부 표시
    for x in range(c):
        if Map[y][x] == '.':
            waterVisited[y][x] = True
            for dy,dx in d:
                nexty, nextx = y+dy, x+dx
                if -1<nexty<r and -1<nextx<c and Map[nexty][nextx] == "X" and not waterVisited[nexty][nextx]:
                    water.append((nexty,nextx))
                    waterVisited[nexty][nextx] = True

def canMeet(water):
    answer = 0
    Q = deque([Swans[0]])
    visited = [[False]*c for _ in range(r)]
    nextQ = deque([])
    while Q:                                            #처음에 오리있는 곳에서 만날 수 있는지 탐색.
        ny,nx = Q.pop()
        if visited[ny][nx]:
            continue
        visited[ny][nx] = True
        if (ny,nx) == Swans[1]:
            return answer
        for dy,dx in d:
            nexty, nextx = ny+dy, nx+dx
            if -1<nexty<r and -1<nextx<c and visited[nexty][nextx] == False:
                if Map[nexty][nextx] != "X":
                    Q.append([nexty,nextx])
                else:                                   # X면 다음에 방문
                    nextQ.append([nexty,nextx])

    while True:     
        answer+=1   
        for y,x in water:                               #물로 바꾸고 다음 물로 바꿀지점들 추가
            Map[y][x] = '.'
        nextWater = []
        for y,x in water:
            for dy,dx in d:
                nexty, nextx = y+dy, x+dx
                if -1<nexty<r and -1<nextx<c and Map[nexty][nextx] == "X" and not waterVisited[nexty][nextx]:
                    nextWater.append((nexty,nextx))
                    waterVisited[nexty][nextx] = True
        water = nextWater

        Q = copy.deepcopy(nextQ)
        nextQ = deque([])
        while Q:
            ny,nx = Q.pop()
            if visited[ny][nx]==True:
                continue
            visited[ny][nx] = True
            if (ny,nx) == Swans[1]:
                return answer
            for dy,dx in d:
                nexty, nextx = ny+dy, nx+dx
                if -1<nexty<r and -1<nextx<c and visited[nexty][nextx] == False:
                    if Map[nexty][nextx] != "X":
                        Q.append([nexty,nextx])
                    else:
                        nextQ.append([nexty,nextx])



        
print(canMeet(water))
