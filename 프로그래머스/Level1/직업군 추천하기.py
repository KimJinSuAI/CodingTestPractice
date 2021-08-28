def solution(table, languages, preference):
    Ntable = []
    for t in table:
        Ntable.append(t.split(" "))
        
    answer = [[Ntable[i][0],0]for i in range(len(Ntable))]
    for l,p in zip(languages,preference):
        for i in range(len(Ntable)):
            try:
                answer[i][1] += (6-Ntable[i].index(l))*p
            except:
                answer[i][1] += 0
                
    return sorted(answer, key = lambda x: (-x[1],x[0]))[0][0]

print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"],
["PYTHON", "C++", "SQL"],[7,5,5]))