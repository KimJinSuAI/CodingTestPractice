import sys
input = sys.stdin.readline

d = [[0,-1],[0,1],[-1,0],[1,0]]


N,M,K = map(int, input().split())
board = []
for i in range(N):
    board.append(input()[:-1])
word = input()

dp = [[[-1 for a in range(M)] for b in range(N)] for c in range(len(word))]
def dfs(idx,y,x):
    if dp[idx][y][x]!=-1:
        return dp[idx][y][x]
    else:
        if idx==len(word)-1:
            dp[idx][y][x] = 1
        else:
            dp[idx][y][x] = 0
            for i in range(1,K+1):
                for dy,dx in d:
                    ny,nx = y+dy*i,x+dx*i
                    if -1<ny<N and -1<nx<M and board[ny][nx]==word[idx]:
                        dp[idx][y][x] += dfs(idx+1,ny,nx)
    return dp[idx][y][x]
        
cnt = 0
for y in range(N):
    for x in range(M):
        if board[y][x] == word[0]:
            cnt += dfs(1,y,x)

print(cnt)
