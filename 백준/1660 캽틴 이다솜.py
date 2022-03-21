import sys
input = sys.stdin.readline

N = int(input())
ans = 0
arr = [1]
k = 2
while arr[-1]<=N:
    arr.append(arr[-1]+k)
    k+=1
arr2 = [0]

for i in range(len(arr)):
    arr2.append(arr[i]+arr2[-1])

DP = [sys.maxsize for _ in range(300001)]
DP[0] = 0

for i in arr2[1:]:
    for j in range(i,N+1):
        DP[j] = min(DP[j], 1+DP[j-i])


print(DP[N])