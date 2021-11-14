# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    words = []
    tmp = S[0]
    maxi = 0
    cnt = 0
    wordstart = 0
    for i in range(len(S)):
        if S[i]==tmp:
            cnt+=1
            maxi = max(maxi, cnt)
        else:
            cnt = 1
            tmp = S[i]
            words.append(S[wordstart:i])
            wordstart = i
    words.append(S[wordstart:])

    ans = 0
    for word in words:
        ans+=maxi-len(word)
    # write your code in Python 3.6
    return ans

# print(solution("babaa"))
print(solution("abbaaabbbaa"))