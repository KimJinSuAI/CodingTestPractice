import sys
N, M = list(map(int, sys.stdin.readline().split()))
m = list(map(int, sys.stdin.readline().split()))
c = list(map(int, sys.stdin.readline().split()))

dp = [[0]* (sum(c)+1) for _ in range(N)] #dp[i][c] = i까지의 앱으로 c비용으로 얻을 수 있는 최대 byte
ans = float('inf')
for i in range(N):
    for j in range(len(dp[0])):
        if i== 0 and j>=c[i]:
            dp[i][j] = m[i]
        elif j>=c[i]:
            dp[i][j] = max(dp[i-1][j], m[i]+dp[i-1][j-c[i]])#안넣었을 때, 넣었을 때
        else:
            dp[i][j] = dp[i-1][j]   #못넣음

        if dp[i][j]>=M:
            ans = min(ans,j)
print(ans)
