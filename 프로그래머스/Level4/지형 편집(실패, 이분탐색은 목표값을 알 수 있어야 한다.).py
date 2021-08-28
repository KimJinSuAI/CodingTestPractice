#실패한 풀이
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

#다른사람의 풀이
def solution(land, P, Q):
    answer = -1
    height_dict = dict()
    for i in range(len(land)):
        for j in range(len(land)):
            if land[i][j] in height_dict:
                height_dict[land[i][j]] += 1
            else:
                height_dict[land[i][j]] = 1
    height_list = sorted(list(height_dict.keys()))
    minidx = 0
    maxidx = len(height_list)-1
    money = 0
    while minidx != maxidx:
        low_num = height_dict[height_list[minidx]]
        high_num = height_dict[height_list[maxidx]]
        if P*low_num < Q*high_num:
            money += P*low_num*(height_list[minidx+1]-height_list[minidx])
            minidx += 1
            height_dict[height_list[minidx]] += low_num
        else:
            money += Q*high_num*(height_list[maxidx]-height_list[maxidx-1])
            maxidx -= 1
            height_dict[height_list[maxidx]] += high_num

    answer = money
    return answer

#위 코드를 참고해 푼 풀이
from collections import Counter
def solution(land, P, Q):
    c = dict()
    for i in range(len(land)):
        for j in range(len(land)):
            if land[i][j] in c:
                c[land[i][j]] += 1
            else:
                c[land[i][j]] = 1
    cKeys = sorted(c.keys())
    left = 0
    right = len(cKeys)-1
    answer = 0
    while left!=right:
        mNum = c[cKeys[left]]
        MNum = c[cKeys[right]]
        if P*mNum<Q*MNum:
            answer+=P*mNum*(cKeys[left+1]-cKeys[left])
            left+=1
            c[cKeys[left]]+=mNum
        else:
            answer+=Q*MNum*(cKeys[right]-cKeys[right-1])
            right-=1
            c[cKeys[right]]+=MNum
    return answer

print(solution([[1, 2], [2, 3]],3,2))
print(solution([[4, 4, 3], [3, 2, 2], [ 2, 1, 0 ]], 5, 3))