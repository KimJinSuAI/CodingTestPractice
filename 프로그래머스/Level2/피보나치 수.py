def solution(n):
    a, b, c = 0, 1, 1
    for i in range(2,n):
        a, b, c = b, c, b+c
    return c%1234567

    
print(solution(5))