import sys, heapq,math
d = [(-1,0),(1,0),(0,-1),(0,1)]
N = int(sys.stdin.readline())
maxi = float('inf')
answer = []
def findPrisoner():
    prisoner = []
    for y in range(H):
        for x in range(W):
            if prison[y][x]=='$':
                prisoner.append([y,x])
                if len(prisoner)==2:
                    return prisoner

def countDist(start):
    dist = [[maxi]*W for _ in range(H)]
    dist[start[0]][start[1]] = 0
    visited = [[True]*W for _ in range(H)]
    Q = [[0]+start]
    while Q:
        dit, y, x = heapq.heappop(Q)
        if visited[y][x]:
            visited[y][x] = False
            for dy, dx in d:
                nexty, nextx = y+dy, x+dx
                if -1<nexty<H and -1<nextx<W:
                    if prison[nexty][nextx] in ['.', '$']:
                        dist[nexty][nextx] = min(dist[nexty][nextx], dit)
                        heapq.heappush(Q,[dist[nexty][nextx],nexty,nextx])
                    elif prison[nexty][nextx] == '#':
                        dist[nexty][nextx] = min(dist[nexty][nextx], dit+1)
                        heapq.heappush(Q,[dist[nexty][nextx],nexty,nextx])
    return dist
for i in range(N):
    exits = []
    H,W = list(map(int,sys.stdin.readline().split()))
    H+=2
    W+=2
    prison = [['.']*(W)]
    for h in range(H-2):
        prison.append(['.']+list(sys.stdin.readline())[:-1]+['.'])
    prison.append(['.']*(W))

    prisoner = findPrisoner()                               #죄수찾기

    dist = []                                               #상근이, 죄수1, 죄수2 dijkstra
    dist.append(countDist([0,0]))
    dist.append(countDist(prisoner[0]))
    dist.append(countDist(prisoner[1]))
    
    mini = maxi
    for y in range(H):
        for x in range(W):
            dist[0][y][x]+=(dist[1][y][x]+dist[2][y][x])
            if prison[y][x]=='#':
                dist[0][y][x]-=2
            mini = min(mini,dist[0][y][x])

    answer.append(mini)
for ans in answer:
    print(ans)