from collections import Counter
def solution(research, n, k):
    issues = {}
    isIssue = 2*n*k
    words = {}
    for i, res in enumerate(research):
        tmp = Counter(res)
        for key in tmp.keys():
            if not words.get(key,[]):
                words[key] = [0]*(i)
            words[key] += [tmp[key]]
        for key in words.keys():
            if key not in tmp.keys():
                words[key].append(0)

    for key in words.keys():
        l,r =0,0
        s = 0
        for count in range(n):
            s+=words[key][r]
            r+=1

        r-=1
        while r!=len(research):
            if s>=isIssue:
                for count in words[key][l:r+1]:
                    if count<k:
                        break
                else:
                    issues[key] = issues.get(key,0)+1
            s-=words[key][l]
            l+=1
            s+=words[key][r]
            r+=1

    answer = ''
    if not issues:
        return "None"
    else:
        return sorted(issues.items(), key = lambda x: (-x[1],x[0]))[0][0]
# print(solution(["abaaaa","aaa","abaaaaaa","fzfffffffa"],2,2))
print(solution(	["yxxy", "xxyyy"], 2, 1))