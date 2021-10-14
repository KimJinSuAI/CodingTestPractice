import sys
ans = []
while True:
    N = list(map(int,sys.stdin.readline().split()))
    if N[0]==0:
        for a in ans:
            print(a)
        break
    N,squares = N[0],N[1:]
    stck = [[squares[0],1]]
    maxi = 0
    for i in range(1,N):
        now = [squares[i],1]
        count = 0
        while stck and now[0]<=stck[-1][0]:
            tmp = stck.pop()
            count+=tmp[1]
            maxi = max(maxi, tmp[0]*count)
        now[1]+=count
        stck.append(now)
    
    count = 0
    while stck:
        tmp = stck.pop()
        count+=tmp[1]
        maxi = max(maxi,tmp[0]*count)
        
    ans.append(maxi)