import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
a = [0]+list(map(int,input()[:-1].split()))
DP = [0 for i in range(N+1)]#DP[i] = a[i]가 들어가는 가장 긴 부분 수열의 길이
tmp = [-1000000001]#tmp[i] = 길이가 i인 부분 수열의 최저값


maxi = 0
for i in range(1,N+1):
    if a[i]>tmp[-1]:
        tmp.append(a[i])
        DP[i] = len(tmp)-1
        maxi = DP[i]
    else:
        DP[i] = bisect_left(tmp,a[i])
        tmp[DP[i]] = a[i]
print(maxi)

tmp2 = []
for i in range(N,0,-1):
    if DP[i]==maxi:
        tmp2.append(a[i])
        maxi-=1

print(*tmp2[::-1])

