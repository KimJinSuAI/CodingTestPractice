def solution(arr1, arr2):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(arr1,arr2)]
            
    return answer
print(solution([[1,2],[2,3]],[[3,4],[5,6]]))