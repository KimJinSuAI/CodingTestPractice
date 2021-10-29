import sys
from collections import deque
input = sys.stdin.readline

arr = []
n = int(input())
for _ in range(n):
    arr.append(list(map(int, input().split())))

d = [(-1,0),(1,0),(0,-1),(0,1)]


l,r = 0, 200

def bfs(mi,mx):
    if not mi<=arr[0][0]<=mx:
        return False
    Q = deque([[0,0]])
    
    visited = [[False]*n for _ in range(n)]
    while Q:
        y,x = Q.popleft()
        if not visited[y][x]:
            visited[y][x] = True
            for dy, dx in d:
                ny, nx = y+dy, x+dx
                if -1<ny<n and -1<nx<n and not visited[ny][nx]:
                    if mi<=arr[ny][nx]<=mx:
                        Q.append([ny,nx])
    return visited[n-1][n-1]

def check(mid):
    for i in range(0,201-mid,1):
        if bfs(i,i+mid):
            return True
    return False
    
while l<=r:
    mid = (r+l)//2

    if check(mid):
        r = mid-1
    else:
        l = mid+1
    
print(r+1)