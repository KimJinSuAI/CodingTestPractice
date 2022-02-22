import sys
input = sys.stdin.readline
inp = list(map(int,input().split()))
N, P = inp[0], inp[1:]
d = [(0,-1),(0,1),(1,0),(-1,0)]
visited = [[False for i in range(2*N+1)] for j in range(2*N+1)]

def dfs(dis,p,y,x):
    ans = 0
    if not visited[y][x]:
        if dis!=N:
            visited[y][x] = True
            for i in range(4):
                if P[i]!=0:
                    pcopy = p
                    dy,dx = d[i]
                    ny,nx = y+dy,x+dx
                    ans+=dfs(dis+1,pcopy*P[i]/100,ny,nx)
            visited[y][x] = False
        else:
            return p
    return ans
print(dfs(0,1,N,N))
