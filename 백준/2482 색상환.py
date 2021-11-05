import sys
input = sys.stdin.readline

N = int(input()[:-1])
K = int(input()[:-1])

DP = [[0]*(K+1) for _ in range(N+1)]

for i in range(N+1):
    DP[i][0] = 1
    DP[i][1] = i
for i in range(2,N+1):
    for j in range(2,K+1):
        if i==N:
            DP[i][j] = DP[i-3][j-1]+DP[i-1][j]
        else:
            DP[i][j] = DP[i-2][j-1]+DP[i-1][j]
        DP[i][j]%=1000000003
print(DP[N][K])

