def solution(nums):
    n = len(nums)//2 
    answer = 0
    sort = set(nums)
    if n>len(sort):
        answer = len(sort) 
    else: 
        answer = n
    return answer
print(solution([3,3,3,2,2,2]))