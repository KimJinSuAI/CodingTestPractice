from collections import Counter
def solution(N, stages):
    user = len(stages)
    c = Counter(stages)
    answer = {}
    for i in range(1,N+1):
        if user!=0:
            answer[i]=c[i]/user
            user-=c[i]
        else:
            answer[i]=0
    
    return sorted(answer, reverse=True ,key=lambda x:(answer[x],-x))
print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))