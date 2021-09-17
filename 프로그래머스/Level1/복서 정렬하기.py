from collections import Counter
def solution(weights, head2head):
    answer = []
    for w,h,i in zip(weights, head2head, range(1,len(weights)+1)):
        tmp = []
        count = 0
        H = Counter(h)
        if H.get("W",0)==0 and H.get("L",0)==0:
            tmp.append(0)
        else:
            tmp.append(H.get("W",0)/(H.get("W",0)+H.get("L",0)))
        for oindex,result in enumerate(h):
            if result=="W" and weights[oindex]>w:
                count+=1
        tmp.append(count)
        tmp.append(w)
        tmp.append(i)
        answer.append(tmp)
    return [x[3] for x in sorted(answer, key= lambda y: (-y[0], -y[1], -y[2], y[3]))]
# print(solution([50,82,75,120], ["NLWL","WNLL","LWNW","WWLN"]))
print(solution([1,2],["NW","LN"]))