#import heapq
def solution(jobs):
    now = jobs[0]
    answer = [now[2]]
    Q = []
    for job in jobs[1:]:
        if job[2]==now[2]:
            now[1]+=job[1]
        elif job[0]>now[0]+now[1]:
            if Q:
                Q.sort(key = lambda x: (x[3],-x[2]))
                tmp = now[0]+now[1]
                now = Q.pop()
                now[0] = tmp
                answer.append(now[2])
                if job[2]==now[2]:
                    now[1]+=job[1]
                else:
                    Q.append(job)
            else:
                Q.append(job)

        else:
            if Q:
                for tmp in Q:
                    if tmp[2]==job[2]:
                        tmp[1]+=job[1]
                        tmp[3]+=job[3]
                        break 
                else:
                    Q.append(job)
            else:
                Q.append(job)
    
    if Q:
        Q.sort(key = lambda x: (x[3],-x[2]))
        while Q:
            tmp = now[0]+now[1]
            now = Q.pop()
            now[0] = tmp
            answer.append(now[2])
        
    return answer
# print(solution([[1, 5, 2, 3], [2, 2, 3, 2], [3, 1, 3, 3], [5, 2, 1, 5], [7, 1, 1, 1], [9, 1, 1, 1], [10, 2, 2, 9]]))
print(solution(	[[0, 2, 3, 1], [5, 3, 3, 1], [10, 2, 4, 1]]))