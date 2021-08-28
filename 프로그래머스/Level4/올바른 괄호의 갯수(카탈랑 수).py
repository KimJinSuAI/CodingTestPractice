# 카탈랑 수
def dp(l, r):
    if l<0 or r<0 or l<r:
        return 0
    elif l==0 and r==0:
        return 1
    else: 
        return dp(l-1,r)+dp(l,r-1)
def solution(n):
    return dp(n,n)

from math import factorial
def solution(n):
    return factorial(2*n)//(factorial(n)*factorial(n)*(n+1))

print(solution(2), 2)
print(solution(3), 5)
print(solution(4), 14)
print(solution(5), 42)
print(solution(6), 132)