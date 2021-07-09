def solution(numbers):
    answer = []
    for i in range(len(numbers)-1):
        for j in range(1,len(numbers)):
            if i==j:
                continue
            s = numbers[i]+numbers[j]
            if s not in answer:
                answer.append(s)
    return sorted(answer)
print(solution([5,0,2,7]))