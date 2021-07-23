def solution(lines):
    stck = []
    lines = list(map(lambda x: x[11:], lines))
    lines = list(map(lambda x: x.split(" "), lines))
    for line in lines:
        line[0] = float(line[0][:2])*3600+float(line[0][3:5])*60+float(line[0][6:])
        line[1] = float(line[1][:-1])
        line[0], line[1] = round(line[0]-line[1]+0.001,3), round(line[0],3)
        stck.append(round(line[0]-0.999,3))  #시작지점
        stck.append(line[1])    #끝난지점
    lines.sort(key = lambda x: x[0])
    stck.sort()
    answer = []
    for s in stck:
        count = 0
        for line in lines:
            if line[0]>round(s+0.999,3):
                answer.append(count)
                break
            elif line[1]<s:
                continue
            else:
                count+=1
        else:
            answer.append(count)
    return max(answer)

# print(solution(["2016-09-15 20:59:57.421 0.351s"]))
# print(solution(	["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]))
print(solution(	["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]))
# print(solution([
# "2016-09-15 20:59:57.421 0.351s",
# "2016-09-15 20:59:58.233 1.181s",
# "2016-09-15 20:59:58.299 0.8s",
# "2016-09-15 20:59:58.688 1.041s",
# "2016-09-15 20:59:59.591 1.412s",
# "2016-09-15 21:00:00.464 1.466s",
# "2016-09-15 21:00:00.741 1.581s",
# "2016-09-15 21:00:00.748 2.31s",
# "2016-09-15 21:00:00.966 0.381s",
# "2016-09-15 21:00:02.066 2.62s"
# ]))