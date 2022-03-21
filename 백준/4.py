def solution(n, m, k, records):
    for record in records:
        mini = min(record)
        record = list(map(lambda x: x-mini+1, record))
        arr = [0 for _ in range(n+1)]
        for i in record:
            arr[i] = 1
        print(arr)
    answer = []
    return answer

print(solution(8, 4, 4, [[1, 5, 1, 3], [5, 7, 5, 6]]))