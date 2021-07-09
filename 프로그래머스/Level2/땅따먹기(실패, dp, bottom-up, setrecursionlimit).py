import sys
sys.setrecursionlimit(1000001)
memo = [[]]
def dp(land, now, level):
    global memo
    if memo[level][now] !=-1:
        return memo[level][now]
    elif level == (len(land)-1):
        return land[level][now]
    else:
        memo[level][now] = max([dp(land, i, level+1) for i in range(4) if i !=now]) + land[level][now]
        return memo[level][now]




def solution(land):
    global memo
    memo = [[-1]*4 for _ in range(len(land))]
    return max(dp(land, 0, 0), dp(land, 1, 0), dp(land, 2, 0), dp(land, 3, 0))


def solution(land):
    answer = 0
    n = len(land)

    for i in range(1, n):
        land[i][0] += max(land[i-1][1], land[i-1][2], land[i-1][3])
        land[i][1] += max(land[i-1][0], land[i-1][2], land[i-1][3])
        land[i][2] += max(land[i-1][0], land[i-1][1], land[i-1][3])
        land[i][3] += max(land[i-1][0], land[i-1][1], land[i-1][2])


    answer = max(land[n-1])

    return answer

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]), 16)
print(solution([[9, 5, 2, 3], [9, 8, 6, 7], [8, 9, 7, 1], [100, 9, 8, 1]] ))
print(solution([[4, 3, 2, 1], [2, 2, 2, 1], [6, 6, 6, 4], [8, 7, 6, 5]]), 20)