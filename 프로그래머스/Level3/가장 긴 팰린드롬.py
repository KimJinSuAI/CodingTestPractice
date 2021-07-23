def ispalindrome(s):
    if s==s[::-1]:
        return True
    return False

def solution(s):
    mx = 1
    found = True
    count = 1
    if ispalindrome(s):
        return len(s)
    while found:
        for i in range(len(s)-mx-count+1):
            if ispalindrome(s[i:i+mx+count]):
                mx +=count
                count = 1
                break
        else:
            if count == 1:
                count = 2
            else:
                found = False

    return mx


print(solution("baab"))