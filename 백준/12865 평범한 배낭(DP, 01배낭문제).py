N, K = list(map(int,input().split()))
stuffs = []
for i in range(N):
    stuffs.append(tuple(map(int,input().split())))

dp = [[0] * (K+1) for _ in range(len(stuffs))]    #dp[i][w] = i까지 물건으로 w무게 만들었을때 최대 가치
for i in range(len(stuffs)):
    for w in range(K+1):
        if i == 0:
            if stuffs[i][0]<=w:
                dp[i][w] = stuffs[i][1]
        else:
            if stuffs[i][0]<=w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-stuffs[i][0]]+stuffs[i][1])
            else:
                dp[i][w] = dp[i-1][w]
print(dp[-1][-1])