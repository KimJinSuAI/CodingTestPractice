import sys,copy
def dp(files, DP):          #비용, 총합
    for i in range(len(DP)):
        for j in range(len(DP)-i-1):
            DP[j][j+i+1] = min([DP[j][k]+DP[k+1][j+i+1] for k in range(j,j+i+1)])+A[j+i+2]-A[j]
    return DP[0][len(DP)-1]




answer = []
T = int(sys.stdin.readline())
for t in range(T):
    K = int(sys.stdin.readline())
    files = list(map(int,sys.stdin.readline().split()))

    DP = [[0]*K for _ in range(K)]
    A = [0]
    for i in range(K):
        A.append(A[i]+files[i])
    answer.append(dp(files, DP))

for ans in answer:
    print(ans)