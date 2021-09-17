#이분탐색

def solution(a, b, g, s, w, t):
    N = len(g)
    l = 0
    r = (a+b)*max(t)*2
    while l<r:
        mid = (l+r)//2
        gold = 0
        silver = 0
        goldSilver = 0
        for i in range(N):
            tmp = mid//t[i]
            workNum = tmp//2+tmp%2
            gold += min(g[i], w[i]*workNum)
            silver += min(s[i], w[i]*workNum)
            goldSilver += min(g[i]+s[i], w[i]*workNum)
        if a>gold or b>silver or a+b>goldSilver:
            l = mid+1
        else:
            r = mid
    return r


        

# print(solution(	10, 10, [100], [100], [7], [10]))
print(solution(90,500,[70,70,0],[0,0,500],[100,100,2],[4,8,1]))