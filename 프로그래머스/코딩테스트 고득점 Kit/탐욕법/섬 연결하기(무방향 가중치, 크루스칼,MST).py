# 처음에는 1.탐욕적으로 하기 2. dp로 풀려했다. 
# dp가 너무 복잡하여 탐욕적방법으로 바꿈
# 크루스칼 비스무리함.. 
graph = {}
def dfs(firstV, target, now):
    global graph
    firstV[now] = 1
    for i in graph[now]:
        if firstV[i[0]]==0:
            dfs(firstV, target, i[0])
    return firstV

def solution(n, costs):
    global graph
    graph={}
    visited = [0]*n
    firstV = visited.copy()
    target = [1]*n
    answer =0
    costs.sort(key = lambda x:x[2])
    for cost in costs[:]:
        if visited[cost[0]] == 0 or visited[cost[1]]==0:
            answer += cost[2]
            graph[cost[0]] = graph.get(cost[0],[])+[[cost[1],cost[2]]]
            graph[cost[1]] = graph.get(cost[1],[])+[[cost[0],cost[2]]]
            costs.remove(cost)
            if visited[cost[0]] == 0:
                visited[cost[0]] = 1
            if visited[cost[1]] == 0:
                visited[cost[1]] = 1


    visited = dfs(firstV[:], target, 0)
    while visited!=target:
        zero =  [x for x in range(len(visited)) if visited[x] ==0]
        for cost in costs[:]:
            if (cost[0] in zero or cost[1] in zero) and (cost[0] not in zero or cost[1] not in zero) :
                graph[cost[0]] = graph.get(cost[0],[])+[[cost[1],cost[2]]]
                graph[cost[1]] = graph.get(cost[1],[])+[[cost[0],cost[2]]]
                answer += cost[2]
                costs.remove(cost)
                break
        visited = dfs(firstV[:], target, 0)
    return answer











#다른사람
def ancestor(node, parents):                                            # 크루스칼
    if parents[node] == node:
        return node
    else:
        return ancestor(parents[node], parents) 
        
def solution(n, costs):
    answer = 0
    edges = sorted([(x[2], x[0], x[1]) for x in costs])
    parents = [i for i in range(n)]                                               #union-find의 초기화
    bridges = 0
    for w, f, t in edges: 
        if ancestor(f, parents) != ancestor(t, parents):                          #union-find 
            answer += w
            parents[ancestor(f, parents)] = t

            bridges += 1
        if bridges == n - 1:
            break
    return answer

            
        











# print(solution(2, [[0,1,4]]), 4)
# print(solution(3, [[0,1,1],[0,2,2]]),3)
# print(solution(4,[[0,1,1],[0,2,6],[0,3,4],[1,2,2],[1,3,5],[2,3,3]]), 6)#3
# print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]), 4)#2
print(solution(5, [[0, 1, 1], [3, 4, 1], [1, 2, 2], [0,2,3], [0, 3, 4]]),8)#4
# print(solution(5, [[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4], [2, 4, 6], [4, 0, 7]]),15)#5
# print(solution(4, [[0, 1, 5], [1, 2, 3], [2, 3, 3], [1, 3, 2], [0, 3, 4]]),9) #6
# print(solution(5, [[0, 1, 1], [3, 1, 1], [0, 2, 2], [0, 3, 2], [0, 4, 100]]), 104) #7
# print(solution(6,  [[0, 1, 5], [0, 3, 2], [0, 4, 3], [1, 4, 1], [3, 4, 10], [1, 2, 2], [2, 5, 3], [4, 5, 4]]), 11)#8
# print(solution(5,[[0, 1, 1], [2, 3, 1], [3, 4, 2], [1, 2, 2], [0, 4, 100]]), 6) #9
# print(solution(5, [[0, 1, 1], [0, 4, 5], [2, 4, 1], [2, 3, 1], [3, 4, 1]]), 8)