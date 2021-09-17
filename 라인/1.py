def solution(student, k):
    answer = 0
    tmp= 0 
    l = 0
    r = 0
    while r!=len(student) and l!=len(student):
        beforeR = r
        tmpl, tmpr=1,0
        while tmp<=k:
            if r==len(student):
                break
            tmp+=student[r]
            r+=1
            if tmp==k:
                tmpr+=1
        r-=1
        tmp-=student[r]
        while tmp>=k:
            if l==len(student):
                break
            tmp-=student[l]
            l+=1
            if tmp==k:
                tmpl+=1
        answer+=tmpl*tmpr
        startr = l
        if beforeR==startr:
            break
        l-=1

        r,l = startr, startr
        tmp = 0
        
    return answer if answer!=0 else 0
print(solution([0,1,0,0],1))
print(solution([0, 1, 0, 0, 1, 1, 0]	,2))