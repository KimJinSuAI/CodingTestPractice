def solution(start_date, end_date, login_dates):
    day = {"SAT":0,"FRI":1,"THU":2,"WED":3,"TUE":4,"MON":5,"SUN":6}
    mon = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    start_date = start_date.split()
    start_date[0] = list(map(int,start_date[0].split('/')))
    end_date = list(map(int,end_date.split('/')))
    login_dates = list(map(lambda x: list(map(int,x.split('/'))),login_dates))
    login_dates.sort(key = lambda x: (x[0],x[1]))

    nextWeekendMonth,nextWeekend = start_date[0][0],start_date[0][1]+day[start_date[1]]
    if nextWeekend>mon[nextWeekendMonth]:
        nextWeekend-=mon[nextWeekendMonth]
        nextWeekendMonth+=1

    maxi,cnt = 0,0
    nextMonth, nextDay = -1,-1
    for i in range(len(login_dates)):
        m,d = login_dates[i]
        if m>nextWeekendMonth:
            while nextWeekendMonth!=m:
                nextWeekend+=7
                if nextWeekend>mon[nextWeekendMonth]:
                    nextWeekend-=mon[nextWeekendMonth]
                    nextWeekendMonth+=1
        if d in [nextWeekend,nextWeekend+1]:
            continue
        else:
            while m == nextWeekendMonth and d>nextWeekend:
                nextWeekend+=7
                
        if [m,d]==[nextMonth,nextDay]:
            cnt+=1
            maxi = max(maxi,cnt)
            nextDay+=1
            if nextDay>mon[m]:
                nextDay-=mon[m]
                nextMonth+=1
            if nextDay==nextWeekend:
                nextDay+=2
        else:
            nextMonth,nextDay = m,d+1
            cnt = 1
            maxi = max(maxi,cnt)
            if nextDay>mon[m]:
                nextDay-=mon[m]
                nextMonth+=1
            if nextDay==nextWeekend:
                nextDay+=2

    return maxi
# print(solution("05/04 MON","05/30", ["05/26","05/25","05/27","05/10","05/11","05/23","05/22","05/21","05/06","05/09","05/07","05/08"]))
print(solution("05/27 SUN", "06/16", ["05/31","05/30","06/01","06/04","06/07","06/06","06/09","06/08","06/13","06/14","06/10"]))