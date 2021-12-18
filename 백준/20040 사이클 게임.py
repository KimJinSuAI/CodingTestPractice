import sys
input = sys.stdin.readline
n,m = map(int,input().split())
parent = list(range(n))
def find(x):
    if x!=parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    x,y = find(x),find(y)
    if x!=y:
        parent[y] = x

for i in range(1,m+1):
    a,b = map(int,input().split())
    if find(a)==find(b):
        print(i)
        break
    else:
        a,b = sorted([a,b], key = lambda x: parent[x])
        union(a,b)
else:
    print(0)

