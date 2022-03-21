import sys
input = sys.stdin.readline

N,M = map(int,input().split())
arr = set()
for i in range(N):
    arr.add(input()[:-1])
ans = 0 

for _ in range(M):
    tmp = input()[:-1]
    if tmp in arr:
        ans +=1

print(ans)
