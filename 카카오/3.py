import math
def solution(fees, records):
    answer = []
    maxTime = 23*60+59
    basicTime, basicMoney, time, money = fees
    
    cars = {}
    for record in records:
        record = record.split()
        record[0] = record[0].split(":")
        record[0] = int(record[0][0])*60+int(record[0][1])
        if not cars.get(record[1], False):
            cars[record[1]] = [0,0,False]   #들어온시간, 누적시간, 있는지)

        if record[2]=="IN":
            cars[record[1]][0] = record[0]
            cars[record[1]][2] = True
        else:
            carTime = record[0]-cars[record[1]][0]
            cars[record[1]][1]+=carTime
            cars[record[1]][2] = False

            # if carTime<=basicTime:
            #     cars[record[1]][1] += basicMoney
            # else:
            #     cars[record[1]][1] += math.ceil(carTime/time)*money
    for car in cars.items():
        if car[1][2]:
            car[1][1]+=maxTime-car[1][0]
            car[1][2] = False
        if car[1][1]<=basicTime:
            cars[car[0]] = basicMoney
        else:
            cars[car[0]] = basicMoney+math.ceil((car[1][1]-basicTime)/time)*money
        
    return [y[1] for y in sorted(cars.items(), key = lambda x: x[0])]
# print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
print(solution([120, 0, 60, 591],["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))