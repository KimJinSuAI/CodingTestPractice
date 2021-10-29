import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[sys.maxsize] * n for _ in range(n)]
for _ in range(m):
    a,b,c = map(int,input().split())
    a-=1
    b-=1
    graph[a][b] = min(graph[a][b],c)
for i in range(n):
    graph[i][i] = 0

for i in range(n):
    for j in range(n):
        for k in range(n):
            if graph[j][k]>graph[j][i]+graph[i][k]:
                graph[j][k]=graph[j][i]+graph[i][k]

for i in range(n):
    for j in range(n):
        if graph[i][j]==sys.maxsize:
            print(0, end = ' ')
        else:
            print(graph[i][j], end= ' ')
    print()
