def solution(priorities, location):
    answer = 0
    while len(priorities)>0:
        a = priorities[0]   #일단뺌
        del priorities[0]
        location -=1
        if len(priorities)==0:
            answer+=1
            return answer
        for i in range(len(priorities)):    #더높은거있는지 검사
            if a<priorities[i]:             #있으면 넣음
                priorities.append(a)
                break
            if i==len(priorities)-1:        #없으면 출력
                answer+=1
                if location==-1:            #출력대상이면 리턴
                    return answer
        if location == -1:                  #검사대상이 내꺼면 뒤로
            location = len(priorities)-1
print(solution([2, 1, 3, 2],1))