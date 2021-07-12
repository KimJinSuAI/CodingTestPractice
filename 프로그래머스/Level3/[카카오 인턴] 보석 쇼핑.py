def solution(gems):
    answer = [0,0]
    kind = len(set(gems))
    min = 0
    max = len(gems)
    while min<max:
        mid = (min+max)//2
        if kind == len(set(gems[:mid])):
            max = mid
        else:
            min = mid+1
    max = (min+max)//2
    answer[1] = max
    min = 0
    maxtmp = max
    while min<maxtmp:
        mid = (min+maxtmp)//2
        if kind==len(set(gems[mid:max])):
            min = mid+1
        else:
            maxtmp = mid
    answer[0] = min
        
    return answer


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPxPHIRE", "DIA"]), [3,7])
print(solution(["AA", "AB", "AC", "AA", "AC"]), [1,3])
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["A","A","A","B","B"]),[3,4])
print(solution(["A"]),[1,1])
print(solution(["A","B","B","B","B","B","B","C","B","A"]),[8,10])