import sys
from collections import deque
R, C = list(map(int,sys.stdin.readline().split()))
cave = [list(sys.stdin.readline())[:-1] for _ in range(R)]
sys.stdin.readline()
throws = list(map(int,sys.stdin.readline().split()))

def isfloating(Q, visited, xs):
    global d
    rtun = True
    while Q:
        y,x = Q.popleft()
        if y == R-1:
            rtun = False
        if visited[y][x] == 2:
            continue
        visited[y][x] = 2
        xs[x] = max(xs.get(x,0),y)
        for dy,dx in d:
            nexty,nextx = y+dy, x+dx
            if -1<nexty<R and -1<nextx<C and cave[nexty][nextx]=="x":
                if visited[nexty][nextx]!=2:
                    Q.append((nexty,nextx))
    return rtun


d = [(1,0),(-1,0),(0,1),(0,-1)]
count = -1
for y in throws:
    count+=1
    y = R-y
    if count%2:
        start, end ,step = C-1, -1, -1
    else:
        start, end, step = 0, C, 1
    for x in range(start, end, step):
        if cave[y][x]=='x':
            cave[y][x] = '.'
            visited = [[False]*C for _ in range(R)]
            
            for dy,dx in d:
                nexty,nextx = y+dy, x+dx
                if -1<nexty<R and -1<nextx<C and cave[nexty][nextx]=="x" and not visited[nexty][nextx]:#x인데 방문했던 x가 아니라면
                    xs = {}
                    if isfloating(deque([(nexty,nextx)]), visited, xs):                         #떨어져있다면
                        howmuchfall = 1001                                                      #얼마나 떨어질지 계산
                        for tmpx, tmpy in xs.items():
                            count2 = 0
                            while tmpy+count2!=R-1 and cave[tmpy+count2+1][tmpx]!="x":
                                count2+=1
                            howmuchfall = min(howmuchfall, count2)

                        if howmuchfall == 0: continue                                           #클러스터 떨어지기
                        for tmpx, tmpy in xs.items():
                            for tmpy2 in range(tmpy,-1,-1):
                                if visited[tmpy2][tmpx]==2 and cave[tmpy2][tmpx]=='x':
                                    cave[tmpy2][tmpx] = '.'
                                    cave[tmpy2+howmuchfall][tmpx] = 'x'
                                    visited[tmpy2][tmpx] = False
                                    visited[tmpy2+howmuchfall][tmpx] = True

                    else:
                        for tmpy in range(R):
                            for tmpx in range(C):
                                if visited[tmpy][tmpx]==2:
                                    visited[tmpy][tmpx] = True
            break

    
        
for i in cave:
    print(''.join(i))


# 12 24
# ........................
# ........................
# ..........xxxxxxxxxxx...
# ....................x...
# .............x.x....x...
# .............xxx....x...
# ..............x.....x...
# ..........xxxxxxxxxxx...
# ..............x.........
# ..............x.........
# ..............x.........
# ..............x.........
# 6
# 6 6 6 5 3 5
# ........................
# ........................
# ........................
# ........................
# ........................
# ..........xxxxxxxxxxx...
# ...............x....x...
# .............xxx........
# ..........xxxxxxxxxxx...
# ..............x.........
# ..............x.........
# ..............x.........