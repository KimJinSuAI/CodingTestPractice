from collections import Counter
def solution(scores):
    answer = ''
    for i in range(len(scores)):
        student = [scores[x][i] for x in range(len(scores))]
        count = sum(student)
        avg = 0
        if (student[i]==max(student) or student[i]==min(student)) and Counter(student)[student[i]]==1:
            count-=student[i]
            avg = count/(len(student)-1)
        else:
            avg = count/len(student)

        if avg>=90:
            answer+='A'
        elif avg>=80:
            answer+='B'
        elif avg>=70:
            answer+='C'
        elif avg>=50:
            answer+='D'
        else:
            answer+="F"
    return answer
print(solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]))