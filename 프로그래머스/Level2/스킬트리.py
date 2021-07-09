def solution(skill, skill_trees):
    dic = {}
    answer=0
    for i,j in enumerate(skill):
       dic[j]=i
    
    for j in skill_trees:
        order=0
        for k in j:
            x = dic.get(k,9999)
            if x==order:
                order+=1
                if order==len(skill):
                    answer+=1
                    break
            elif x==9999:
                continue
            else:
                break
        else:
            answer+=1
    return answer

print(solution("CBD",["BACDE", "CBADF", "AECB", "BDA"]))