def cant(i):
    global stck
    for s in stck:
        if s[1]==i or abs(s[0]-(stck[-1][0]+1))==abs(s[1]-i):
            return True
    return False
def dfs(n):
    global stck
    count = 0
    for i in range(n):
        if cant(i):
            continue
        else:
            if stck[-1][0]+1==n-1:
                count+=1
            else:
                stck.append([stck[-1][0]+1,i])
                count += dfs(n)
    stck.pop()
    return count
def solution(n):
    global stck
    stck = []
    answer = 0
    if n==1:
        return 1
    for i in range(n):
        stck.append([0,i])
        answer+=dfs(n)
    return answer
print(solution(4))