from collections import deque
def str2sec(s):
    s = list(map(int,s.split(":")))
    return s[0]*3600+s[1]*60+s[2]

def sec2str(sec):
    return str(sec//3600).rjust(2,"0")+":"+str((sec//60)%60).rjust(2,"0")+":"+str(sec%60).rjust(2,"0")

def solution(play_time, adv_time, logs):
    play_time = str2sec(play_time)
    adv_time = str2sec(adv_time)
    logs = list(map(lambda x: x.split("-"), logs))
    for i in range(len(logs)):
        logs[i][0] = str2sec(logs[i][0])
        logs[i][1] = str2sec(logs[i][1])
    logs.sort(key = lambda x: x[0])
    viewer = [0 for _ in range(play_time+1)]

    for start, end in logs:
        viewer[start]+=1
        viewer[end]-=1

    for i in range(1,play_time):
        viewer[i] +=viewer[i-1]
    for i in range(1,play_time):
        viewer[i] +=viewer[i-1]
        
    maxTime = (viewer[adv_time],0)
    for i in range(adv_time,len(viewer)):
        time = viewer[i]-viewer[i-adv_time]
        if time>maxTime[0]:
            maxTime = (time,i-adv_time+1)

    return sec2str(maxTime[1])





print(solution("02:03:55","00:14:15",["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))
print(solution("99:59:59","25:00:00",["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))
print(solution("50:00:00","50:00:00",["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))