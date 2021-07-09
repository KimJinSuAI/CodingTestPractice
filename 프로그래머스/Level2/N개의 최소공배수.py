import math
def solution(arr):
    index = [1]*len(arr)
    arr = sorted(arr,reverse=True)
    count = arr[:]
    i=0
    while i<len(arr)-1:
        if count[i]<count[i+1]:
            index[i]+=1
            count[i]=arr[i]*index[i]
            i=0
        elif count[i]>count[i+1]:
            index[i+1]+=1
            count[i+1]=arr[i+1]*index[i+1]
            i=0
        else:
            i+=1
        
    return count[0]

def solution(num):      
    answer = num[0]
    for n in num:
        answer = int(n * answer / math.gcd(n, answer))

    return answer

print(solution([2,6,8,14]))