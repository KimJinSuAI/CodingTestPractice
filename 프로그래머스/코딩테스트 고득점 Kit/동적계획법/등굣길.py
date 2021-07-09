memo=[]
def dp(x, y, m, n, puddles):
    if memo[y][x]!=0:
        return memo[y][x]
    elif [x+1,y+1] in puddles:
        return 0
    elif x==m-1 and y==n-1:
        return 1
    elif x==m-1:
        memo[y][x] = dp(x, y+1, m, n, puddles)
    elif y==n-1:
        memo[y][x] = dp(x+1, y, m, n, puddles)
    else:
        memo[y][x] = dp(x, y+1, m, n, puddles) + dp(x+1, y, m, n, puddles)
    return memo[y][x]

def solution(m, n, puddles):
    global memo
    memo = [[0]*m for _ in range(n)]
    return dp(0,0,m,n,puddles)%1000000007

# print(solution(4,3,[[2,2]]))
# print(solution(3,3,[[2,2]]))
# print(solution(4,1,[[2,1],[2,2]]))