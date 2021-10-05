import sys
N, K = list(map(int,sys.stdin.readline().split()))

def power(a,b):
    if b==0:
        return 1
    else:
        if b % 2:
            return (power(a,b//2)**2*a) % p
        else:
            return (power(a,b//2)**2) % p

p = 1000000007
fact = [1 for _ in range(N+1)]
for i in range(1,N+1):
    fact[i] = (fact[i-1]*i) % p
tmp1 = fact[N]
tmp2 = (fact[K]*fact[N-K])%p
# 페르마의 소정리에 의해
# comb(n,k)%p = (n!//(k!*(n-k!)))%p = (n!*(k!*(n-k)!)^-1)%p = n!%p*((k!*(n-k)!)^p-2)%p

print((tmp1 * power(tmp2,p-2))%p )