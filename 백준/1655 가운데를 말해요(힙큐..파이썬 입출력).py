# import sys
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#         self.leftnum = 0
#         self.rightnum = 0
        
# N = int(sys.stdin.readline())
# tmp = int(sys.stdin.readline())
# nums = Node(tmp)
# answer = [tmp]
# count = 1
# for i in range(N-1):
#     tmp = int(sys.stdin.readline())
#     nowNode = nums
#     while nowNode!=None:                        #삽입
#         beforeNode = nowNode
#         if tmp>=nowNode.data:
#             nowNode.rightnum+=1
#             nowNode = nowNode.right
#         else:
#             nowNode.leftnum+=1
#             nowNode = nowNode.left
#     if tmp>=beforeNode.data:
#         beforeNode.right = Node(tmp)
#     else:
#         beforeNode.left = Node(tmp)
#     count+=1

    
#     target = (count)//2-1 if count%2==0 else count//2
#     nowNode = nums
#     now = nowNode.leftnum
#     while True:
#         if target==now:
#             answer.append(nowNode.data)
#             break
#         elif target>now:
#             nowNode = nowNode.right
#             now+=nowNode.leftnum+1
#         else:
#             nowNode = nowNode.left
#             now-=nowNode.rightnum+1

# for a in answer:
#     print(a)


import sys
import heapq
left, right = [],[]
N = int(sys.stdin.readline())
answer = []
for i in range(N):
    tmp = int(sys.stdin.readline())
    if len(left)==len(right):
        heapq.heappush(left,-tmp)
    else:
        heapq.heappush(right,tmp)
    if right and right[0]<-left[0]:
        tmp = heapq.heappop(left)
        heapq.heappush(left,-heapq.heappop(right))
        heapq.heappush(right,-tmp)
    answer.append(-left[0])
    
for a in answer:
    print(a)