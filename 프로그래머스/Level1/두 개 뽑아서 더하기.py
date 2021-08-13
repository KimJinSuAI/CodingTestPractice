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

from itertools import combinations
def solution(numbers):
    answer = set()
    for i in combinations(numbers,2):
        answer.add(i[0]+i[1])
    return sorted(answer)
print(solution([5,0,2,7]))