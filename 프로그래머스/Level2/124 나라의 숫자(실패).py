def solution(n):
    x = 0
    i = 0
    j = 0
    while x+3**i<=n:
        x+=3**i
        i+=1
    while x+j*3**(i-1)<=n:
        x+=j*3**(i-1)
        j+=1
    return j-1

print(solution(9))