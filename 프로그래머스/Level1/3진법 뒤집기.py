def solution(n):
    tmp = []
    while n>2:
        tmp.append(int(n%3))
        n = int(n/3)
    tmp.append(n)

    ans = 0
    tmp.reverse()
    for i in range(len(tmp)):
        ans+=tmp[i]*(3**i)
    return ans

print(solution(45))
print(solution(125))