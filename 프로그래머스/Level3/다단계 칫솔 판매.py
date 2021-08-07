import math
def solution(enroll, referral, seller, amount):
    graph = {}
    for e,r in zip(enroll,referral):
        graph[e] = graph.get(e,[0]) + [r]

    amount = list(map(lambda x: x*100, amount))

    for s,a in zip(seller, amount):
        man = s
        while man != "-":
            payForSeller = math.ceil(0.9*a)
            payForReferral = math.floor(a*0.1)
            graph[man][0]+=payForSeller
            if payForReferral==0:
                break
            a= payForReferral
            man = graph[man][1]
        

    return [x[0] for x in graph.values()]

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
["young", "john", "tod", "emily", "mary"],
[12, 4, 2, 5, 10]))