from collections import deque
def solution(n, start, end, roads, traps):
    answer = -1
    miro = {}
    for i,road in enumerate(roads):
        miro[road[0]] = miro.get(road[0],{})
        miro[road[0]][road[1]] = miro[road[0]].get(road[1],[])+[[i,road[2]]]
        miro[road[1]] = miro.get(road[1],{})
        miro[road[1]][road[0]] = miro[road[1]].get(road[0],[])+[[i,-1]]
    Q = deque()
    Q.append((start,0,miro.copy()))
    while Q:
        node = Q.popleft()
        if answer!=-1 and node[1]>=answer:
            continue
        elif node[0]==end:
            answer = node[1]
            continue
        if node[0] in traps:   #trap
            for road in node[2][node[0]].items():#현재다리에 연결된 노드별 처리. road[0] = 노드, road[1] = [번호, 가중치]
                for r in road[1]:                #노드에 연결된 다리별 처리
                    for tmp in node[2][road[0]].items():    #상대 노드와 같은번호의 다리 찾아 처리
                        if tmp[0]==node[0]:     #상대의 현재노드찾음
                            for x in tmp[1]:    #상대노드에서도 같은 번호의 다리 찾음
                                if x[0]==r[0]:
                                    if r[1]==-1:
                                        r[1] = x[1]
                                        x[1] = -1
                                    else:
                                        x[1] = r[1]
                                        r[1] = -1
                                    break
                            break
           

        for road in node[2][node[0]].items():
            for r in road[1]:
                if r[1]==-1:
                    continue
                Q.append((road[0],node[1]+r[1],node[2].copy()))
    return answer
# print(solution(4,1,4,[[1, 2, 1], [3, 2, 1], [2, 4, 1]],[2, 3]))

print(solution(4,1,3,[[1, 2, 1], [4, 3, 1], [4, 2, 1]],[2,4]))