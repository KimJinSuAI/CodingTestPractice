import sys
answer = []
N = int(sys.stdin.readline())
tmp = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())

DP = [[-1]*N for _ in range(N)]

for diag in range(N):
    for i in range(N-diag):
        j = i+diag
        if i==j:
            DP[i][j] = 1
        elif i==j-1:
            DP[i][j] = 1 if tmp[i]==tmp[j] else 0
        else:
            DP[i][j] = 1 if tmp[i]==tmp[j] and DP[i+1][j-1]==1 else 0

for i in range(M):
    S,E = list(map(int,sys.stdin.readline().split()))
    S-=1
    E-=1
    answer.append(DP[S][E])
    
for ans in answer:
    print(ans)
