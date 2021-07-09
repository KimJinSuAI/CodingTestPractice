import math
def solution(n):
    answer = 0
    for i in range(2, n+1):
        for j in range(2, int(math.sqrt(i)+1)):
            if i%j==0:
                break
        else:
            answer+=1
    return answer

def solution(n):            #에라토스테너스의 체
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)
print(solution(5))
print(solution(10))