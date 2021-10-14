from collections import deque
def solution(n, m, x, y, queries):
    d = [(0,-1),(0,1),(-1,0),(1,0)]
    for i in range(len(queries)):
        if queries[i][0] == 0:
            queries[i][0] = 1
        elif queries[i][0] == 1:
            queries[i][0] = 0
        elif queries[i][0] == 2:
            queries[i][0] = 3
        elif queries[i][0] == 3:
            queries[i][0] = 2
    queries = queries[::-1]

    Q = set((x,y))
    for dir, dis in queries:
        dy, dx = d[dir]
        dy, dx = dy*dis, dx*dis
        tmp = set()
        for idx in range(len(Q)):
            sy,sx = Q[idx]
            nexty, nextx = sy+dy, sx+dx
            if dir == 2 and nexty<=0:
                nexty = 0
                for i in range(nexty,sy+1):
                    tmp.add((i,sx))
            elif dir == 3 and nexty>=n-1:
                nexty = n-1
                for i in range(sy,nexty+1):
                    tmp.add((i,sx))

            elif dir == 0 and nextx<=0:
                nextx = 0
                for i in range(nextx,sx+1):
                    tmp.add((sy,i))
            elif dir == 1 and nextx>=m-1:
                nextx = m-1
                for i in range(sx,nextx+1):
                    tmp.add((sy,i))
            Q += tmp
            Q.remove((sy,dx))
            Q.add((nexty,nextx))
        
        
    return len(Q)

# print(solution(2, 2, 0, 0, [[2, 1], [0, 1], [1, 1], [0, 1], [2, 1]]), 4)
print(solution(2, 5, 0, 1, [[3, 1], [2, 2], [1, 1], [2, 3], [0, 1], [2, 1]]), 2)