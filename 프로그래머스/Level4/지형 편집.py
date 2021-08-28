from collections import Counter
memo = {}
def cost(h, P, Q):
    global Land,memo
    if memo.get(h,False):
        return memo[h]
    p,q = 0,0
    for y in range(len(Land)):
        for x in range(len(Land)):
            tmp = h-Land[y][x]
            if tmp>0:
                p+=abs(tmp)
            elif tmp<0:
                q+=abs(tmp)
    memo[h] = P*p+Q*q
    return memo[h]

def solution(land, P, Q):
    global Land,memo
    Land,memo = land,{}
    s = set()
    for y in land:
        for x in y:
            s.add(x)
    l = min(s)
    r = max(s)
    while l<=r:
        mid = (l+r)//2
        lCost = cost(l,P,Q)
        rCost = cost(r,P,Q)
        if lCost>rCost:
            l = mid+1
        else:
            r = mid-1
    return cost(l,P,Q)

print(solution([[1, 2], [2, 3]],3,2))
print(solution([[4, 4, 3], [3, 2, 2], [ 2, 1, 0 ]], 5, 3))