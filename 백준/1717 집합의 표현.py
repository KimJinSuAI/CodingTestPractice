import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
n,m = map(int,input().split())
parent = list(range(n+1))

def union(x,y):
    x = find(x)
    y = find(y)
    if x!=y:
        parent[x] = y
    return


def find(x):
    if x!=parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

for i in range(m):
    op, a,b = map(int,input().split())
    if op == 0:
        union(min(a,b),max(a,b))
    else:
        print("YES" if find(a)==find(b) else "NO")