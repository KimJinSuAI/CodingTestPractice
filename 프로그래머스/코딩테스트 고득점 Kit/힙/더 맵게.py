import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0

    for i in range(len(scoville)):
        if len(scoville)>1 and scoville[0]<K:
            answer+=1
            heapq.heappush(scoville,heapq.heappop(scoville)+heapq.heappop(scoville)*2)
        else:
            break

    tmp = scoville.pop()
    if tmp<K:
        return -1
    else:
        return answer
    

print(solution([1, 2, 3, 9, 10, 12],7))