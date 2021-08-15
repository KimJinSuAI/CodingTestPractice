N=input()
dic = {}#사용자 위치
androidappuser = {}#화면별 순방문자수
iosappuser = {}#화면별 순방문자수
android = {}#android로그
ios = {}#ios로그
visited = set()
log_name = ['home','transfer','account_tab','enter_account_no','enter_transfer_amount','transfer_decision','enter_password','transfer_complete']
for i in range(int(N)):
    log = input().split(',')
    if log[-2]=='android':#앱별 A,B를 키로 하여 화면이동횟수 count
        if log[3] in log_name:
            androidappuser[log[3]] = androidappuser.get(log[3],0)+1#화면은 항상 +1
            if dic.get(log[1],'') != '':#사용자별 위치 초기화
                android[dic[log[1]]+','+log[3]] = android.get(dic[log[1]]+','+log[3],0)+1
            else:
                dic[log[1]] = log[3]

    else:
        if log[3] in log_name:
            iosappuser[log[3]] = iosappuser.get(log[3],0)+1#화면은 항상 +1
            if dic.get(log[1],'') != '':#사용자별 위치 초기화
                ios[dic[log[1]]+','+log[3]] = ios.get(dic[log[1]]+','+log[3],0)+1
            else:
                dic[log[1]] = log[3]
                
for c in android.items():
    c[1] = int(c[1]/androidappuser[c[0].split(',')[0]]*100)
for c in ios.items():
    c[1] = int(c[1]/iosappuser[c[0].split(',')[0]]*100)
a = sorted(android.items(),key = lambda x: x[1])
i = sorted(ios.items(),key = lambda x: x[1])
print('android'+a[0][0].split(',')[0]+a[0][0].split(',')[1]+a[0][1]+"%")
print('ios'+i[0][0].split(',')[0]+i[0][0].split(',')[1]+i[0][1]+"%")