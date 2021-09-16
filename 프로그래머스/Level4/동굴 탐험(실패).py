import sys
sys.setrecursionlimit(10**9)
from collections import deque
def dfs(node):
    if visited[node]:           #싸이클 종료안된 사이클로 다시 돌아옴
        if visited[node]==-1:
            return True
        return False            #종료되었던 노드
    else:
        visited[node] = -1
        for j in graph[node]:
            if dfs(j):
                return True
        visited[node] = 1
        return False

def solution(n, path, order):
    global graph, visited
    visited = [0]*n
    ograph = [[] for _ in range(n) ]
    for p in path:
        ograph[p[0]].append(p[1])
        ograph[p[1]].append(p[0])
    
    Q = deque([0])
    graph = [[] for _ in range(n) ]
    while Q:
        node = Q.popleft()
        visited[node] = 1
        for next in ograph[node]:
            if visited[next]==1:
                continue
            graph[next].append(node)
            Q.append(next)

    for o in order:
        graph[o[1]].append(o[0])

    visited = [0]*n
    for i in range(n):
        if dfs(i):
            return False
    return True

print(solution(9,[[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]],[[8,5],[6,7],[4,1]]))
print(solution(9,[[8,1],[0,1],[1,2],[0,7],[4,7],[0,3],[7,5],[3,6]],[[4,1],[5,2]]))
print(solution(	9, [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]], [[4, 1], [8, 7], [6, 5]]))