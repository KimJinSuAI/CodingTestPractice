def solution(progresses, speeds):
    answer = []
    while len(progresses)>0:                                        #할거남았으면
        count = 0
        delList = []

        for i in range(len(progresses)):                            #더하기
            progresses[i]+=speeds[i]

        for j in range(len(progresses)):                            #100넘었는지검사 후 삭제리스트추가
            if progresses[j]>=100:
                count+=1
                delList.append([progresses[j],speeds[j]])
            else:                                                   #안넘은거있으면 break
                break

        for k,l in delList:                                         #삭제할거삭제
            progresses.remove(k)
            speeds.remove(l)

        if count>0:                                                 #일별배포수 추가
            answer.append(count)
    return answer

print(solution([93, 30, 55],[1, 30, 5]))