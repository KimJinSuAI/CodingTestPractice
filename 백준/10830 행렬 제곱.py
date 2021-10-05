import sys
N, B = list(map(int,sys.stdin.readline().split()))
A = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
def mul(A,B):
    tmp = [tmp for tmp in zip(*B)]
    newA = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            newA[i][j] = sum(a*b%1000 for a,b in zip(A[i],tmp[j]))%1000
    return newA
    
def dp(A,B):
    if B==1:
        return A
    else:
        if B%2:
            return mul(dp(mul(A,A),B//2),A)
        else:
            return dp(mul(A,A),B//2)

A = dp(A,B)
for y in range(N):
    tmp = ""
    for x in range(N):
        tmp += str(A[y][x]%1000)+" "
    print(tmp[:-1])