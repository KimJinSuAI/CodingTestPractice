# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    ans = 0
    cnt = 0
    before = A[0]
    for i in A:
        if i==before:
            cnt+=1
        else:
            if cnt>before:
                ans+=cnt-before
            elif cnt<(before+1)//2:
                ans+=cnt
            else:
                ans+=before-cnt
            cnt = 1
            before = i
    if cnt>before:
        ans+=cnt-before
    elif cnt<(before+1)//2:
        ans+=cnt
    else:
        ans+=before-cnt
    return ans
    # write your code in Python 3.6
# print(solution([1,1,3,4,4,4]))
# print(solution([1,2,2,2,5,5,5,8]))
print(solution([1,4,4,1]))