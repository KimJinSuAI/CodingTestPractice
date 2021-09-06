# from itertools import combinations
# def solution(n, edges):                                         #Floyd
#     dist = [[float('INF')]*n for i in range(n)]
#     for i,j in edges:
#         dist[i-1][j-1] = 1
#         dist[j-1][i-1] = 1
#     for i in range(n):
#         dist[i][i] = 0
#     for k in range(n):
#         for i in range(n):
#             for j in range(n):
#                 if dist[i][j] > dist[i][k]+dist[k][j]:
#                     dist[i][j] = dist[i][k]+dist[k][j]

#     answer = 0
#     for a,b,c in combinations(range(n),3):
#         answer = max(answer,sorted([dist[a][b],dist[b][c],dist[c][a]])[1])
#     return answer


import heapq
def dijkstra(i,n):
    Q = [(0,i)]
    visited = [True]*n
    dp = [float('inf')]*n
    dp[i] = 0
    while Q:
        cost, node = heapq.heappop(Q)
        if visited[node]:
            visited[node] = False
            for next in graph[node]:
                if dp[next] > cost+1:
                    dp[next] = cost+1
                    Q.append((dp[next],next))
    ans = [[0,0]]
    for num, cost in enumerate(dp):
        if ans[0][1]<cost:
            ans = [[num,cost]]
        elif ans[0][1] == cost:
            ans.append([num,cost])
    return ans

def solution(n, edges):
    global graph
    graph = [[]for _ in range(n)]  
    for e in edges:
        graph[e[0]-1].append(e[1]-1)
        graph[e[1]-1].append(e[0]-1)

    tmp = dijkstra(0,n)
    tmp2 = dijkstra(tmp[0][0],n)
    if len(tmp2)>1:
        return tmp2[0][1]
    else:
        tmp3 = dijkstra(tmp2[0][0],n)
        if len(tmp3)>1:
            return tmp3[0][1]
        else:
            return tmp3[0][1]-1



print(solution(4, [[1,2],[2,3],[3,4]]))
print(solution(5,[[1,5],[2,5],[3,5],[4,5]]))