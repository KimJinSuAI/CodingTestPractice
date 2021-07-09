def solution(citations):
    citations.sort(reverse=True)
    max = 0
    for i in range(1,len(citations)+1):
        count1=0
        count2=0
        for j in range(len(citations)):
            if citations[j]>=i:
                count1 = count1+1
            if citations[j]<=i:
                count2 = count2+1
        if i<=count1 and i>=count2:
            if max<i:
                max = i

    return max

print(solution([3, 0, 6, 1, 5]))