import sys

answer = []
T = int(sys.stdin.readline())
for test in range(T):
    n, m, t = list(map(int,sys.stdin.readline().split()))   #교차로, 도로, 목적지 후보 개수
    s, g, h = list(map(int,sys.stdin.readline().split()))   #출발지, 교차로 g,h사이도로?
    graph = {}
    candi = []
    for mm in range(m):
        a,b,d = list(map(int,sys.stdin.readline().split()))
        graph[a] = graph.get(a,[])+[(b,d)]
        graph[b] = graph.get(b,[])+[(a,d)]
    for tt in range(t):
        candi.append(int(sys.stdin.readline()))
