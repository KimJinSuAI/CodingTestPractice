def snail(index, now, n, answer, x):
    j=0                     #index = 시작인덱스, now = 시작값, n=n, answer = 배열, x=반복횟수
    k=0
    for j in range(n):      # j = 좌측하향용 변수
        now+=1
        index+=j+2*x
        answer[index]=now
    if now==len(answer):
        return answer
    for k in range(1,n):  # k = 하단용 변수
        now+=1
        index+=1
        answer[index]=now
    if now==len(answer):
        return answer
    for l in range(n,2,-1):   #l = 우측상향용 변수
        now+=1
        index-=(l+2*x)
        answer[index]=now
    if now== len(answer):
        return answer
    else: 
        x+=1
        return snail(index, now, n-3, answer,x)
def solution(n):
    answer = [0]*(n*(n+1)//2)
    return snail(0, 0, n, answer, 0)

print(solution(6))