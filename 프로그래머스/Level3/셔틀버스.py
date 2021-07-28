from collections import deque
def solution(n, t, m, timetable):
    timetable = list(map(lambda x:x.split(":"), timetable))
    timetable = sorted(list(map(lambda x:int(x[0])*60+int(x[1]), timetable)), reverse=True)
    
    Q = deque()
    geton = 0
    time = 540
    while n!=1:
        for i in range(len(timetable)-1,-1,-1):
            if timetable[-1]<=time and geton<m:
                Q.append(timetable.pop())
                geton+=1
            else:
                break
        for i in range(m):
            if Q:
                Q.popleft()
            else:
                break
        n-=1
        time+=t
        geton = 0
    
    lastman = time
    while True:             #막차일 때
        if not timetable:
            return str(time//60).zfill(2)+":"+str(time%60).zfill(2)

        elif geton==m-1:                                    #막차의 마지막 승객일때
            if timetable and timetable[-1] <=time:          #막차의 마지막 승객이 탈수있으면 그승객-1일때 타기
                return str((timetable[-1]-1)//60).zfill(2)+":"+str((timetable[-1]-1)%60).zfill(2)
            else:                                           #마지막승객이 못타면 시간에맞춰타기
                return str(time//60).zfill(2)+":"+str(time%60).zfill(2)
        else:
            lastman = timetable.pop()
            geton+=1
            

# print(solution(1,1,5,["08:00", "08:01", "08:02", "08:03"]))
# print(solution(2,10,2,["09:10", "09:09", "08:00"]))
# print(solution(2,1,2,	["09:00", "09:00", "09:00", "09:00"]))
# print(solution(1,1,5,["00:01", "00:01", "00:01", "00:01", "00:01"]))
print(solution(10,60,1,["17:59","23:59"]))
# print(solution(10,60,45,["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]))