import math
def solution(a, s):
    def get_b(b):
        N = len(b)
        i = 1
        ct = 1
        PS = [0]
        for tmp in b:
            PS.append(PS[-1]+tmp)
        DP = [[0]*(math.floor(math.log2(max(b)))+1) for _ in range(N)]
        DP[0][0] = 1        #DP[0][0] = 1
        while i<N:
            DP[i][b[i]] = (ct,i-1)
            var = b[i]
            j = i-1
            while DP[j].get(var,None)!=None:
                diff = DP[j][var]
                ct += diff[0]
                var *= 2
                DP[i][var] = diff
                j = diff[1]
                if j == None:
                    break
            i+=1
        return ct%(10**9 + 7)


    answer = []
    subsum = 0
    for x in s:
        b = a[subsum:subsum+x]
        subsum+=x
        answer.append(get_b(b))
    return answer
print(solution(	[1, 1, 1, 1, 1, 1, 2, 5, 8, 2, 1, 1, 4, 8, 8, 8, 12, 6, 6], [4, 3, 1, 5, 6]))