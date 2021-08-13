def solution(dartResult):
    answer = 0
    before = 0
    now = 0
    for i in range(len(dartResult)):
        if dartResult[i].isdigit():
            if (dartResult[i-1]).isdigit():
                now *=10
                continue
            answer+=before
            before = now
            now = int(dartResult[i])
        elif dartResult[i]=="D":
            now**=2
        elif dartResult[i]=="T":
            now**=3
        elif dartResult[i]=="*":
            before *=2
            now *=2
        elif dartResult[i]=="#":
            now *=-1
    return answer+before+now

print(solution("1S2D*3T"))
print(solution("1D2S#10S"))
print(solution("1D2S0T"))
print(solution("1S*2T*3S"))
print(solution("1D#2S*3S"))
print(solution("1T2D3D#"))
print(solution("1D2S3T*"))
print(solution("1D*1D1D#"),2)
print(solution("1D*1D10D#"),-97)