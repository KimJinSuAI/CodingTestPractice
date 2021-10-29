import sys
input = sys.stdin.readline

ans = []
count = 0
while(True):
    try:
        M,P,L,E,R,S,N = map(int,sys.stdin.readline().split())
        count+=1 
        for i in range(N):
            L, P, M = M*E, L//R, P//S
        ans.append(M)
    except :
        for i in range(count):
            print(ans[i])
        break