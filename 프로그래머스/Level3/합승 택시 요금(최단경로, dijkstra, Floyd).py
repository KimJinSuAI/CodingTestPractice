#floyd-warshall
def solution(n, s, a, b, fares):
    d = [ [ 20000001 for _ in range(n) ] for _ in range(n) ]
    for x in range(n):
        d[x][x] = 0
    for x, y, c in fares:
        d[x-1][y-1] = c
        d[y-1][x-1] = c

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if d[j][k] > d[j][i] + d[i][k]:
                    d[j][k] = d[j][i] + d[i][k]

    minv = 40000002
    for i in range(n):
        minv = min(minv, d[s-1][i]+d[i][a-1]+d[i][b-1])
    return minv








#dijkstra
from collections import defaultdict
import heapq

def solution(n, s, a, b, fares):
    dic = defaultdict(list)
    for st, ed, co in fares:
        dic[st].append((co, ed))
        dic[ed].append((co, st))
    ans = []
    for i in range(1, n+1):                             #다이젝스트라는 한점에서 모든점까지 거리 구해줌. 따라서 모든점에서 dijkstra구하면 
        Q = [(0, i)]                                    #어떤 점이(내리는지점)에서 시작점, a, b까지 거리의 합이 가장 작은지 알 수 있음.
        visited = [True] * (n+1)                        #사실 Floyd랑 같다고 본다..
        dp = [float('inf')] * (n+1)
        dp[i] = 0
        while Q:
            co, des = heapq.heappop(Q)
            if visited[des]:
                visited[des] = False
                for cost, destination in dic[des]:
                    dp[destination] = min(cost + dp[des], dp[destination])
                    heapq.heappush(Q, (dp[destination], destination))
        ans.append(dp[a] + dp[b] + dp[s])

    return min(ans)

print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))