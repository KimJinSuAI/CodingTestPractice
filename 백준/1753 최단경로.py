import sys, heapq
input = sys.stdin.readline

V,E = map(int,input().split())
K = int(input())-1
board = [list() for _ in range(V)]
dist = [sys.maxsize for _ in range(V)]
dist[K] = 0
for i in range(E):
    u,v,w = map(int,input().split())
    u-=1;v-=1
    board[u].append([v,w])



Q = [[0,K]]
while Q:
    dis, node = heapq.heappop(Q)
    for next, d in board[node]:
        if dist[next]> dis+d:
            dist[next]= dis+d
            heapq.heappush(Q,[dist[next],next])
for i in dist:
    if i==sys.maxsize:
        print("INF")
    else:
        print(i)
