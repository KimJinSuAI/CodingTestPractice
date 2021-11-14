import sys
input = sys.stdin.readline
A = input()[:-1]
B = input()[:-1]
DP = [[""]*(len(B)+1) for _ in range(len(A)+1)] #DP[i][j] = A의 i까지 B의 j까지 문자열로 만들 수 있는 공통 부분 수열
for i in range(1,len(A)+1):
    for j in range(1,len(B)+1):
        if A[i-1]==B[j-1]:
            DP[i][j] = DP[i-1][j-1]+A[i-1]
        else:
            if len(DP[i-1][j])>len(DP[i][j-1]):
                DP[i][j] = DP[i-1][j]
            else:
                DP[i][j] = DP[i][j-1]

s = DP[-1][-1]
print(len(s))
if len(s)!=0:
    print(s)
