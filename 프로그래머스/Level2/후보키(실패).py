from itertools import combinations
def isDuplicated(j, relation):         #중복검사
    for k in range(0, len(relation)-1):
        for l in range(k+1,len(relation)):
            tup1=[relation[k][x] for x in j]
            tup2 = [relation[l][x] for x in j]
            if tup1==tup2:
                return False
    return True
    
def isCandidate(m,j):
    count=0
    for i in j:
        if i in m:
            count+=1
    return False if count!=len(m) else True

def solution(relation):
    candidate = []
    for i in range(1,len(relation[0])+1):
        for j in list(map(list,combinations(range(len(relation[0])),i))):
            for m in candidate:
                if isCandidate(m,j):
                    break
            else:
                if isDuplicated(j, relation):
                    candidate.append(j)
    answer = 0
    return len(candidate)

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))