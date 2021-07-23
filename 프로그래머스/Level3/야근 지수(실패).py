def solution(n, works):

    works.sort(reverse=True)
    while n > 0 and works[0] != 0:
        count = works.count(works[0])
        if count == len(works):
            sub = 1
        else:
            sub = works[0] - works[count]

        for i in range(0, count * sub):
            if n - 1 >= 0:
                works[i%count] = works[i%count] - 1
                n = n - 1
            else:
                break

    answer = 0
    for x in works:
        answer = answer + x * x
    return answer

# print(solution(4, [4,3,3]))
# print(solution(1,[2, 1, 2]))
# print(solution(3,[1,1]), 0)
# print(solution(5,[4,4,4]), 17)
# print(solution(5,[1,5,9]), 42)
print(solution(99, [2, 15, 22, 55, 55]), 580)