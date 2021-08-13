def solution(strings, n):
    answer = []
    return sorted(strings,key = lambda x:(x[n],x))

print(solution(["sun", "bed", "car"],1))