import math
def solution(n):
    one = n
    two = 0
    answer = 0
    for i in range(n):
        if one<0:
            break
        answer += math.factorial(one+two)//math.factorial(one)//math.factorial(two)
        answer %=1234567
        one-=2
        two+=1
    return answer % 1234567

print(solution(100))