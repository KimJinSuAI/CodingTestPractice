def didYouWent(xy, before, stck):
    A = []
    B = []
    for s in range(len(stck)):
        if stck[s]==xy:
            A.append(s)
        elif stck[s]==before:
            B.append(s)
    for a in A:
        for b in B:
            if abs(a-b)==1:
                return True      
    return False
def solution(dirs):
    LRUD = {"L":(-1,0), "R":(1,0),"U":(0,1),"D":(0,-1)}
    stck = [[0,0]]
    xy=[0,0]
    answer = 0
    for dir in dirs:
        before = xy.copy()
        xy[0] = xy[0]+LRUD[dir][0]
        xy[1] = xy[1]+LRUD[dir][1]

        if xy[0]<-5 or xy[0]>5 or xy[1]<-5 or xy[1]>5:
            xy = before
            continue

        if not didYouWent(xy, before, stck):
            answer+=1
        stck.append(xy.copy())
    return answer

def solution(dirs):                                                         #다른사람 풀이
    s = set()
    d = {'U': (0,1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    x, y = 0, 0
    for i in dirs:
        nx, ny = x + d[i][0], y + d[i][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            s.add((x,y,nx,ny))
            s.add((nx,ny,x,y))
            x, y = nx, ny
    return len(s)//2

print(solution("LULLLLLLU"))
print(solution("ULURRDLLU"))