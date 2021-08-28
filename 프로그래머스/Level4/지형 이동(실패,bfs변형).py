import heapq
def solution(land, height):
    visited = [[False]*len(land) for _ in range(len(land))]
    d = [[-1,0],[1,0],[0,-1],[0,1]]
    Q = [[0,0,0]]
    answer = 0
    while Q:
        cost,y,x = heapq.heappop(Q)
        if visited[y][x]:
            continue
        visited[y][x] = True
        if cost>height:
            answer+=cost
        for dy,dx in d:
            tmpy, tmpx = y+dy, x+dx
            if 0<=tmpy<len(land) and 0<=tmpx<len(land) and not visited[tmpy][tmpx]:
                heapq.heappush(Q,[abs(land[y][x]-land[tmpy][tmpx]),tmpy,tmpx])
    return answer

# print(solution([[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]],3))
print(solution([[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]], 1))