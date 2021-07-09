def rightStr(stck):
    cnt = 0
    while stck:
        tmp = stck.pop()
        if tmp==")":
            cnt+=1
        else:
            cnt-=1
            if cnt<0:
                return False
    return True
            
def solution(p):
    if len(p)==0:
        return ""
    else:
        stck = []
        l = 0
        r = 0
        for i in range(len(p)):
            stck.append(p[i])
            if p[i]=="(":
                l+=1
            else:
                r+=1
            if r==l:
                break
        u = p[:i+1]
        v = p[i+1:]
        if rightStr(stck):
            return u+solution(v)
        else:
            tmp = "("+solution(v)+")"
            for j in u[1:-1]:
                if j=="(":
                    tmp+=")"
                else:
                    tmp+="("
            return tmp

# print(solution("(()())()"))
# print(solution(")("))
print(solution("()))((()"))