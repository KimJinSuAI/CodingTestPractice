import sys, heapq

def dijkstra(start):
    visited = [sys.maxsize for _ in range(n+1)]
    visited[start] = 0
    Q = [start]
    while Q:
        node = heapq.heappop(Q)
        for next, w in graph[node]:
            if visited[next] > visited[node] + w:
                visited[next] = visited[node]+w
                heapq.heappush(Q,next)
    return visited

answer = []
T = int(sys.stdin.readline())
for test in range(T):
    n, m, t = list(map(int,sys.stdin.readline().split()))   #교차로, 도로, 목적지 후보 개수
    s, g, h = list(map(int,sys.stdin.readline().split()))   #출발지, 교차로 g,h사이도로? 냄새맡은지점
    graph = {}
    candi = []
    for mm in range(m):
        a,b,d = list(map(int,sys.stdin.readline().split()))
        graph[a] = graph.get(a,[])+[(b,d)]
        graph[b] = graph.get(b,[])+[(a,d)]
    for tt in range(t):
        candi.append(int(sys.stdin.readline()))

    start = dijkstra(s)
    H = dijkstra(h)
    G = dijkstra(g)

    answer.append(sorted([can for can in candi if start[can] in [start[h]+H[g]+G[can] , start[g]+G[h]+H[can]]]))
for ans in answer:
    tmp = ""
    for a in ans:
        tmp+= str(a) + " "
    print(tmp)
