from collections import deque
def bfs(n,start):
    count = 0
    visited = [False for _ in range(n+1)] 
    Q = deque([start])
    while Q:
        node = Q.popleft()
        if visited[node]:
            continue
        visited[node] = True
        count+=1
        for next in graph[node]:
            if not visited[next]:
                Q.append(next)
    return count

def solution(n, wires):
    global graph
    graph = {}
    mini = n
    for a,b in wires:
        graph[a] = graph.get(a,[])+[b]
        graph[b] = graph.get(b,[])+[a]
    for a,b in wires:
        graph[a].remove(b)
        graph[b].remove(a)
        A = bfs(n,a)
        B = bfs(n,b)
        mini = min(mini,abs(A-B))
        graph[a] = graph.get(a,[])+[b]
        graph[b] = graph.get(b,[])+[a]
    return mini
