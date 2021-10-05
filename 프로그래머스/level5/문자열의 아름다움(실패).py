def solution(s):
    answer = 0
    for i in range(len(s)):
        for j in range(i,len(s)):
            length = j-i
            while length!=0 and (s[i]==s[i+length] and s[j]==s[j-length]):
                length -=1
            answer+=length
    return answer


print(solution("oo"))
print(solution("baby"))