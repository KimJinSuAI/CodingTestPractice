def solution(A, B):
    answer = 0
    A.sort(reverse = True)
    B.sort(reverse = True)
    maxStart = 0
    for b in B:
        for a in range(maxStart,len(A)):
            if b>A[a]:
                answer+=1
                maxStart=a+1
                break
    return answer
print(solution([5,1,3,7],[2,2,6,8]))