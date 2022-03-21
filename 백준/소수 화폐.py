import sys
input = sys.stdin.readline
N = int(input())

DP = [0 for _ in range(N+1)]
DP[0]=1

def isprime(num):
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True

primes = []
mod = 123456789
for num in range(2,N+1):
    if isprime(num):
        primes.append(num)

for p in primes:
    for i in range(p, N+1):
        DP[i] = (DP[i]+DP[i-p])%mod
print(DP[N])


# import sys
# input = sys.stdin.readline

# DP = [[],[]]

# def isprime(num):
#     for i in range(2,int(num**0.5+1)):
#         if num%i==0:
#             return False
#     return True

# n = int(input())
# prime = []

# for i in range(2, n+1):
#     if isprime(i):
#         prime.append(i)

# dp = [0 for _ in range(n+1)]
# dp[0] = 1
# for p in prime:
#     for i in range(p, n+1):
#         dp[i] = (dp[i] + dp[i-p]) % 123456789
            
# print(dp[n])