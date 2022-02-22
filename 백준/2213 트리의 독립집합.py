import sys
from functools import lru_cache
sys.setrecursionlimit(10**5+10**4)
input = sys.stdin.readline

n = int(input())
w = [0]+list(map(int,input().split()))
tree = [[] for _ in range(n+1)]
dp = [[0,0] for _ in range(n+1)]    #dp[i][0]: i 노드를 포함하지 않았을 때
visited = [False for _ in range(n+1)] #dp[i][1] i노드를 포함했을 때
nums = [[[],[]] for _ in range(n+1)]


for _ in range(n-1):
        a,b = map(int,input().split())
        tree[a].append(b)
        tree[b].append(a)

def dfs(i):
    visited[i] = True
    dp[i][1] = w[i]
    nums[i][1].append(i)

    for node in tree[i]:
        if not visited[node]:
            dfs(node)
            dp[i][1] += dp[node][0]
            nums[i][1] += nums[node][0]

            if dp[node][1] <= dp[node][0]:
                dp[i][0] += dp[node][0]
                nums[i][0] += nums[node][0]
            else:
                dp[i][0] += dp[node][1]
                nums[i][0] += nums[node][1]

dfs(1)
i = 0 if dp[1][0]>=dp[1][1] else 1
print(dp[1][i])
print(*sorted(nums[1][i]))