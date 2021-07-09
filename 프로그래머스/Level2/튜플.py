import re
def solution(s):
    a = re.findall("[0-9,]*[^{,}}]",s)
    a = list(map(lambda x: x.split(",",-1),a))
    a.sort(key=lambda x: len(x))
    
    answer = []
    for i in a:
        for j in i:
            if int(j) not in answer:
                answer.append(int(j))
    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))