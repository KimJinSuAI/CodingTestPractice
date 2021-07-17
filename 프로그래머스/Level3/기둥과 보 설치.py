def gidoong(job, answer,n):
    if 0<=job[1]<n and 0<=job[0]<=n and (
                job[1]==0 or
                [job[0],job[1]-1,0] in answer or
                [job[0]-1,job[1],1] in answer or
                [job[0],job[1],1] in answer):
                return True
    return False

def bo(job, answer,n):
    if 0<=job[1]<=n and 0<=job[0]<n and ([job[0],job[1]-1,0] in answer or [job[0]+1,job[1]-1,0] in answer or
                ([job[0]-1,job[1],1] in answer and [job[0]+1,job[1],1] in answer)):
                return True
    return False

def solution(n, build_frame):
    answer = []
    for job in build_frame:
        if job[2]==0:           #[2]==0은 기둥
            if job[3]==1:       #[3]==1은 설치
                if gidoong(job, answer, n):
                    answer.append(job[:-1])
            else:               #삭제
                answer.remove(job[:-1])
                for stuff in answer:
                    if stuff == [job[0],job[1]+1,0]:
                        if not gidoong(stuff,answer,n):
                            break
                    elif stuff in [[job[0],job[1]+1,1], [job[0]-1, job[1]+1,1]]:
                        if not bo(stuff,answer,n):
                            break
                else:
                    continue
                answer.append(job[:-1])

        else:                   #보
            if job[3]==1:
                if bo(job, answer,n):
                    answer.append(job[:-1])
            else:
                answer.remove(job[:-1])
                for stuff in answer:
                    if stuff in [[job[0],job[1],0],[job[0]+1,job[1],0]]:
                        if not gidoong(stuff, answer, n):
                            break
                    elif stuff in [[job[0]-1,job[1],1],[job[0]+1,job[1],1]]:
                        if not bo(stuff, answer, n):
                            break
                else:
                    continue
                answer.append(job[:-1])
                
    return sorted(answer,key = lambda x: (x[0], x[1], x[2]))

print(solution(5,[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
print(solution(5,[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))