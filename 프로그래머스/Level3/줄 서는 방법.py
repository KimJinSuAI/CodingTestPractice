import math
from itertools import permutations
def solution(n, k):
    answer = []
    x = list(range(1,n+1))
    tmp = n-1
    count = math.factorial(tmp)
    
    while x:
        totalcount = 0
        xIndex = 0
        while totalcount<k:
            totalcount += count
            xIndex+=1
        totalcount-=count
        if tmp!=0:
            count /=tmp
        xIndex -= 1
        k-=totalcount
        tmp-=1

        answer.append(x.pop(xIndex))

    return answer

print(solution(3,5))