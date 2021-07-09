def isKeepingDistance(places, people, i):   
        for f in range(len(people)-1):
            for s in range(f+1, len(people)):
                distance = abs(people[f][0] - people[s][0]) + abs(people[f][1]-people[s][1])
                if distance <= 1:
                    return 0
                elif distance == 2:
                    if people[f][0]==people[s][0]:
                        if places[i][people[f][0]][people[f][1]+1]!="X":
                            return 0
                    elif people[f][1]<people[s][1]:
                        if places[i][people[f][0]][people[f][1]+1]!="X" or places[i][people[s][0]][people[s][1]-1]!="X":
                            return 0
                    elif people[f][1]==people[s][1]:
                        if places[i][people[f][0]+1][people[f][1]]!="X":
                            return 0
                    elif people[f][1]>people[s][1]:
                        if places[i][people[f][0]][people[f][1]-1]!="X" or places[i][people[s][0]][people[s][1]+1]!="X":
                            return 0
        return 1

def solution(places):
    answer = []
    for i in range(len(places)):
        people = []
        for j in range(len(places[i])):
            for k in range(len(places[i][j])):
                if places[i][j][k]=="P":
                    people.append([j,k])
        
        answer.append(isKeepingDistance(places,people,i))

    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))