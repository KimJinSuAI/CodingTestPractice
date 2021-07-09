#문제를 잘읽자.. 최대2명만 탈 수 있다.
#2명이상인줄 -> 큰놈정렬해서 큰놈들2명 제거 -> 큰놈1 작은놈1
def solution(people, limit):
    count=0
    people.sort(reverse = True)
    people = dict(enumerate(people))
    i=0
    j=len(people)-1
    while people:
        count+=1
        now = people[i]
        if len(people)>1 and now+people[j]<=limit:
            del people[j]    
            j-=1
        del people[i]
        i+=1

    return count

    # while people:
    #     count+=1
    #     x = list(people.keys())[0]
    #     now = people[x]
    #     del people[x]

    #     for i in people.keys():
    #         if now + people[i]<=limit:
    #             now = 0
    #             del people[i]
    #             break

    # return count
print(solution([70, 50, 80, 50], 100), 3)
print(solution([70,80,50], 100), 3)