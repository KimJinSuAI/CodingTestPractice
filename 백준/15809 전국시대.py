import sys
input = sys.stdin.readline

N,M = map(int, input().split())
A = []
parent = list(range(N))
def find(x):
    if x!=parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(o,x,y):
    x,y = find(x),find(y)
    if x!=y:
        x,y = sorted([x,y], key = lambda z: A[z])

        parent[x] = y
        if o==1:#동맹
            A[y]+=A[x]
        else:
            A[y]-=A[x]
        A[x] = 0


    

for i in range(N):
    A.append(int(input()))

for i in range(M):
    O,P,Q = map(int,input().split())
    P-=1;Q-=1
    union(O,P,Q)


ans = []
for i in range(N):
    if A[i]!=0:
        ans.append(A[i])
ans.sort()
print(len(ans))
for i in range(len(ans)):
    print(ans[i], end=' ')


