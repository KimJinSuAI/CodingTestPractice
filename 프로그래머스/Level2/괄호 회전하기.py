def solution(s):
    answer = 0
    small = []
    middle = []
    large = []
    for i in range(len(s)):
        s = s[1:]+s[0]
        for j in s:
            if j=='(': small.append(j)
            elif j==')':
                if len(small)==0:
                    break
                else:
                    small.pop()
            if j=='{': middle.append(j)
            elif j=='}':
                if len(middle)==0:
                    break
                else:
                    middle.pop()
            if j=='[': large.append(j)
            elif j==']':
                if len(large)==0:
                    break
                else:
                    large.pop()
        else:
            if len(small)+len(middle)+len(large)==0:
                answer+=1


    return answer

print(solution("[](){}"))