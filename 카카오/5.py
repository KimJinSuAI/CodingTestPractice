from collections import deque
def solution(info, edges):
    maxSheep = 1
    graph = {}
    for edge in edges:
        graph[edge[0]] = graph.get(edge[0],[]) + [edge[1]]

    visited = [False]*len(info)
    visited[0] = True
    Q = deque()
    Q.append([[0],1,0,visited])
    while Q:   
        lList ,sheep, wolf, visited = Q.popleft()
        if sheep>maxSheep:
            maxSheep = sheep
        for l in lList:
            if graph.get(l,1)==1:
                continue
            for next in graph[l]:
                if not visited[next]:
                    if info[next]==1:
                        if sheep==wolf+1:
                            continue
                        else:
                            visitedCopy = visited[:]
                            visitedCopy[next] = True
                            Q.append([lList+[next],sheep,wolf+1, visitedCopy])
                    else:
                        visitedCopy = visited[:]
                        visitedCopy[next] = True
                        Q.append([lList+[next],sheep+1,wolf, visitedCopy])
    
    answer = 0
    return maxSheep
print(solution([0,0,1,1,1,0,1,0,1,0,1,1],[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))