memo = []
def dp(triangle,now):
    val = triangle[now[0]][now[1]]
    if memo[now[0]][now[1]]!=-1:
        return memo[now[0]][now[1]]
    elif now[0]==len(triangle)-1:
        return val
    else:
        memo[now[0]][now[1]] = val+max(dp(triangle,[now[0]+1,now[1]]), dp(triangle, [now[0]+1,now[1]+1]))
        return memo[now[0]][now[1]]

def solution(triangle):
    global memo 
    memo= [[-1]*len(triangle) for i in range(len(triangle))]
    return dp(triangle,[0,0])

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))