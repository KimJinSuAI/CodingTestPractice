import sys, heapq
def findMirror():
    mirror = []
    for y in range(H):
        for x in range(W):
            if field[y][x]=='C':
                mirror.append([y,x])
                if len(mirror)==2:
                    return mirror

def countMirror(start, sdir):
    dist = [[maxi]*W for _ in range(H)]
    dist[start[0]][start[1]] = 0
    Q = [[0]+start+[sdir]]
    while Q:
        dit, y, x, dir = heapq.heappop(Q)
        for i, ds in enumerate(d):
            if (dir==0 and i==1) or (dir==1 and i==0): continue
            elif dir*i==6: continue
            dy, dx = ds
            nexty, nextx = y+dy, x+dx
            if -1<nexty<H and -1<nextx<W and field[nexty][nextx] in ['.', 'C']:
                tmpDit = dit
                if i!= dir:
                    tmpDit+=1
                if dist[nexty][nextx] > tmpDit:
                    dist[nexty][nextx] = tmpDit
                    heapq.heappush(Q,[dist[nexty][nextx],nexty,nextx,i])
    return dist

maxi = float('inf')
d = [(-1,0),(1,0),(0,-1),(0,1)]#상하좌우
W, H = list(map(int,sys.stdin.readline().split()))
field = []
for h in range(H):
    field.append(list(sys.stdin.readline())[:-1])

mirrors = findMirror()
mini = maxi
for i in range(4):
    mini = min(mini,countMirror(mirrors[0], i)[mirrors[1][0]][mirrors[1][1]])
print(mini)