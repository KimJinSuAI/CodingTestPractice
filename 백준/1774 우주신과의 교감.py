import sys
input = sys.stdin.readline
N, M = map(int,input()[:-1].split())
t = set()
vertices = []
for i in range(N):
    vertices.append(list(map(int,input()[:-1].split())))
for j in range(M):
    a,b = map(int,input()[:-1].split())
    a-=1;b-=1
    t.add(a); t.add(b)
T = []
for i in t:
    T.append(vertices[i])

answer = 0
if not T:
    T.append(vertices[0])

while len(T)!=N:
    mini = [-1,-1,sys.maxsize]
    for x,y in vertices:
        if [x,y] not in T:
            for x2,y2 in T:
                tmp =((x2-x)**2+(y2-y)**2)**0.5
                if mini[2]>tmp:
                    mini = (x2,y2,tmp)
    answer+=mini[2]
    T.append([x2,y2])
print(round(answer,2))




