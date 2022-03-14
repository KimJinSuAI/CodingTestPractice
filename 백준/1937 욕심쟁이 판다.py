import sys
input = sys.stdin.readline
n = int(input())
board = []
for i in range(n):
    board.append(list(map(int,input().split())))

visited = [[False for i in range(n)] for j in range(n)]
cnt = [[1 for i in range(n)] for j in range(n)]
d = [(1,0),(-1,0),(0,1), (0,-1)]

def dfs(y,x):
    visited[y][x] = True
    for dy,dx in d:
        ny,nx = y+dy,x+dx
        if -1<ny<n and -1<nx<n and board[ny][nx]>board[y][x]:
            if visited[ny][nx]:
                cnt[y][x] = max(cnt[y][x], 1+cnt[ny][nx])
            else:
                cnt[y][x] = max(cnt[y][x], 1+dfs(ny,nx))
    return cnt[y][x]
                
for y in range(n):
    for x in range(n):
        if not visited[y][x]:
            dfs(y,x)

maxi = 0
for y in range(n):
    maxi = max(maxi, max(cnt[y]))
print(maxi)


