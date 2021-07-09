def solution(A,B):
    A = sorted(A)
    B = sorted(B, reverse = True)
    answer = sum([i*j for i,j in zip(A,B)])
    return answer

print(solution([1,2],[3,4]))