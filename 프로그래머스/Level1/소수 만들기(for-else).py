import itertools
def solution(nums):
    count=0
    for i in itertools.combinations(nums,3):
        a = sum(i)
        for j in range(2,a):
            if a%j==0:
                break
        else:
            count+=1
    return count

print(solution([1,2,3,4]))
print(solution([1,2,7,6,4]))