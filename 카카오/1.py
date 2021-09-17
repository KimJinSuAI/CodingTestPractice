def solution(id_list, report, k):
    answer = []
    ids = {}
    for i,id in enumerate(id_list):
        ids[id] = [set(),set(),0,i] #신고한 사람, ~에게 신고당함
    for rep in report:        
        rep = rep.split()
        ids[rep[0]][0].add(rep[1])
        ids[rep[1]][1].add(rep[0])
    
    for id in ids.keys():
        if len(ids[id][1])>=k:
            for i in ids[id][1]:
                ids[i][2]+=1
    tmp = sorted(ids.values(), key = lambda x: x[3])
    return [x[2] for x in tmp]

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2))