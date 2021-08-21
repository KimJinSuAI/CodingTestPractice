import sys
sys.setrecursionlimit(10000)
def dp(n):
    a,b = 2,3
    for i in range(3,n+1):
        if i%2==0:
            a,b = b,a+b
        else:
            a,b = b,a+2*b
    return b

def solution(n):
    if n%2!=0: return 0
    else: return dp(n)%1000000007


print(solution(14), 7953)
print(solution(12), 2131)
print(solution(10),571)
print(solution(8),153)
print(solution(6),41)
print(solution(4),11)
print(solution(2),3)