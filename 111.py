def solution(n):
    a,b = 1, 3
    for i in range(2,n+2):
        a,b = b, b+4*i-2
    answer = 0
    return answer

print(solution(3))