def solution(routes):
    routes.sort()
    count = 0
    while routes:
        tmp = routes.pop()
        for i in range(len(routes)-1,-1,-1):
            if routes[i][0]<=tmp[1]<=routes[i][1]:#시간대가 걸쳐있는지 확인
                if tmp[0]<=routes[i][0]:#포함은아니고 겹치면
                    routes.append([routes[i][0],tmp[1]])
                else:#포함되어있으면
                    routes.append(tmp)
                routes.pop(i)
                break
            elif routes[i][0]<=tmp[0]<=routes[i][1] :
                if tmp[1]>=routes[i][1]:
                    routes.append([tmp[0],routes[i][1]])
                else:
                    routes.append(tmp)
                routes.pop(i)
                break
        else:
            count+=1
    return count

def solution(routes):
    routes = sorted(routes, key=lambda x: x[1])
    last_camera = -30000

    answer = 0

    for route in routes:
        if last_camera < route[0]:
            answer += 1
            last_camera = route[1]

    return answer

print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]), 2)