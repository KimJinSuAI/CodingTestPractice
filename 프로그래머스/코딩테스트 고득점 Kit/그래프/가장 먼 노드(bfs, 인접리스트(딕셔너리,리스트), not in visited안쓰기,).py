from collections import deque
def solution(n, edge):
    queue = deque([[1,0]])                #자신, 계층
    visited = [0]*(n+1)
    count = [0,0]                         #계층, 개수
    adj = {}                              #인접리스트화1 딕셔너리
    for e in edge:
        adj[e[0]] = adj.get(e[0],[])+[e[1]]
        adj[e[1]] = adj.get(e[1],[])+[e[0]]
    # adj = [[] for _ in range(n+1)]
    # for e in edge:                        #인접리스트화2 리스트
    #     adj[e[0]].append(e[1])
    #     adj[e[1]].append(e[0])

    while queue:
        n = queue.popleft()
        if visited[n[0]] ==0:               #not in visited는 O(n)이다.. RandomAcess는 O(1)
            visited[n[0]] = 1
            
            if n[1]>count[0]:
                count=[n[1],1]
            elif n[1]==count[0]:
                count[1]=count[1]+1

            for i in adj[n[0]]:             #인접리스트만큼만 돌기 (Random Access) O(n(e))<<O(E)
                queue.append([i,n[1]+1])
            # for i in edge[:]:             #간선 다도는방법.. 간선개수가 커지면 복잡도매우증가 O(E)
            #     if i[0]==n[0]:
            #         queue.append([i[1],n[1]+1])
            #         edge.remove(i)
            #     elif i[1]==n[0]:
            #         queue.append([i[0],n[1]+1])
            #         edge.remove(i)

    return count[1]

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))