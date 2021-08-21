from collections import deque
import re
def solution(arr):
    answer = set()
    count = 0
    op = []
    for index,j in enumerate(arr):
        if not re.match("[0-9]",j):
            count+=1
    Q = deque([[2,'('+''.join(arr[:2]),count-1,count]])
    while Q:
        index, exp, cntl,cntr = Q.popleft()
        if index>=len(arr)-2:
            answer.add(eval('('*cntl+exp+''.join(arr[index:])+')'*cntr))
        else:
            if cntr>cntl:
                Q.append([index+2,exp+arr[index]+')'+arr[index+1], cntl, cntr-1])
            tmp = 1
            while tmp!=cntl+1:
                Q.append([index+2,exp+'('*tmp+''.join(arr[index:index+2]),cntl-tmp,cntr])
                tmp+=1

    return max(answer)
    
def solution(arr):
    arrs = ''.join(arr).split("-")
    arrs[0] = sum(list(map(int,arrs[0].split('+'))))
    BminVal = 0
    BmaxVal = 0
    for arr in arrs[:0:-1]:
        arr = list(map(int,arr.split('+')))
        AminVal = -sum(arr)
        AmaxVal = -arr[0]+sum(arr[1:])
        BminVal, BmaxVal = AminVal + BminVal, max(AminVal-BminVal, AmaxVal+BmaxVal)
    return int(arrs[0])+BmaxVal


print(solution(["1", "-", "3", "+", "5", "-", "8"]))
print(solution(["5", "-", "3", "+", "1", "+", "2", "-", "4"]))