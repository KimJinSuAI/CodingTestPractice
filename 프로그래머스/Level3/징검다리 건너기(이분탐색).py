def solution(stones, k):
    minP = min(stones)
    maxP = max(stones)
    while minP<maxP:
        mid = (minP+maxP)//2
        count = 0
        for i in stones:
            if i<=mid:
                count+=1
                if count>=k:
                    maxP = mid
                    break
            else:
                count = 0
        if count<k:
            minP = mid+1
    mid = (minP+maxP)//2
    return mid

        
    return



print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1],3))
# print(solution([1,2,3,4,5,6,7,8,9,10,11,12],2))