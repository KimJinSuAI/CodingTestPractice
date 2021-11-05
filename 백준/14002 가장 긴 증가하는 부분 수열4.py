import sys
from collections import deque
input = sys.stdin.readline

N = int(input()[:-1])
arr = list(map(int, input().split()))
DP = []
for i in range(N):
    maxi = [-1,-1]
    for j in range(i):
        if arr[i]>DP[j][-1] and maxi[0]<len(DP[j]):
            maxi = [len(DP[j]),j]
    if maxi[0]==-1:
        DP.append([arr[i]])
    else:
        DP.append(DP[maxi[1]]+[arr[i]])

DP.sort(key=lambda x: len(x))
print(len(DP[-1]))
for i in DP[-1]:
    print(i, end=" ")
print()
