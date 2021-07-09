import pandas as pd
import operator
def solution(genres, plays):
    df = pd.DataFrame([genres,plays]).T
    sum={}
    count = {}
    for i,j in zip(df[0], df[1]):
        if i not in sum:
            sum[i]=j
            count[i]=0
        else: 
            sum[i]=sum[i]+j
    
    selectedGenre = list(pd.DataFrame(sorted(sum.items(), reverse = True, key=operator.itemgetter(1)))[0])#장르순위
    sortedList = sorted(zip(genres,range(len(genres)),plays), reverse = True, key=operator.itemgetter(2))
    answer = []
    for i in selectedGenre:
            for k in range(len(sortedList)):
                if i==sortedList[k][0] and count[i]<2:
                    answer.append(sortedList[k][1])
                    count[i]=count[i]+1


    return answer

def solution2(genres, plays):
    answer = []
    d = {e:[] for e in set(genres)}
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1] , e[2]])
    genreSort =sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)
    for g in genreSort:
        temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
        answer += temp[:min(len(temp),2)]
    return answer
print(solution(["c", "a", "b", "a", "c", "c"],[100, 200, 300, 400, 500, 600]))
# print(solution(["classic", "pop", "classic", "classic","jazz","pop", "Rock", "jazz"],[500, 600, 150, 800, 1100, 2500, 100, 1000]))
print(sum([100,0]+[200,1]))