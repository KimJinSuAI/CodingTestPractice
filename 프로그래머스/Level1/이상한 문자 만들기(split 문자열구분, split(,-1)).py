def solution(s):
    s = s.split(" ",-1)
    answer = ""
    for i in s:
        for j in enumerate(i):
            if j[0]%2==0:
                answer+=j[1].upper()
            else:
                answer+=j[1].lower()
        answer+=" "
    return answer[:-1]
print(solution("try hello world strys"))
print(solution("1"))