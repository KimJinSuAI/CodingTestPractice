import math
def solution(a, s):
    answer = []
    i = 0
    for j in s:
        tmp = a[i:i+j]
        maxE = math.floor(math.log2(max(tmp)))+1
        DP = [[0]*maxE for _ in range(len(tmp))]    #DP정의

        DP[0][0] = 1 #기저조건
        

        answer.append((tmp, DP))
        i+=j
        
    return answer
print(solution(	[1, 1, 1, 1, 1, 1, 2, 5, 8, 2, 1, 1, 4, 8, 8, 8, 12, 6, 6], [4, 3, 1, 5, 6]))