def solution(names, homes, grades):
    #Sort
    tmp = sorted(enumerate(zip(names,homes,grades)), key= lambda x: (-int(str(x[1][2])[0]),-(x[1][1][0]**2+x[1][1][1]**2),x[1][0]))

    #Answer
    answer = [0 for _ in range(len(names))]
    for idx,x in enumerate(tmp):
        answer[x[0]] = idx+1
    return answer

print(solution(	["azad", "andy", "louis", "will", "edward"], [[3, 4], [-1, 5], [-4, 4], [3, 4], [-5, 0]], [4.19, 3.77, 4.41, 3.65, 3.58]))