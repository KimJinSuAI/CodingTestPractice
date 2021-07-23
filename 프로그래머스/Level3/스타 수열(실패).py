from itertools import combinations
def isStarSeq(s):
    x = [{s[i],s[i+1]} for i in range(0,len(s),2)]
    tmp = x[0]
    for a in x:
        if len(a)!=2:
            return False
        tmp = tmp & a
        if len(tmp)==0:
            return False
    return True

def solution(a):
    if len(a)<4:
        return 0
    mx = 4
    found = True
    while found:
        for c in list(combinations(a,mx)):
            if isStarSeq(c):
                mx+=2
                break
        else:
            found = False
    mx-=2    
    return mx

    # 조건식 추가하여 성공
# Max_time = 408.39 ms
# Memory = 91.7 MB
from collections import defaultdict
def solution(a):
    dic = defaultdict(list)
    for i, v in enumerate(a):
        dic[v].append(i)

    l = len(a)
    answer = 0
    for k, v in dic.items():
        if len(v) <= answer // 2:
            continue
        else:
            now = a.copy()
            cnt = 0
            for j in v:
                if j > 0 and now[j-1] != k:
                    now[j-1] = k
                    cnt += 2
                elif j < l-1 and now[j+1] != k:
                    now[j+1] = k
                    cnt += 2
            answer = max(answer, cnt)
    return answer


print(solution([0,3,3,0,7,2,0,2,2,0]))