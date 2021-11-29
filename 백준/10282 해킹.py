import sys
import heapq
input = sys.stdin.readline
TestCase = int(input()[:-1])
answer = []
for i in range(TestCase):
    n,d,c = map(int,input()[:-1].split())
    visited = [False for _ in range(n+1)]
    dist = [sys.maxsize for _ in range(n+1)]
    dist[c] = 0
    Q = [[0,c]]
    cnt, time = 0,0

    graph = [list() * (n+1) for _ in range(n+1)]
    for j in range(d):
        a,b,s = map(int,input()[:-1].split())
        graph[b].append([a,s])
    
    while Q:
        cost, node = heapq.heappop(Q)
        if not visited[node]:
            visited[node] = True
            cnt+=1
            time = cost
            for next,c in graph[node]:
                if dist[next]>cost+c:
                    dist[next] = cost+c
                    heapq.heappush(Q,[dist[next],next])
    answer.append([cnt,time])
for cnt,time in answer:
    print(cnt,time)


        