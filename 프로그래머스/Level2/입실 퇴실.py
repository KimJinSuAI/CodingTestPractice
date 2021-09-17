def solution(enter, leave):
    people = [0]*len(enter)
    i = 0
    now = []
    for l in leave:
        while i!= len(enter) and l not in now:
            now.append(enter[i])
            i+=1
        now.remove(l)
        people[l-1] += len(now)
        for n in now:
            people[n-1]+=1
        

    answer = []
    return people

print(solution(	[1, 3, 2], [1, 2, 3]))
print(solution([1, 4, 2, 3], [2, 1, 3, 4]))