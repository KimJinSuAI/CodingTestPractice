import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N,M,K = map(int, input().split())
    dp = [[sys.maxsize] * (M+1) for tmp in range(N)]
    dp[0][0] = 0
    graph = {}
    for __ in range(K):
        u,v,c,d = map(int, input().split()) #출발,도착,비용,시간
        u-=1
        v-=1
        graph[u] = graph.get(u,[]) + [[v,c,d]]

    for j in range(M+1):
        for i in range(N):
            if dp[i][j] == sys.maxsize: continue
            for dst, c, t in graph.get(i,[]):
                nextC,nextT = j+c, dp[i][j]+t
                if nextC>M: continue
                if dp[dst][nextC]>nextT:
                    dp[dst][nextC] = nextT

    tmp = min(dp[N-1][i] for i in range(M+1))
    if tmp == sys.maxsize:
        print("Poor KCM")
    else:
        print(tmp)
    

