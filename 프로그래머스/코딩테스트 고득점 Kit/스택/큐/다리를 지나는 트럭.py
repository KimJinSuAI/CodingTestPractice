def solution(bridge_length, weight, truck_weights):
    weight_n = 0
    time = 0
    
    truck_weights = list(map(list,zip(truck_weights,[0]*len(truck_weights))))
    going = []

    while truck_weights or going:
        time += 1
        if len(going)>0:
            if going[0][1]==bridge_length:
                weight_n -= going.pop(0)[0]
        if truck_weights:
            if weight_n+truck_weights[0][0]<=weight:
                going.append(truck_weights.pop(0))
                weight_n +=going[-1][0]
        for i in going:
            i[1]+=1

        if truck_weights:
            if weight_n+truck_weights[0][0]>weight:
                tmp = bridge_length-going[0][1]
                time += tmp
                for i in going:
                    i[1]+= tmp
    return time

print(solution(2,10,[7,4,5,6]))
print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]))