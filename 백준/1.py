import re

def isword(goods,i,j):
    word_arr = set()
    for k in range(len(goods[i])-j+1): #단어시작점
        flag = True
        for l in range(len(goods)): #상대단어
            if i!=l and re.findall(f"{goods[i][k:k+j]}", goods[l]):
                flag = False
                break
        if flag: 
            word_arr.add(goods[i][k:k+j])

    return word_arr

def solution(goods):
    answer = []
    for i in range(len(goods)): #검사단어
        for j in range(1,len(goods[i])+1):  #단어길이
            tmp = isword(goods,i,j)
            if tmp:
                answer.append(' '.join(sorted(tmp)))
                break
            elif j==len(goods[i]):
                answer.append("None")

    return answer

# print(solution(["pencil","cilicon","contrabase","picturelist"]))
print(solution(["abcdeabcd", "cdabe", "abce", "bcdeab"]))
# print(solution(["aaa","aba","abc"]))