import sys
input = sys.stdin.readline

R,C = map(int, input().split())
board = []
for _ in range(R):
    board.append(input())

visited = [False for _ in range(26)]
ans = 0
d = [(-1,0),(1,0),(0,-1),(0,1)]
def dfs(cnt,y,x):
    global ans
    here = ord(board[y][x])-65
    if not visited[here]:
        visited[here] = True
        ans = max(ans,cnt)
        for dy,dx in d:
            ny,nx = dy+y, dx+x
            if -1<ny<R and -1<nx<C:
                next = ord(board[ny][nx])-65
                if not visited[next]:
                    dfs(cnt+1,ny,nx)
        visited[here] = False

dfs(1,0,0)
print(ans)