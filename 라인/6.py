import re
def solution(records, k, date):
    prod = {}
    date = list(map(int,date.split("-")))

    for record in records:
        record = record.split()
        record[0][0] = list(map(int,record[0][0].split("-")))
        
        if date[0] < record[0][0] or (date[0]==record[0] and date[1]<record[0][1]) or (date[0]==record[0][0] and date[1]==record[0][1] and date[2]<record[0][2]) :    
            if prod:
                answer = sorted(list(prod.items()), key = lambda x: ((-len(x[1][0])/len(x[1][1]) if x[1][1]!=0 else 0),-x[1][2],int(x[0][3:])))
                return [x[0] for x in answer]
            else:
                return ["no result"]
        if prod.get(record[2],1)==1:            #상품초기화
            prod[record[2]] = [set(),set(),0]
        prod[record[2]][2]+=1
        if record[1] not in prod[record[2]][1]:            #처음구매
            prod[record[2]][1].add(record[1])
        else:                                     #재구매
            prod[record[2]][0].add(record[1])
    
    if prod:
        answer = sorted(list(prod.items()), key = lambda x: ((-len(x[1][0])/len(x[1][1]) if x[1][1]!=0 else 0),-x[1][2],int(x[0][3:])))
        return [x[0] for x in answer]
    else:
        return ["no result"]


print(solution(["2020-01-01 uid1000 pid5000"], 10, "2020-01-11"))
# print(solution(["2020-02-02 uid141 pid141", "2020-02-03 uid141 pid32", "2020-02-04 uid32 pid32", "2020-02-05 uid32 pid141"], 10, "2020-02-05"))
# print(solution(["2020-02-02 uid1 pid1", "2020-02-26 uid1 pid1", "2020-02-26 uid2 pid1", "2020-02-27 uid3 pid2", "2020-02-28 uid4 pid2", "2020-02-29 uid3 pid3", "2020-03-01 uid4 pid3", "2020-03-03 uid1 pid1", "2020-03-04 uid2 pid1", "2020-03-05 uid3 pid2", "2020-03-05 uid3 pid3", "2020-03-05 uid3 pid3", "2020-03-06 uid1 pid4"],10,"2020-03-05"))