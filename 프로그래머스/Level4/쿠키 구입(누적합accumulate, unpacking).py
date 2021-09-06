def solution(cookie):
    global prefixSum, Cookie
    Cookie = cookie
    answer = 0
    prefixSum = [0]
    count = 0
    for ck in cookie:
        count += ck
        prefixSum.append(count)

    for m in range(1, len(cookie)+1):    
        for l in range(m,-1,-1):
            left = prefixSum[m]-prefixSum[l-1]
            if left > (prefixSum[-1]-prefixSum[m]):
                break
            for r in range(m+1,len(Cookie)+1):
                right = prefixSum[r]-prefixSum[m]
                if right==left:
                    answer = max(answer,right)
                elif right>left:
                    if right>prefixSum[m]:
                        return answer
                    else:
                        break
    return answer

def solution(cookie):
    answer = 0
    for l in range(0,len(cookie)-1):
        r = l+1
        m = l
        left = cookie[m]
        right = cookie[r]
        while r!=len(cookie):
            if left<right:
                m+=1
                left+=cookie[m]
                right-=cookie[m]
                if m>r:
                    r+=1
                    if r==len(cookie):
                        break
                    right+=cookie[r]
            elif left>right:
                r+=1
                if r==len(cookie):
                    break
                right+=cookie[r]
            else:
                answer = max(answer,left)
                r+=1
                if r==len(cookie):
                    break
                right+=cookie[r]
    return answer

#다른사람 풀이
from itertools import accumulate

def solution(cookie):
    answer = 0
    for m in range(len(cookie)-1):
        a = set(accumulate(reversed(cookie[:m+1])))
        b = set(accumulate(cookie[m+1:]))
        c = a & b 

        if c:
            answer = max(*c, answer)#unpacking
    return answer
    
print(solution([1,1,2,3,1]))