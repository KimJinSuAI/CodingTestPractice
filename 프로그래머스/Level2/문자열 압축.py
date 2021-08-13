def solution(s):
    answer = []
    if len(s)==1:
        return 1
    for i in range(1,len(s)):
        stck = []
        tmp = s
        count = 0
        now = ""
        append = ""
        for j in range(0,len(s),i):
            stck.append(tmp[:i])
            tmp = tmp[i:]
        if len(tmp)!=0:
            stck.append(tmp)

        for k in stck:
            if now == k:
                count +=1
            else:
                if count<2:
                    append+=str(now)
                else:
                    append+=(str(count)+str(now))
                now = k
                count = 1
        else:
            if count<2:
                append+=str(now)
            else:
                append+=(str(count)+str(now))
        answer.append(len(append))
    return min(answer)

print(solution("aabbaccc"), 7)
# print(solution("ababcdcdababcdcd"), 9)
# print(solution("a"))