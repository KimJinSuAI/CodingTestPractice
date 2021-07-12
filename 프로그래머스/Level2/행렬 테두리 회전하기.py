def solution(rows, columns, queries):
    answer = []
    table = [[1+i+j*columns for i in range(columns)] for j in range(rows)]
    for query in queries:             # (x1, y1, x2, y2)
        next = table[query[0]-1][query[1]-1]
        min = 10000*10000
        for a in range(query[1]-1,query[3]):
            before = next
            next = table[query[0]-1][a]
            table[query[0]-1][a] = before
            if next<min:
                min = next
        for b in range(query[0],query[2]):
            before = next
            next = table[b][a]
            table[b][a] = before
            if next<min:
                min = next
        for c in range(query[3]-2,query[1]-2,-1):
            before = next
            next = table[b][c]
            table[b][c] = before
            if next<min:
                min = next
        for d in range(query[2]-2,query[0]-2,-1):
            before = next
            next = table[d][c]
            table[d][c] = before
            if next<min:
                min = next
        answer.append(min)

    return answer

# print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
print(solution(3,3,[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))
# print(solution(100,97,[[1,1,100,97]]))