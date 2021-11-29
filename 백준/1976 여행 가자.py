import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
parent = list(range(N))

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

for i in range(N):
    city = list(map(int,input().split()))
    for j in range(N):
        if city[j] == 1:
            union(max(i,j),min(i,j))


plan = list(map(lambda x: int(x)-1,input().split()))
travel = find(plan[0])
for i in range(1,M):
    if find(plan[i])!=travel:
        print("NO")
        break
else:
    print("YES")