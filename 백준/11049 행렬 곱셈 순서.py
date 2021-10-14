import sys
N = int(sys.stdin.readline())
mat = []
for i in range(N):
    mat.append(list(map(int, sys.stdin.readline().split())))

d = [mat[0][0]]
for i in range(len(mat)):
    d.append(mat[i][1])
M = [[sys.maxsize] * (N+1) for _ in range(N+1)]

for diag in range(1,N+1):
    for i in range(1,N+2-diag):
        j = i+diag-1
        if i==j:
            M[i][j] = 0
        else:
            for k in range(i,j):
                M[i][j] = min(M[i][j], M[i][k]+M[k+1][j]+d[i-1]*d[k]*d[j])

print(M[1][N])
