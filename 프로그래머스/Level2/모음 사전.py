def solution(word):
    word2num = {"A":1,"E":1,"I":2,"O":3,"U":4}
    answer = 0
    for i,w in enumerate(word):
        if w=="A":
            answer+=1
        else:
            if i==0:
                answer+=1+781*word2num[w]
            elif i==1:
                answer+=1+156*word2num[w]
            elif i==2:
                answer+=1+31*word2num[w]
            elif i==3:
                answer+=1+6*word2num[w]
            else:
                answer+=1+word2num[w]

    return answer

print(solution("AAAAE"))
print(solution("AAAE"))
print(solution("I"))
print(solution("EIO"))