import sys
input = sys.stdin.readline
N, M = map(int,input()[:-1].split())
t = set()
vertices = []
parent = list(range(N))

def dist(x,y):
    x1,y1 = vertices[x]
    x2,y2 = vertices[y]
    return ((x1-x2)**2+(y1-y2)**2)**0.5

def find(x):
    if x!=parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    x = find(x); y = find(y)
    parent[min(x,y)] = parent[max(x,y)]

for i in range(N):
    vertices.append(list(map(int,input()[:-1].split())))
for j in range(M):
    a,b = map(int,input()[:-1].split())
    a-=1;b-=1
    union(a,b)


answer = 0
lines = []
for i in range(N):
    for j in range(i+1,N):
        lines.append([dist(i,j),i,j])
lines.sort()
for d,x,y in lines:
    if find(x)!=find(y):
        answer+=d
        union(x,y)
print(f"{answer:.2f}")





