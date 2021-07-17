memo = {}
def dp(n, now, target):
    key = str(n)+","+str(now)+","+str(target)
    tmp = memo.get(key, [])
    if tmp:
        return tmp
    else:
        if n==1:
            return [[now, target]]
        memo[key] = dp(n-1, now, 6-now-target)+[[now,target]]+dp(n-1, 6-now-target, target)
        return memo[key]

def solution(n):
    return dp(n, 1, 3)

print(solution(2))