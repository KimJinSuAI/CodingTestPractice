import copy
def dp(i, n, count,l, aScore):
    if n<=Info[i] or i==10:
        if aScore<count:
            return count-aScore,l+[n]+[0]*(10-i)
        else:
            return False, False
    else:
        nScore, nl = dp(i+1, n, count, l+[0], copy.deepcopy(aScore))
        if Info[i]!=0:
            aScore-=10-i
        sScore, sl = dp(i+1, n-Info[i]-1, count+10-i, l+[Info[i]+1], copy.deepcopy(aScore))

        if nScore!=False and sScore!=False:
            if sScore>nScore :
                return sScore,sl
            elif sScore<nScore:
                return nScore,nl
            else:
                for i in range(10,0,-1):
                    if nl[i]>sl[i]:
                        return nScore,nl
                    elif nl[i]<sl[i]:
                        return sScore,sl

        elif sScore == False and nScore== False:
            return False, False
        elif sScore == False:
            return nScore,nl
        else:
            return sScore,sl
def solution(n, info):
    global Info
    Info = info
    aScore = 0
    for i,tmp in enumerate(info):
        if tmp!=0:
            aScore+=10-i
        
    tmp = dp(0,n,0,[], aScore)
    return tmp[1] if tmp[0]!=False else [-1]
print(solution(5,[2,1,1,1,0,0,0,0,0,0,0]))