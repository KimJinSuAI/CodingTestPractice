import string
d=dict(zip(string.ascii_uppercase,[i for i in range(26)]))
def dfs(name, now, nowName):
    global d
    if name == nowName:
        return 0
    else:
        ans = d[name[now]]                          #자기꺼 +
        if ans>13:
            ans = (-1*ans)%26
        nowName[now] = name[now]
        if nowName==name:
            return ans

        count1 = 0                                  #비교
        for i in range(now+1,len(name)):
            x = i%len(name)
            if name[x]==nowName[x]:
                count1+=1
            else:
                count1+=1
                break
        count2 = 0

        for i in range(now+1,len(name)):
            tmp = -1*i
            x = (tmp+len(name))%len(name)
            if name[x]==nowName[x]:
                count2+=1
            else:
                count2+=1
                break

        if count1<=count2:
            return ans+dfs(name, (now+1)%len(name),nowName)+count1
        else:
            return ans+dfs(name, (now-1+len(name))%len(name),nowName)+count2

def solution(name):
    return dfs(list(name), 0, ["A"]*len(name))

# print(solution("BA"), 1)
# print(solution("B"), 1)
# print(solution("A"), 0)
# print(solution("AA"), 0)
# print(solution("AAB"), 2)
# print(solution("JEROEN"), 56)
# print(solution("JAZ"), 11)
# print(solution("JAN"), 23)
# print(solution("BBABAAAB"),9)
print(solution("AABAAAAAAABBB"),11)