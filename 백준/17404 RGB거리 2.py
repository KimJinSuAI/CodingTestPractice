import sys
input = sys.stdin.readline

N = int(input()[:-1])
cost = []
for i in range(N):
    cost.append(list(map(int,input()[:-1].split())))

ans = sys.maxsize
for i in range(3):
    DP = [[sys.maxsize] *3 for _ in range(N)] #DP[color][num] = num건물을 color로 칠했을 때 최소 비용
    DP[0][i] = cost[0][i]
    for j in range(1,N):
        DP[j][0] = cost[j][0] +min(DP[j-1][1],DP[j-1][2])
        DP[j][1] = cost[j][1] +min(DP[j-1][0],DP[j-1][2])
        DP[j][2] = cost[j][2] +min(DP[j-1][0],DP[j-1][1])
    
    for j in range(3):
        if i!=j:
            ans = min(ans,DP[N-1][j])
        
print(ans)