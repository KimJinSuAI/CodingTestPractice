def solution(n, results):
    adj = {}
    visited = [[0]*(n+1) for i in range((n+1))] 
    stack = []
    for result in results:
        adj[result[0]] = adj.get(result[0],[])+[result[1]]

    for i in range(1,n+1):
        stack.append(i)
        while stack:
            tmp = stack.pop()
            if visited[i][tmp]==0:
                visited[i][tmp]=1
                visited[tmp][i]=1
                for j in adj.get(tmp,[]):
                    stack.append(j)

    count = 0
    for i in visited:
        if sum(i)==n:
            count+=1
    return count

print(solution(1, [[1,1]]),1)
print(solution(4,[[1,3],[2,3],[4,3]]),1)
print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]), 2)
print(solution(4, [[1,2],[1,4],[3,1]]),2)
