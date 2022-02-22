import sys
input = sys.stdin.readline


N = int(input())
DP = [[] for _ in range(N+1)]
i=1
while i!=N+1:
    if not DP[i]:
        DP[i] = [i]
    tmp = []
    if not i%3:
        tmp.append(DP[i//3])
    if not i%2:
        tmp.append(DP[i//2])
    if i-1:
        tmp.append(DP[i-1])
    if tmp:
        tmp.sort(key = lambda x: len(x))
        DP[i]+=tmp[0]
    i+=1

print(len(DP[N])-1)
print(*DP[N])