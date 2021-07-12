def dfs(i, n, computers, visited):
    visited[i]=1
    for j in range(len(computers[i])):
        if computers[i][j]==1 and visited[j]==0:
            dfs(j, n, computers, visited)


def solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)]
    for i in range(n):
        if visited[i]==0:
            answer+=1
            dfs(i,n,computers,visited)
    return answer
















def solution(n, computers):
    temp = []
    for i in range(n):
        temp.append(i)  #0,1,2,3 -> 1,1,2,3

    for i in range(n):
        for j in range(n):
            if computers[i][j]:
                for k in range(n):
                    if temp[k] == temp[i]:
                        temp[k] = temp[j]
    return len(set(temp))
# print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(4,[[1,1,0,0],[1,1,1,0],[0,1,1,0],[0,0,0,1]]))