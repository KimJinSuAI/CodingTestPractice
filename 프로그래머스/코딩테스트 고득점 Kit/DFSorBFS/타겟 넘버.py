def solution(numbers, target):
    if len(numbers)==1:
        answer = 0
        if target==numbers[0]:
            answer+=1
        if target==-1*numbers[0]:
            answer+=1
        return answer
    else:
        return solution(numbers[1:],target-numbers[0])+solution(numbers[1:],target+numbers[0])
print(solution([1,1,1,1,1],3))