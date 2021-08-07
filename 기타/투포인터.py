#data에서 합이 sum인 구간의 개수 구해줌
def twoPointer(sum, data):
    start, end = 0,0
    result, total = 0, 0
    for start in range(len(data)):
        while end < len(data) and total < sum:
            total += data[end]
            end+=1
        if total == sum:
            result+=1
        total -= data[start]
    return result

print(twoPointer(5,[1,2,3,2,5]))