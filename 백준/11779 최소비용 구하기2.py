import sys
import heapq
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[]for _ in range(n+1)]
for i in range(m):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])
s,t = map(int, input().split())

visited = [False for _ in range(n+1)]
move = [0 for _ in range(n+1)]
dist = [sys.maxsize for _ in range(n+1)]
dist[s] = 0

Q = [[0,s]]
while Q:
    total, now = heapq.heappop(Q)
    if now==t:
        break
    if not visited[now]:
        visited[now] = True
        for next, cost in graph[now]:
            if dist[next]>total+cost:
                dist[next] = total+cost
                move[next] = now
                heapq.heappush(Q,[dist[next],next])

print(dist[t])
tmp = t
route = []
while tmp:
    route.append(tmp)
    tmp = move[tmp]
print(len(route))
print(' '.join(map(str,route[::-1])))
