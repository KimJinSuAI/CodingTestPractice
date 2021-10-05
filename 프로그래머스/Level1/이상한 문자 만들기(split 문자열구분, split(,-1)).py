def solution(s):
    s = s.split(" ",-1)
    answer = ""
    for i in s:
        for idx, j in enumerate(i):
            if idx%2==0:
                answer+=j.upper()
            else:
                answer+=j.lower()
        answer+=" "
    return answer[:-1]
print(solution("try hello world strys"))
print(solution("1"))