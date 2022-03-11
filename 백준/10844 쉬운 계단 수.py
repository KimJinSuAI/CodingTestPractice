import sys
input = sys.stdin.readline
N = int(input())
DP = [[0 for x in range(10)] for y in range(N+1)]
for i in range(1,10):
    DP[1][i] = 1
for i in range(2,N+1):
    for j in range(10):
        if j==0:
            DP[i][j] = DP[i-1][j+1] %1e9
        elif j==9:
            DP[i][j] = DP[i-1][j-1] %1e9
        else:
            DP[i][j] = (DP[i-1][j-1]+DP[i-1][j+1])%1e9
        DP[i][j] = int(DP[i][j])
print(int(sum(DP[N])%1e9))