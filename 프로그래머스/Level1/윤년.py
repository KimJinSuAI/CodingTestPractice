def solution(a, b):
    day = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    month = [31,29,31,30,31,30,31,31,30,31,30,31]
    for i in range(a-1):
        b += month[i]
    return day[b%7]

print(solution(5,24))