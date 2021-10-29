#벨만포드
import sys
input = sys.stdin.readline
N,M = list(map(int, input().split()))

cities = {}
for j in range(M):
    a,b,c = list(map(int, input().split()))
    cities[a] = cities.get(a,[]) + [[b,c]]

dist = [sys.maxsize for _ in range(N+1)]
dist[1] = 0
for i in range(N-1):
    for j in range(1,N+1):
        if dist[j]!=sys.maxsize:
            for node, w in cities.get(j,[]):
                if dist[node]>dist[j]+w:
                    dist[node] = dist[j]+w

flag = True
for j in range(1,N+1):
    if flag:
        if dist[j]!=sys.maxsize:
            for node,w in cities.get(j,[]):
                if dist[node]>dist[j]+w:
                    flag = False
                    break
    else:
        print(-1)
        break
else:
    for i in range(2,N+1):
        if dist[i]==sys.maxsize:
            print(-1)
        else:
            print(dist[i])
