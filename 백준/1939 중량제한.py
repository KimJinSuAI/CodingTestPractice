from collections import deque
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
board = [list() for _ in range(N)]
max_c = -sys.maxsize
for i in range(M):
    A,B,C = map(int,input().split())
    A-=1;B-=1
    board[A].append([B,C])
    board[B].append([A,C])
    max_c = max(max_c,C)
s,t = map(int,input().split())
s-=1;t-=1

def bfs(k):
    visited = [False for _ in range(N)]
    Q = deque([s])

    while Q:
        node = Q.popleft()
        if not visited[node]:
            visited[node] = True
            for next,dist in board[node]:
                if not visited[next] and k<=dist:
                    Q.append(next)

    return visited[t]

l,r = 0,max_c
ans = 0
while l<=r:
    mid = (l+r)//2
    if bfs(mid):
        l = mid+1
    else:
        r = mid-1

print(r)