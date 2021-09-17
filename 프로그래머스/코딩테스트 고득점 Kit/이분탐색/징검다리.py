from functools import reduce
def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    l = 0
    r = distance
    answer = 0
    while l<r:
        mid = (l+r)//2
        cnt = 0
        p = 0
        for i in range(len(rocks)):
            if rocks[i]-p<=mid:
                cnt+=1
            else:
                p = rocks[i]
        if cnt<=n:
            l = mid+1
        else:
            r = mid
            answer = mid
    return answer
    # return min([i[1] for i in rocks])

# print(solution(25, [1,2,3,4,5],2) )
print(solution(25, [2, 14, 11, 21, 17], 2), 4)