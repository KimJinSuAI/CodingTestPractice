import sys
from collections import deque

LOG = 21
input = sys.stdin.readline
N = int(input())
tree = [list() for _ in range(N+1)]
for _ in range(N-1):
    a,b = sorted(map(int,input().split()))
    tree[b].append(a)
    tree[a].append(b)

level = [-1 for _ in range(N+1)]
parent = [[0]*LOG for _ in range(N+1)]
Q = deque([[1,0,0]])
while Q:
    node, nowlevel, before = Q.pop()
    if level[node]==-1:
        level[node] = nowlevel
        parent[node][0] = before
        for next in tree[node]:
            if level[next]==-1:
                Q.append([next,nowlevel+1,node])

for i in range(1,LOG):
    for j in range(1,N+1):
        parent[j][i] = parent[parent[j][i-1]][i-1]
    


ans = []
M = int(input())
for _ in range(M):
    x,y = map(int,input().split())
    if level[x]>level[y]:
        x,y = y,x
    for i in range(LOG-1,-1,-1):
        if level[y]-level[x]>=(1<<i):
            y =parent[y][i]
    if x==y:
        ans.append(x)
    else:
        for i in range(LOG-1,-1,-1):
            if parent[x][i]!=parent[y][i]:
                x = parent[x][i]
                y = parent[y][i]
        ans.append(parent[x][0])

for i in ans:
    print(i)
