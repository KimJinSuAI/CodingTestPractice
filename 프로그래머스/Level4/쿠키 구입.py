def solution(cookie):
    global prefixSum
    answer = 0
    prefixSum = [0]
    count = 0
    for ck in cookie:
        count += ck
        prefixSum.append(count)

    for m in range(1, len(cookie)+1):
        tmp = []
        for l in range(1,m+1):
            tmp.append(prefixSum[m]-prefixSum[l-1])
        for r in range(m+1,len(cookie)-1):
            right = cookie[-1]-cookie[r]
            if right in tmp and right>answer:
                answer = right
                break
    return answer

print(solution([1,1,2,3]))