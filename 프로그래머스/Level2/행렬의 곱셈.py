def solution(arr1, arr2):
    arr = [[0] * len(arr2[0]) for i in range(len(arr1))]
    for i in range(len(arr)):
        for j in range(len(arr2[0])):
            arr[i][j] = sum([arr1[i][x]*arr2[x][j] for x in range(len(arr1[0]))])
    return arr

print(solution([[1, 4], [3, 2], [4, 1]],[[3, 3], [3, 3]]))

print(solution([[1, 2, 3], [4, 5, 6]], [[1, 4], [2, 5], [3, 6]]))