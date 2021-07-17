def solution(stones, k):
    maxIndex = len(stones)
    maxIndexTmp =0
    stck = []
    while True:
        max = 0
        start = maxIndex-k
        if start<0:
            return min(stck)
        stones2 = stones[start:maxIndex]

        for x in range(len(stones2)):
            if stones2[x]>max:
                max = stones2[x]
                maxIndexTmp = x
                
        maxIndex = start + maxIndexTmp
        stck.append(max)



# print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1],3))
print(solution([1,2,3,4,5,6,7,8,9,10,11,12],2))