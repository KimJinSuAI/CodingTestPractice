from itertools import permutations
import heapq
import copy
def solution(n, start, end, roads, traps):
    maze = {}
    visited = [[False]*n for _ in range(1<<len(traps))]
    for road in roads:
        maze[road[0]] = maze.get(road[0],[])+[[road[1],road[2],0]]
        maze[road[1]] = maze.get(road[1],[])+[[road[0],-1,1]]
    Q = []
    heapq.heappush(Q, (0,start,0))
    
    while Q:
        cost, node, state = heapq.heappop(Q) #비용, 노드, 상태
        if node==end:
            return cost
        if visited[state][node]:
            continue
        visited[state][node] = True

        for nextNode in maze[node]:
            if nextNode[1]==0:
                if nextNode[0] in traps:

                heapq.heappush(Q, (nextNode[0],nextNode[1],state))
            
    return -1

print(solution(4,1,4,[[1, 2, 1], [3, 2, 1], [2, 4, 1]],[2, 3]))