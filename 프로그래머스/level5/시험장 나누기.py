import sys
sys.setrecursionlimit(10**8)
def dfs(i, visited):
    visited[i] = True
    for child in graph[i][2]:
        if not visited[child]:
            dfs(child,visited)
        graph[i][1]+=graph[child][1]

    return 
def solution(k, num, links):
    global graph
    answer = 0
    graph = {}
    for i,n in enumerate(num):
        graph[i] = [n,n,[]]
    for i, link in enumerate(links):
        left, right = link
        if left!=-1:
            graph[i][2].append(left)
        if right!=-1:
            graph[i][2].append(right)

    visited = [False]*len(num)                          #그래프 편집
    for i, v in enumerate(visited):
        if not v:
            dfs(i, visited)

    
    maxNode = [-1,-1]                                   #루트노드찾기
    for node in graph.items():
        if node[1][1]>maxNode[1]:
            maxNode = [node[0],node[1][1]]

    parents = [maxNode]
    while k!=1:
        k-=1
        parents.sort(key = lambda x: -x[1])
        nowNode = parents[0]
        maxVal = [-1,0]
        for child in graph[nowNode[0]][2]:
            if graph[child][1]>maxVal[1]:
                maxVal = [child,graph[child][1]]

        if maxVal[0]!=-1:
            parents[0][1]-=maxVal[1]
            parents.append(maxVal)
        else:
            if parents[0][1]!= parents[1][1]:
                return nowNode[1]
            else:
                k+=1 
        graph[nowNode[0]][2].remove(maxVal[0])
        graph[nowNode[0]][1] = parents[0][1]
        



    
    return sorted(graph.values(), key = lambda x: -x[1])[0][1]

# print(solution(	3, [12, 30, 1, 8, 8, 6, 20, 7, 5, 10, 4, 1], [[-1, -1], [-1, -1], [-1, -1], [-1, -1], [8, 5], [2, 10], [3, 0], [6, 1], [11, -1], [7, 4], [-1, -1], [-1, -1]]))
# print(solution(4,[6, 9, 7, 5],[[-1, -1], [-1, -1], [-1, 0], [2, 1]]))
print(solution(3, [10,77,8,5,6,1,1,4], [[1,2],[-1, -1], [3,4],[5,-1],[6,7],[-1,-1],[-1,-1]]))