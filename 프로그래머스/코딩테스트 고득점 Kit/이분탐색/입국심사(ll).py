from functools import reduce
def solution(n, times):
    times.sort()
    min = 1
    max = times[-1]*n
    ans = 1
    while min<=max:
        mid = (min+max)//2
        done = 0
        for time in times:
            done+=mid//time
            if done>n:
                break
            
        if done<n:
            min = mid+1
        else:
            ans=mid
            max = mid-1


    return ans

print(solution(9,[3,3,3]), 9)
print(solution(3, [1, 2, 3]), 2)
print(solution(3, [1, 1, 1]), 1)