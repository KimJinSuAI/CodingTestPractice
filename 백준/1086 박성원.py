import sys
from itertools import permutations
import math
input = sys.stdin.readline

N = int(input()[:-1])
arr = []
for i in range(N):
    arr.append(input()[:-1])
K = int(input()[:-1])
DP = [[-1]* K for _ in range(1<<N)]

ln = [1 for _ in range(51)]
ln2 = []
for i in range(1,51):
    ln[i] = (ln[i-1]*10)%K

for i in range(len(arr)):
    ln2.append([len(arr[i]),int(arr[i])%K])

def dp(v,num):
    if DP[v][num]==-1:
        DP[v][num] = 0
        if v==(1<<N)-1 :
            if not num%K:
                DP[v][num] = 1
        else:
            for i in range(N):
                if not v&(1<<i):
                    DP[v][num] += dp(v|(1<<i), (num*ln[ln2[i][0]]+ln2[i][1])%K)
    return DP[v][num]

p = dp(0,0)
q = math.factorial(N)


gcd = math.gcd(p,q)
p//=gcd
q//=gcd
print(p, end='/')
print(q)