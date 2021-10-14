import sys
N,M = list(map(int,sys.stdin.readline().split()))
N+=1
students = {}
stck = []
for i in range(M):
    a,b = list(map(int,sys.stdin.readline().split()))
    students[a] = students.get(a,[]) + [b]

visited = [False for _ in range(N)]
for i in range(1,N):
    if not visited[i]:
        Q = [i]
        while Q:
            node = Q[-1]
            if students.get(node,[]):
                next = students[node].pop()
                if not visited[next]:
                    Q.append(next)
            else:
                stck.append(Q.pop())
                visited[stck[-1]] = True

answer = ""
while stck:
    answer+=str(stck.pop())+" "
print(answer[:-1])

    
        
