import heapq
from functools import reduce
def solution(jobs):
    count=0
    time = []
    N = len(jobs)
    heap = []       #작업시간힙
    heapq.heapify(jobs)
    heapq.heapify(heap)
    while len(jobs)!=0:
        if jobs[0][0]<=count:                   #요청시간 <= 이전작업 종료시간->대기열추가
            tmp = heapq.heappop(jobs)
            heapq.heappush(heap,[tmp[1],tmp[0]])
        else:                                   #요청시간 > 이전작업 종료시간->대기열pop
            while len(heap)>0:
                tmp = heapq.heappop(heap)
                count+=tmp[0]
                time.append(count-tmp[1])
                if jobs[0][0]<count:
                    break
            if jobs[0][0]>count:
                count = jobs[0][0]
               
    
    while len(heap)>0:
        tmp = heapq.heappop(heap)
        count+=tmp[0]
        time.append(count-tmp[1])
    
    time [1,2,3,4,5]
    return int(reduce(lambda x,y: x+y,time)/N,0)

print(solution([[24, 10], [18, 39], [34, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]), 74)
print(solution([[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]), 72)
print(solution([[0, 10], [4, 10], [15, 2], [5, 11]]), 15)
print(solution([[0, 3], [1, 9], [2, 6]]), 9)