def dp(num):
    if crews.get(num,False):
        childrenFee = []
        count = 0
        for child in crews[num]:
            O,X = dp(child)
            childrenFee.append(O-X)
            if O<X:
                count +=1
            Cost[num][1]+=min(X,O)
            Cost[num][0]+=min(X,O)
        if count==0:
            Cost[num][0]+=min(childrenFee)
        return Cost[num][1],Cost[num][0]
    else:
        return Cost[num][1],Cost[num][0]

def solution(sales, links):
    global crews,Cost
    Cost = [[0]*2 for i in range(len(sales))]
    crews = {}                                                  # "번호": [자식들]
    for i,sale in enumerate(sales,0):
        Cost[i][1] = sale
    for boss, crew in links:
        crews[boss-1] = crews.get(boss-1,[])+[crew-1]

    return min(dp(0))
print(solution([14, 17, 15, 18, 19, 14, 13, 16, 28, 17],[[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]))

print(solution([10, 10, 1, 1],[[3,2], [4,3], [1,4]]))