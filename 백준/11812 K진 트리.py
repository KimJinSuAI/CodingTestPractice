import sys
input = sys.stdin.readline
N,K,Q = map(int,input().split())

if K==1:
    for _ in range(Q):
        x,y = map(int,input().split())
        print(abs(x-y))
else:
    level = [0]
    tmp = 0

    while level[-1]<=N:
        level.append(level[-1]+K**tmp)
        tmp+=1

    def findLevel(num):
        tmp = 1
        while num>level[tmp]:
            tmp+=1
        return tmp-1

    ans = []
    for _ in range(Q):
        x,y = map(int,input().split())
        xlevel = findLevel(x)
        ylevel = findLevel(y)
        cnt = 0
        while x!=y:
            if x<y:
                y = level[ylevel-1]+(y-level[ylevel]-1)//K+1
                ylevel-=1
            else:
                x = level[xlevel-1]+(x-level[xlevel]-1)//K+1
                xlevel-=1
            cnt+=1
        ans.append(cnt)
    for cnt in ans:
        print(cnt)

