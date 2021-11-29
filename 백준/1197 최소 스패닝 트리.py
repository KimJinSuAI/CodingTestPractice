import sys
input = sys.stdin.readline

answer = 0
V,E = map(int,input().split())
lines = []
for i in range(E):
    lines.append(list(map(int,input().split())))
lines.sort(key= lambda x: x[2])
parent = list(range(V+1))

def find(x):
    if x!=parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

cnt = 1
for A,B,C in lines:
    if find(A)!=find(B):
        a,b = min(parent[A],parent[B]), max(parent[A],parent[B])
        parent[b] = parent[a]
        cnt+=1
        answer+=C
        if cnt==V:
            break
    
print(answer)


