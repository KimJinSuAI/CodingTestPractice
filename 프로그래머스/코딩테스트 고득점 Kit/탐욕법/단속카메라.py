def solution(routes):
    routes.sort()
    count = 0
    while routes:
        tmp = routes.pop()
        for i in range(len(routes)-1,-1,-1):
            if tmp[1]>=routes[i][0] and tmp[1]<=routes[i][1]:
                if tmp[0]<=routes[i][0]:
                    routes.append([routes[i],tmp[1]])
                else:
                    routes.append(tmp)
                routes.pop(i)
                break
            elif tmp[0]<=routes[i][1] and tmp[0]>=routes[i][0]:
                if tmp[1]>=routes[i][1]:
                    routes.append([tmp[0],routes[i][1]])
                else:
                    routes.append(tmp)
                routes.pop(i)
                break
        else:
            count+=1
    return count

print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]), 2)