import sys,math
input = sys.stdin.readline
n = int(input()[:-1])
stars = []
for i in range(n):
    stars.append(list(map(float,input()[:-1].split())))

answer = 0
T = [stars[0]]
while len(T)!=n:
    mini = [-1,-1,sys.maxsize]
    for x,y in T:
        for x2,y2 in stars:
            if [x2,y2] not in T:
                tmp = math.sqrt((x2-x)**2+(y2-y)**2)
                if tmp< mini[2]:
                    mini = [x2,y2,tmp]
    answer+=mini[-1]
    T.append(mini[:-1])
print(round(answer,2))