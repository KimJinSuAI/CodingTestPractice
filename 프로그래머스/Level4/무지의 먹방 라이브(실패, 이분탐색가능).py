# from collections import Counter
# def solution(food_times, k):
#     s = sum(food_times)
#     c = Counter(food_times)
#     sortedc = sorted(c)
#     i = 0
#     l = 0
#     r = len(food_times)-1
#     while l<r:
#         mid = (l+r)//2
#         tmp = 0
#         while True:
            
        
#     answer = 0
#     return answer

def solution(food_times, k):
    if k>=sum(food_times):
        return -1
    food_times = sorted(enumerate(food_times), key = lambda x: x[1])
    delTime = food_times[0][1]*len(food_times)
    i = 1
    while delTime<k:
        k-=delTime
        delTime = (food_times[i][1]-food_times[i-1][1])*(len(food_times)-i)
        i+=1
    


    food_times = sorted(food_times[i-1:], key=lambda x: x[0])
    return food_times[k%len(food_times)][0]+1

#진 정답 뺄수를 구하는 이분탐색
def solution(food_times, k):
    low,high = 0,100000000
    n,cutting,idx = len(food_times),0,0
    while low<=high:
        mid = (low+high)//2
        v = n*mid
        for f in food_times:
            tmp = f-mid
            if tmp<0:
                v+=tmp
        if v<=k:
            cutting, idx = mid,v
            low = mid+1
        else:
            high = mid-1

    food_times = [f-cutting for f in food_times]

    for i in range(n):
        if food_times[i]>0 and idx==k:
            return i+1
        else:
            if food_times[i]>0:
                idx+=1
    return -1

print(solution([1,3,3,4,5],5))
print(solution([1,3,3,4,5],5), 2)
print(solution([3,1,2],5))
print(solution([5,1,2,5,1,2,5,1,2], 23),7)
print(solution([3,1,2,4,5],12), 4)