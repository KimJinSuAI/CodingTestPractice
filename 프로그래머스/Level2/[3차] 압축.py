def solution(msg):
    dic = {}
    answer = []
    for i,j in zip(range(1,27),range(ord("A"),ord("Z")+1)):
        dic[chr(j)] = i

    tmp = ""
    out = 0

    for i in range(len(msg)):
        tmp +=msg[i]
        out = dic.get(tmp,0)
        if out==0:
            answer.append(dic.get(tmp[:-1]))
            dic[tmp] = len(dic)+1
            tmp = tmp[-1]
    else:
        answer.append(dic.get(tmp,0))

    return answer

print(solution("KAKAO"))
print(solution("TOBEORNOTTOBEORTOBEORNOT"))
