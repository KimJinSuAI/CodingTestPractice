from collections import deque
def solution(N, road, K):
    dic = {}
    visited = [0]*(N+1)
    for i in road:
        dic[i[0]] = dic.get(i[0],[])+[[i[1],i[2]]]
        dic[i[1]] = dic.get(i[1],[])+[[i[0],i[2]]]
    
    queue = deque([[1,0]])
    visited[1]=-1
    while queue:
        now = queue.popleft()
        for i in dic[now[0]]:
            if visited[i[0]]==0 or visited[i[0]]>(now[1]+i[1]):
                visited[i[0]] = now[1]+i[1]  ##
                queue.append([i[0], now[1]+i[1]])

    return len([i for i in range(N) if visited[1:][i]<=K])

print(solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3))
print(solution(6,[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]],4))