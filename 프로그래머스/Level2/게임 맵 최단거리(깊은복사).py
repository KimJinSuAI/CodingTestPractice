# import sys
# import copy
# sys.setrecursionlimit(1000001)
# map = []
# minimum = 99999999
# def dfs(visited, nowX, nowY, count):
#     global minimum
#     global map
#     if nowX==len(map[0])-1 and nowY==len(map)-1:
#         return count
#     if minimum<count:
#         return 99999999
#     if visited[nowY][nowX]==1:
#         return 99999999
#     else:
#         visitedCopy = copy.deepcopy(visited)
#         visitedCopy[nowY][nowX] = 1
#         go = []
#         if nowX+1<=len(map[0])-1:              #우
#             if map[nowY][nowX+1] == 1 and visited[nowY][nowX+1]==0:
#                 x=dfs(visitedCopy, nowX+1,nowY, count+1)
#                 if minimum>x: 
#                     minimum = x 
#                 go.append(x)
#         if nowY+1<=len(map)-1:                 #하
#             if map[nowY+1][nowX]==1 and visited[nowY+1][nowX]==0:
#                 x=dfs(visitedCopy, nowX,nowY+1, count+1)
#                 if minimum>x: 
#                     minimum = x 
#                 go.append(x)
#         if nowX-1>=0:                       #좌
#             if map[nowY][nowX-1]==1 and visited[nowY][nowX-1]==0:
#                 x=dfs(visitedCopy, nowX-1,nowY, count+1)
#                 if minimum>x: 
#                     minimum = x 
#                 go.append(x)
#         if nowY-1>=0:
#             if map[nowY-1][nowX]==1 and visited[nowY-1][nowX]==0:        #상
#                 x=dfs(visitedCopy, nowX,nowY-1, count+1)
#                 if minimum>x: 
#                     minimum = x 
#                 go.append(x)
        
#         return min(go) if go else 99999999


# def solution(maps):
#     global map
#     map = maps
#     visited = [[0]*len(maps[0]) for _ in range(len(maps))]
    
#     answer = dfs(visited[:], 0, 0, 1)
#     return -1 if answer==99999999 else answer

from collections import deque
def solution(maps):
    queue = deque([[0,0,1]])
    visited = [[0]*len(maps[0]) for _ in range(len(maps))]
    while queue:
        n = queue.popleft()                          #y,x
        if visited[n[0]][n[1]]==1:
            continue
        visited[n[0]][n[1]]=1
        count = n[2]
        if n[0] == len(maps)-1 and n[1] == len(maps[0])-1:
            return count
        else:
            if n[1]-1>=0:                           #상
                if maps[n[0]][n[1]-1]==1 and visited[n[0]][n[1]-1]==0:
                    queue.append([n[0],n[1]-1, count+1])
            if n[1]+1<=len(maps[0])-1:                  #우
                if maps[n[0]][n[1]+1]==1 and visited[n[0]][n[1]+1]==0:
                    queue.append([n[0],n[1]+1, count+1])
            if n[0]+1<=len(maps)-1:               #하
                if maps[n[0]+1][n[1]]==1 and visited[n[0]+1][n[1]]==0:
                    queue.append([n[0]+1,n[1], count+1])
            if n[0]-1>=0:                           #좌
                if maps[n[0]-1][n[1]]==1 and visited[n[0]-1][n[1]]==0:
                    queue.append([n[0]-1,n[1], count+1])
    return -1


print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]), 11)
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]),-1)