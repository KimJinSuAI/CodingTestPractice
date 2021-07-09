import heapq
def solution(operations):
    heap = []
    for i in operations:
        if i[0]=='I':
            heapq.heappush(heap,int(i[2:]))
        else:
            if len(heap)>0:
                if i =="D 1":
                    heap.remove(heapq.nlargest(1,heap)[0])
                else :
                    heapq.heappop(heap)
                    

    if len(heap)==0:
        return [0,0]
    else:
        return [heapq.nlargest(1,heap)[0],heapq.heappop(heap)]

# print(solution(["I 16","D 1"]))
# print(solution(["I 7","I 5","I -5","D -1"]))
print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))