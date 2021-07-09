def solution(n):
    answer = 0
    for i in range(1,n+1):
        k = i
        summ = 0
        while summ<n:
            summ+=k
            k+=1
        if summ==n:
            answer +=1
    return answer
    
print(solution(15))