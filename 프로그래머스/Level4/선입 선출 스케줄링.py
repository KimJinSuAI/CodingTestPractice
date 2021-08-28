def solution(n, cores):
    if n<=len(cores):
        return n
    else:
        n-=len(cores)
        coresCopy = sorted(cores)
        l = 0
        r = coresCopy[-1]*n   
        while l<=r:
            mid = (l+r)//2
            count = 0
            for core in coresCopy:
                count += mid//core
                if count>n:
                    break
            if count<n:
                l = mid+1
            else:
                ans = mid
                r = mid-1
        ansList = []
        for i,core in enumerate(cores):
            n-=(ans-1)//core
            if ans%core ==0:
                ansList.append(i)
        return ansList[n-1]+1
        

# print(solution(6, [1,2,3]), 2)
# print(solution(10, [1,2,3,4]), 1)
# print(solution(5,[4540, 6383, 8674, 2699]))
# print(solution(5,[50, 50, 50, 30]),4)