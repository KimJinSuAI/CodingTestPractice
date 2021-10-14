def solution(n, left, right):
    tmp = []
    for i in range(left,right+1):
        tmp.append(max(i//n+1,i%n+1))
    return tmp

print(solution(3,2,5))