import sys
def solution(matrix_sizes):
    answer = 0
    d = [matrix_sizes[0][0]]
    for i in range(len(matrix_sizes)):
        d.append(matrix_sizes[i][1])
    length = len(d)
    M = [[0 for x in range(length)] for y in range(length)]
    for diag in range(1, length):
        for i in range(1, length-diag):
            j = i+diag
            M[i][j] = sys.maxsize
            for k in range(i,j):
                M[i][j] = min(M[i][j], M[i][k] + M[k+1][j] + d[i-1]*d[k]*d[j])
    answer = M[1][length-1]
    return answer

def solution(matrix_sizes):
    d = [matrix_sizes[0][0]]
    for tmp in matrix_sizes:
        d.append(tmp[1])
    M = [[0] * len(matrix_sizes) for _ in range(len(matrix_sizes))]
    for diag in range(len(matrix_sizes)):
        for i in range(len(matrix_sizes)-diag):
            j = i+diag
            if i==j:
                M[i][j] = 0
            else:
                M[i][j] = float('inf')
                for k in range(i,j):
                        M[i][j] = min(M[i][j], M[i][k]+M[k+1][j]+d[i-1]*d[k]*d[j])
    return M[0][len(matrix_sizes)-1]                                            



print(solution([[5, 3], [3, 2], [2, 6]]), 90)
# print(solution([[5,3],[3,10],[10,6]]))
print(solution([[5,200],[200,5],[5,1]]), 2000)