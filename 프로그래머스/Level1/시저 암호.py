def solution(s, n):
    s = s.split(" ",-1)
    answer=""
    for i in s:
        for j in i:
            if j.isupper():
                answer+=chr((ord(j)+n-65)%26+65)
            else:
                answer+=chr((ord(j)+n-97)%26+97)
        answer+=" "
    return answer[:-1]

print(solution("AB",1))
print(solution("a B z",4))