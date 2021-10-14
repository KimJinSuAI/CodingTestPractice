import sys
from itertools import permutations
from collections import deque

def bfs(start):
    Q = deque([[0]+start])
    dist = [[sys.maxsize] * w for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    dist[Q[0][1]][Q[0][2]] = 0
    while Q:
        dis, ny,nx = Q.popleft()
        dist[ny][nx] = dis
        if not visited[ny][nx]:
            visited[ny][nx] = True
            for dy, dx in d:
                nexty, nextx = ny+dy, nx+dx
                if -1<nexty<h and -1<nextx<w and room[nexty][nextx]!='x' and not visited[nexty][nextx]:
                    Q.append([dis+1,nexty,nextx])
    return dist

answer = []
while True:
    w,h = list(map(int, sys.stdin.readline().split())) 
    if [w,h] == [0,0]:
        for ans in answer:
            print(ans)
        break
    else:
        room = []
        for y in range(h):
            room.append(list(sys.stdin.readline())[:-1])
        
        dirts = []
        d = [(-1,0),(1,0),(0,-1),(0,1)]
        
        for y in range(h):
            for x in range(w):
                if room[y][x] == "*":
                    dirts.append((y,x))
                elif room[y][x] == "o":
                    start = (y,x)

        flag, dist = False, {}
        dist[start] = bfs(list(start))
        for y,x in dirts:
            if dist[start][y][x] == sys.maxsize:
                flag = True
                break
            
        if flag:
            answer.append(-1)
            continue

        for dirt in dirts:
            dist[dirt] = bfs(list(dirt))
    
        ans = sys.maxsize
        for dirtlist in permutations(dirts):
            now = start
            count = 0
            for nexty,nextx in dirtlist:
                count+=dist[now][nexty][nextx]
                now = (nexty,nextx)
            ans = min(ans,count)
        answer.append(ans)
