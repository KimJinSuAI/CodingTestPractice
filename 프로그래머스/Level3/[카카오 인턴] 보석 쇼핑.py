from collections import Counter
from collections import deque
def solution(gems):
    kind = len(set(gems))
    l, r = 0, 0
    currentList = deque([gems[0]])
    answer = [0,100000]
    while r!=len(gems):
        nowCounter = Counter(currentList)
        while len(nowCounter)!= kind:
            r+=1
            if r==len(gems):
                return answer
            currentList.append(gems[r])
            nowCounter[gems[r]] = nowCounter.get(gems[r],0)+1

        while len(nowCounter)==kind:
            tmp = currentList.popleft()
            if nowCounter[tmp]==1:
                del nowCounter[tmp]
            else:
                nowCounter[tmp]-=1
            l+=1
        if answer[1]-answer[0]>r+1-l:
            answer = [l,r+1]
    return answer


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPxPHIRE", "DIA"]), [3,7])
print(solution(["AA", "AB", "AC", "AA", "AC"]), [1,3])
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["A","A","A","B","B"]),[3,4])
print(solution(["A"]),[1,1])
print(solution(["A","B","B","B","B","B","B","C","B","A"]),[8,10])