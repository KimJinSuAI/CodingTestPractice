def solution(play_time, adv_time, logs):
    stck = []
    play_time = list(map(int,play_time.split(":")))
    adv_time = list(map(int,adv_time.split(":")))
    logs = list(map(lambda y: list(map(lambda x: x.split(":"),y)),list(map(lambda x:x.split("-"),logs))))
    for log in range(len(logs)):
        logs[log] = [int(logs[log][0][0])*3600+int(logs[log][0][1])*60+int(logs[log][0][1]),
        int(logs[log][1][0])*3600+int(logs[log][1][1])*60+int(logs[log][1][2])]
    play_time = play_time[0]*3600+play_time[1]*60+play_time[2]
    adv_time = adv_time[0]*3600+adv_time[1]*60+adv_time[2]
    
    logs.sort(key=lambda x: x[0])
    logs.append([0,play_time,1])
    for a in logs:
        acc1 = [a[0],0]     #시작시간,누적시간
        acc2 = [a[1]-adv_time,0]
        endTime = acc1[0]+adv_time
        for b in logs:
            if(len(b))>2:
                continue
            if b[0]>=endTime:
                stck.append(acc1)
                break
            elif a[0]>=b[1]:
                continue
            else:
                if b[1]>=endTime:
                    acc1[1]+=endTime-b[0]
                else:
                    if a[0]>=b[0]:
                        acc1[1]+=b[1]-a[0]
                    else:
                        acc1[1]+=b[1]-b[0]
        else:
            stck.append(acc1)

        for b in logs:
            if(len(b))>2:
                continue
            if b[0]>=a[1]:#endTime <- a[1]
                stck.append(acc2) #acc1 <- acc2
                break
            elif acc2[0]>=b[1]:    #a[0]<-acc2[0]
                continue
            else:
                if b[1]>=a[1]:
                    acc2[1]+=a[1]-b[0]
                else:
                    if acc2[0]>=b[0]:
                        acc2[1]+=b[1]-acc2[0]
                    else:
                        acc2[1]+=b[1]-b[0]
        else:
            stck.append(acc2)

        
    answer = sorted(stck, key = lambda x: (-x[1],x[0]))[0] 
    if answer[0]<0:
        return "00:00:00"
    miniute = answer[0]//60
    answer = str(miniute//60).zfill(2)+":"+str(miniute%60).zfill(2)+":"+str(answer[0]%60).zfill(2)
    return answer
# print(solution("02:03:55","00:14:15",
# ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))
print(solution("50:00:00","50:00:00",["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))