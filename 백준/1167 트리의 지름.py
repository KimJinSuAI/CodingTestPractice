import sys, heapq
input = sys.stdin.readline

def dijkstra(start):
    global v, tree
    dist = [sys.maxsize for _ in range(v+1)]
    visited = [False for _ in range(v+1)]
    dist[start] = 0
    Q = [[0,start]]
    while Q:
        d, node = heapq.heappop(Q)
        if not visited[node]:
            visited[node] = True
            for next, cost in tree[node]:
                if dist[next]>d+cost:
                    dist[next] = d+cost
                    heapq.heappush(Q,[dist[next],next])
    
    maxi = [-1,0]
    for i,d in enumerate(dist[1:]):
        if maxi[1]<d:
            maxi = [i+1,d]
    return maxi


v = int(input())
tree = [list() for _ in range(v+1)]
for i in range(v):
    tmp = list(map(int,input().split()))
    idx = 1
    while tmp[idx]!=-1:
        tree[tmp[0]].append([tmp[idx],tmp[idx+1]])
        idx+=2

a,b = dijkstra(1)
a,b = dijkstra(a)
a,b = dijkstra(a)

print(b)
    
