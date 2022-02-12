import sys
input = sys.stdin.readline
N= int(input()[:-1])

vertices = []
parent = list(range(N))


def find(x):
    if x!=parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    x = find(x); y = find(y)
    parent[min(x,y)] = parent[max(x,y)]

for i in range(N):
    vertices.append([i]+list(map(int,input()[:-1].split())))
    



answer = 0
lines = []
for i in range(1,4):
    vertices.sort(key = lambda x: x[i])
    for j in range(N-1):
            lines.append([abs(vertices[j+1][i]-vertices[j][i]),vertices[j][0],vertices[j+1][0]])

lines.sort()
for d,x,y in lines:
    if find(x)!=find(y):
        answer+=d
        union(x,y)
print(answer)