import sys
from collections import deque
input = sys.stdin.readline

arr = []
n = int(input())
for _ in range(n):
    arr.append(list(map(int, input().split())))

d = [(-1,0),(1,0),(0,-1),(0,1)]

ll,rr = sys.maxsize,-1
for y in range(len(arr)):
    for x in range(len(arr[0])):
        ll = min(ll,arr[y][x])
        rr = max(rr,arr[y][x])

lr, rl = min(arr[0][0],arr[-1][-1]), max(arr[0][0],arr[-1][-1])
l,r = ll, rl
ans = sys.maxsize
while ll<=l<=lr and rl<= r <= rr:
    Q = deque([[0,0]])
    visited = [[False]*n for _ in range(n)]
    while Q:
        y,x = Q.popleft()
        if not visited[y][x]:
            visited[y][x] = True
            for dy, dx in d:
                ny, nx = y+dy, x+dx
                if -1<ny<n and -1<nx<n and not visited[ny][nx] and l<=arr[ny][nx]<=r:
                    Q.append([ny,nx])
    if visited[n-1][n-1]:
        ans = min(ans,r-l)
        l+=1
    else:
        r+=1
    
print(ans)