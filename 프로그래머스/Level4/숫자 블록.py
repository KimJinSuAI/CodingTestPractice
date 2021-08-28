import math
def solution(begin, end):
    answer = []
    for i in range(begin, end+1):
        for n in range(2,int(math.sqrt(i))+1):
            if i%n==0:
                if i//n>10000000:
                    continue
                else:
                    answer.append(i//n)
                    break
        else:
            answer.append(1)
    if begin==1:
        answer[0] = 0
    return answer

# print(solution(1,10))
print(solution(1000000000-10000,1000000000))
