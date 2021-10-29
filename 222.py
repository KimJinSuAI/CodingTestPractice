def solution(numArr):
    answer = []
    aver = '{:.2f}'.format(sum(numArr)/3)
    answer.append(str(aver))
    aver = float(aver)
    if aver>=90:
        answer.append("A")
    elif aver>=80:
        answer.append("B")
    elif aver>=70:
        answer.append("C")
    elif aver>=60:
        answer.append("D")
    else:
        answer.append("F")
    return answer

print(solution([50,60,75]))