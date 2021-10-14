import sys
from collections import deque
def swap(node, i, j):
    node = node[:i] + node[j] + node[i+1:j] + node[i] + node[j+1:]
    if node[0]=='0':
        return -1
    else:
        return node

N, K = sys.stdin.readline().split()
K = int(K)
M = len(N)
maxi = -1
visited = [[False]*(K+1) for _ in range(1000001)]
Q = deque([[N,0]])
while Q:
    node, p = Q.popleft()
    if p==K:
        if maxi<int(node):
            maxi = int(node)
    else:
        p+=1
        for i in range(M-1):
            for j in range(i+1,M):
                change = swap(node, i, j)
                if change!=-1 and not visited[int(change)][p]:
                    visited[int(change)][p] = True
                    Q.append([change, p])
print(maxi)
