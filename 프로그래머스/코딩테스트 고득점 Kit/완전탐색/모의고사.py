def solution(answers):
    a = {
        1:[[1,2,3,4,5],-1,0],#규칙,인덱스,정답수
        2:[[2,1,2,3,2,4,2,5],-1,0],
        3:[[3,3,1,1,2,2,4,4,5,5],-1,0]}

    for i in range(len(answers)):
        a[1][1]=a[1][1]+1
        a[2][1]=a[2][1]+1
        a[3][1]=a[3][1]+1
        if a[1][0][a[1][1]]==answers[i]:
            a[1][2]=a[1][2]+1
        if a[2][0][a[2][1]]==answers[i]:
            a[2][2]=a[2][2]+1
        if a[3][0][a[3][1]]==answers[i]:
            a[3][2]=a[3][2]+1
        if a[1][1]==len(a[1][0])-1:
            a[1][1]=-1
        if a[2][1]==len(a[2][0])-1:
            a[2][1]=-1
        if a[3][1]==len(a[3][0])-1:
            a[3][1]=-1

    answer = []
    a = sorted(a.items(),reverse=True, key = lambda x: x[1][2])
    for i in a:
        if i[1][2]== a[0][1][2]:
            answer.append(i[0])

    return answer
print(solution([1,2,3,4,5]))