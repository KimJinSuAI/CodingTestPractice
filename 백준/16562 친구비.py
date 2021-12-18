import sys
input = sys.stdin.readline



N,M,k = map(int,input().split())
parent = list(range(N+1))
def find(x):
    if x!=parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    x,y = find(x),find(y)
    if x!=y:
        x,y = sorted([x,y], key= lambda z: A[z])
        parent[y] = x

A = [0]+list(map(int,input().split()))
for i in range(M):
    x,y = map(int,input().split())
    union(x,y)

money = A[find(1)]
for i in range(2,N+1):
    if find(1)!=find(i):
        money+=A[find(i)]
        union(1,i)
if money<=k:
    print(money)
else:
    print("Oh no")

        
