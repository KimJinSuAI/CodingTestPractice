def getTheGroups(n, queryType, students1, students2):
    answer = []
    people = [[False]*n for _ in range(n)]
    for i in range (n):
        people[i][i] = True
        
    for i,query in enumerate(queryType):
        s1 = students1[i]-1
        s2 = students2[i]-1
        if query=="Friend":
            
            for j in range(n):
                people[s1][j] |= people[s2][j]
            for j in range(n):
                if people[s1][j]:
                    people[j] = people[s1]
                
        else:
            c1 = 0
            c2 = 0
            for j in range(n):
                if people[s1][j]:
                    c1+=1
                if people[s2][j]:
                    c2+=1
            answer.append(c1+c2)
    return answer
# print(getTheGroups(4,["Friend","Friend","Total"],[1,2,1],[2,3,4]))
print(getTheGroups(3,["Friend","Total"],[1,2],[2,3]))