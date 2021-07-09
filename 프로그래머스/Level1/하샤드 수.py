def solution(x):
    tmp = str(x)
    tmp = sum([int(i) for i in tmp])
    return x%tmp==0

print(solution(11))