def solution(n):
    x= []
    for i in str(n):
        x.append(i)
    x.sort(reverse=True)
    return int(''.join(x))
print(solution(118372))