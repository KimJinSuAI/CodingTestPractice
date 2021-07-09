def solution(n, m):
    GCF = -1
    LCM = -1
    for i,j in zip(range(1,n+1),range(1,m+1)):
        if n%i==0 and m%j==0:
            GCF = i

    na=1
    ma=1
    xn = n
    xm = m
    while xn!=xm:
        if xn>xm:
            ma+=1
            xm = m*ma
        elif xn<xm:
            na+=1
            xn = n*na
    LCM = xn
    return [GCF,LCM]
print(solution(3,12))