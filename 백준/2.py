from collections import deque

def solution(arr, processes):
    answer = []
    
    processes = list(map(lambda x: x.split(), processes))

    for i in range(len(processes)):
        processes[i][0] = 0 if processes[i][0][0]=="w" else 1   #0:쓰기 1: 읽기
        for j in range(1,5):
            processes[i][j] = int(processes[i][j])

    global_start = processes[0][1]
    Q = deque()
    processing = []
    nowjob = 1 

    jobs = []
    nexttime = 0
    
    idx = 0
    for time in range(100000):
        while jobs and time>=jobs[-1][1]:
            if len(jobs[-1])==6:
                job, t1,t2,A,B,C = jobs.pop()
                arr[A:B+1] = C
            else:
                job, t1,t2,A,B = jobs.pop()
                answer.append(arr[A:B+1])

        if idx>len(processes):
            if not Q:  #끝났다
                answer.append(time-global_start)
                break
            else:       #Q남음
                break #############

        elif time>= processes[idx][1]:
            while idx<=len(processes) and time>=processes[idx][1]: #대기가능하면 대기큐에 넣기
                Q.append(processes[idx])
                idx+=1
            Q = deque(sorted(Q, key = lambda x: (x[0],x[1])))

        if nexttime<=time:                              #쓰기
            if Q and Q[1]<=time:    
                job, t1,t2,A,B,C = Q.popleft()
                nexttime = max(nexttime,time+t2)
        
        elif Q and Q[0][1]<=time:           #읽기는 동시가능
            while Q and len(Q[0])==5:
                jobs.append(Q.popleft())
            jobs.sort(key = lambda x: -x[1])
            nexttime = jobs[0][1]

            


    return answer

print(solution(["1","2","4","3","3","4","1","5"],["read 1 3 1 2", "read 2 6 4 7", "write 4 3 3 5 2", "read 5 2 2 5", "write 6 1 3 3 9", "read 9 1 0 7"]))