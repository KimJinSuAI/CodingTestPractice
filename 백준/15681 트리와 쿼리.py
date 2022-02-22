import sys
sys.setrecursionlimit(10**5+1)
input = sys.stdin.readline

N, R, Q = map(int, input().split())
tree = [[] for _ in range(N+1)]
SubtreeNodes = [0] * (N+1)

for i in range(N-1):
    U,V = map(int,input().split())
    tree[U].append(V)
    tree[V].append(U)

def Cntnode(root):
    SubtreeNodes[root] = 1
    for next in tree[root]:
        if not SubtreeNodes[next]:
            Cntnode(next)
            SubtreeNodes[root]+=SubtreeNodes[next]
Cntnode(R)

for i in range(Q):
    U = int(input())
    print(SubtreeNodes[U])

            

