def isCross(now,before,arrow):
    if arrow == 1:
        tmp1 = (now[0]-1,now[1])
        tmp2 = (now[0],now[1]+1)
        if memo.get(tmp1,False):
            if tmp2 in memo[tmp1]:
                return 1
    elif arrow == 3:
        tmp1 = (now[0]-1,now[1])
        tmp2 = (now[0],now[1]-1)
        if memo.get(tmp1,False):
            if tmp2 in memo[tmp1]:
                return 1
    elif arrow == 5:
        tmp1 = (now[0]+1,now[1])
        tmp2 = (now[0],now[1]-1)
        if memo.get(tmp1,False):
            if tmp2 in memo[tmp1]:
                return 1
    elif arrow == 7:
        tmp1 = (now[0]+1,now[1])
        tmp2 = (now[0],now[1]+1)
        if memo.get(tmp1,False):
            if tmp2 in memo[tmp1]:
                return 1
            

    return 0

def solution(arrows):
    global memo
    answer = 0
    d = [(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1)]
    memo = {}
    now = [0,0]
    memo[tuple(now)] = set()
    for arrow in arrows:
        before = now[:]
        now[0]+=d[arrow][0]
        now[1]+=d[arrow][1]
        beforeKey = tuple(before)
        nowkey = tuple(now)
        if not memo.get(nowkey,False):                  #처음간다면
            memo[nowkey] = set()
            memo[nowkey].add(beforeKey)
            memo[beforeKey].add(nowkey)
            answer+=isCross(now,before,arrow)
            
        else:                                           #돌아왔다면
            if beforeKey not in memo[nowkey]:           #왔던길이 아니라면
                memo[nowkey].add(beforeKey)
                memo[beforeKey].add(nowkey)
                answer+=1
                answer+=isCross(now,before,arrow)
                
    return answer
print(solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]))
print(solution([6, 5, 2, 7, 1, 4, 2, 4, 6]))
print(solution([5, 2, 7, 1, 6, 3]))
print(solution([6, 2, 4, 0, 5, 0, 6, 4, 2, 4, 2, 0]))
print(solution([6, 0, 3, 0, 5, 2, 6, 0, 3, 0, 5]))