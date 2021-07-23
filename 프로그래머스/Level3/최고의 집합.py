import math
def solution(n, s):
    x = s/n
    if x<1:
        return [-1]
    else:
        flr = math.floor(x)
        tmp = s-flr*n
        ceil = [flr+1 for _ in range(tmp)]
        answer = [flr for _ in range(n-tmp)]
        return answer+ceil

# print(solution(4,7))
print(solution(2,1))