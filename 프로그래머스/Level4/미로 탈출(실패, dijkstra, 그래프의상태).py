import heapq
#https://sklubmk.github.io/2021/07/15/28bed7b50dc1/
def solution(n, start, end, roads, traps):
    maze = {}
    visited = [[False]*(n+1) for _ in range(1<<len(traps))]
    trapIndex = {trap:i for i,trap in enumerate(traps)}
    for road in roads:
        maze[road[0]] = maze.get(road[0],[])+[[road[1],road[2],0]]
        maze[road[1]] = maze.get(road[1],[])+[[road[0],road[2],1]]
    Q = []
    heapq.heappush(Q, (0,start,0))
    
    while Q:
        cost, node, state = heapq.heappop(Q) #비용, 노드, 상태
        if node==end:
            return cost
        now_isTrap = True if node in traps else False
        if now_isTrap:
            state ^= (1<<trapIndex[node])
        if visited[state][node]:
            continue
        visited[state][node] = True

        for nextNode in maze[node]:
            next_isTrap = True if nextNode[0] in traps else False
            if not now_isTrap and not next_isTrap:
                if nextNode[2]==1: continue
            elif now_isTrap ^ next_isTrap:   
                t = node if now_isTrap else nextNode[0]
                isOn = (state & (1<<trapIndex[t]))>>trapIndex[t]
                if isOn != nextNode[2]: continue
            else:
                isNowOn = (state & (1<<trapIndex[node]))>>trapIndex[node]
                isNextOn = (state & (1<<trapIndex[nextNode[0]]))>>trapIndex[nextNode[0]]
                if isNowOn ^ isNextOn != nextNode[2]:continue
            heapq.heappush(Q, (cost+nextNode[1], nextNode[0], state))
            

print(solution(4,1,4,[[1, 2, 1], [3, 2, 1], [2, 4, 1]],[2, 3]))