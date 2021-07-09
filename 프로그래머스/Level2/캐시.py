def solution(cacheSize, cities):
    answer = 0
    cache = {}
    cities=list(map(lambda x:x.lower(),cities))

    for i in cities:
        isMiss = cache.get(i,-1)
        if isMiss==-1:
            answer+=5
            cache[i]=-1
        else:
            answer+=1
            cache[i]=-1
        
        for j in cache.keys():
            cache[j]+=1

        if len(cache)>cacheSize:
            tmp = sorted(cache.keys(), reverse=True, key = lambda x: cache[x])[0]
            del cache[tmp]
        

    return answer

# print(solution(3,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
# print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
print(solution(	2, ["Jeju", "Pangyo", "NewYork", "newyork"]))