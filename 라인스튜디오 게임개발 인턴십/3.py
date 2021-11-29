from collections import deque
def solution(r, c):
    d = [[0,-1],[1,0],[0,1],[-1,0],[0,-1],[-1,0],[0,1],[1,0]]
    visited = [[False]*c for _ in range(r)]
    Q = deque()
    Q.append([0,c-1,0])
    cnt = 1
    while Q:
        y,x,idx = Q.popleft()
        if not visited[y][x]:
            visited[y][x] = cnt
            cnt+=1
            if idx in [3,7]:
                idx=(idx+1)%8
            dy,dx = d[idx]
            ny,nx = y+dy,x+dx
            if -1<ny<r and -1<nx<c and not visited[ny][nx]:
                    Q.append([ny,nx,idx])
            else:
                idx= (idx+1)%8
                dy,dx = d[idx]
                ny,nx = y+dy,x+dx
                if -1<ny<r and -1<nx<c and not visited[ny][nx]:
                    Q.append([ny,nx,idx])
                else:
                    break
    return visited
print(solution(5,4))