def solution(nums):
    n = len(nums)/2 
    answer = 0
    if n>len(set(nums)):
        answer = len(set(nums)) 
    else: 
        answer = n
    return int(answer)
print(solution([3,3,3,2,2,2]))