def solution(a):
    if len(a)<3:
        return len(a)
    stck = [a[0],1,min(a[2:])]
    answer = 2
    for i in range(1,len(a)-1):
        stck[1] = a[i]
        if stck[0] > a[i-1]:        #좌측 최소 갱신
            stck[0] = a[i-1]
        if stck[2] == a[i-1]:       #현재 노드가 전체최소 다음노드면 break
            break
        if max(stck) != stck[1]:    #현재값이 좌측에서 최소면 +1
            answer+=1

    stck = [stck[2], 1 ,a[-1]]
    if i!= len(a)-2:
        for j in range(len(a)-2,i-1,-1):        # 우측부터 지역최소 찾으면 +1
            stck[1] = a[j]
            if stck[2] > a[j+1]:
                stck[2] = a[j+1]
            if max(stck) != stck[1]:
                answer+=1
            
    return answer

# print(solution([-1,-2,-5,-3,0]))
print(solution([9,-1,-5]))
# print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))
# print(solution([-4,-3,-2,-5,-5]))