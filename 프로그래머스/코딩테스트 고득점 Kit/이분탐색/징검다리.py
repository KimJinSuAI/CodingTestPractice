from functools import reduce
def solution(distance, rocks, n):
    rocks.append(distance)
    rocks.sort()
    rocks = list(map(list,zip(rocks, [0]*len(rocks))))
    tmp1=0
    tmp2=0
    for i in range(0,len(rocks)):       #바위간 거리
        tmp1 = tmp2
        tmp2 = rocks[i][0]
        rocks[i][1]=rocks[i][0]-tmp1


    rocks.sort(key = lambda x:x[1])
    for i in range(n):                #바위 제거
        rocks[1][1] += rocks[0][1]
        rocks.pop(0)
    rocks[0][1]+=tmp1

    return rocks
    # return min([i[1] for i in rocks])

# print(solution(25, [1,2,3,4,5],2) )
print(solution(25, [2, 14, 11, 21, 17], 2), 4)