from collections import Counter
def solution(v):
    answer = []
    x = {}
    y = {}
    for x1,y1 in v:
        x[x1] = x.get(x1,0) + 1
        y[y1] = y.get(y1,0) + 1
    for tmpx in x.items():
         if tmpx[1] == 1:
             answer.append(tmpx[0])
             break
    for tmpy in y.items():
         if tmpy[1] == 1:
             answer.append(tmpy[0])
             break
        
    return answer

print(solution([[1, 4], [3, 4], [3, 10]]	))